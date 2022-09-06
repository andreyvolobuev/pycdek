import aiohttp
from pycdek import entities
from pycdek import endpoints
from typing import Optional, Union
from uuid import UUID
from pathlib import Path


class CDEK:
    def __init__(self, client_id: str = None, client_secret: str = None):
        self.credentials = entities.ClientCredentials(
            client_id=client_id, client_secret=client_secret
        )
        self.token = None

    async def __call__(
        self,
        Endpoint: endpoints.Endpoint,
        payload: dict = None,
        auth: bool = False,
        **kwargs
    ):
        endpoint = Endpoint()
        try:
            async with aiohttp.ClientSession() as session:
                return await endpoint(
                    payload,
                    session=session,
                    headers={} if auth else await self.headers,
                    **kwargs
                )
        except PermissionError:
            self.token = await TokenManager.get_token(self)
            return await self(Endpoint, payload)

    @property
    async def headers(self):
        if not self.token or not self.token.is_valid():
            self.token = await TokenManager.get_token(self)
        headers = entities.Headers(Authorization=self.token.access_token)
        return headers.dict(by_alias=True)

    async def get_cities(self, **kwargs):
        r = entities.CitySearchRequest(**kwargs)
        return await self(endpoints.CityList, r.dict(exclude_none=True))

    def get_location(self, address: str, city: entities.City) -> entities.Location:
        return entities.Location(
            code=city.code,
            longitude=city.longitude,
            latitude=city.latitude,
            country_code=city.country_code,
            region=city.region,
            sub_region=city.sub_region,
            city=city.city,
            address=address,
        )

    def create_package(
        self,
        name: str,
        weight: int,
        payment: Optional[int] = None,
        cost: Optional[int] = None,
        vat_sum: Optional[int] = None,
        vat_rate: Optional[int] = None,
        amount: Optional[int] = 1,
    ) -> entities.Package:
        item = entities.Item(
            name=name,
            payment=entities.Money(
                value=payment if payment else 0, vat_sum=vat_sum, vat_rate=vat_rate
            ),
            cost=cost or 0,
            weight=weight,
            amount=amount,
        )
        return entities.Package(weight=weight, items=[item])

    async def get_available_tariffs(self, **kwargs) -> entities.TariffListResponse:
        r = entities.TariffListRequest(**kwargs)
        return await self(endpoints.CalculateByAvailableTariffs, r.json())

    async def register_order(self, **kwargs) -> entities.OrderInfoResponse:
        r = entities.OrderCreationRequest(**kwargs)
        return await self(endpoints.NewOrder, r.json())

    def get_contact(self, name: str, phones: Union[str | list]) -> entities.Contact:
        phone_list = []
        if not isinstance(phones, list):
            phones = [phones]
        for phone in phones:
            phone_list.append(entities.Phone(number=phone))
        return entities.Contact(name=name, phones=phone_list)

    async def get_office(self, **kwargs) -> list[entities.Office]:
        r = entities.OfficeListRequest(**kwargs)
        return await self(endpoints.OfficeList, r.dict())

    async def get_order_info(
        self, uuid: Union[str | UUID]
    ) -> entities.OrderInfoResponse:
        if isinstance(uuid, UUID):
            uuid = str(uuid)
        return await self(endpoints.OrderInfo, uuid=uuid)

    async def auth(self):
        return await self(endpoints.Auth, self.credentials.dict(), auth=True)


class TokenManager:
    @staticmethod
    def _get_tmp_token_path(
        dir_name: str = "/tmp/pycdek", file_name: str = "_token.json"
    ) -> Path:
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        return Path(dir_name, file_name)

    @staticmethod
    def _read_token_from_file() -> Optional[entities.AccessToken]:
        tmp_file = TokenManager._get_tmp_token_path()
        if tmp_file.exists():
            with open(tmp_file) as file:
                token = entities.AccessToken.parse_raw(file.read())
                if token.is_valid():
                    return token

    @staticmethod
    def write_token_to_file(token: entities.AccessToken) -> None:
        tmp_file = TokenManager._get_tmp_token_path()
        tmp_file.touch()
        with open(tmp_file, "w") as file:
            file.write(token.json())

    @staticmethod
    async def get_token(client: CDEK) -> entities.AccessToken:
        """
        Чтобы не делать запрос к СДЭКу каждый раз, когда нам нужен токен,
        мы будем сохранять его во временный файл и брать от туда до тех пор,
        пока не истечет срок его валидности.

        @param credentials: Объект логина и пароля интеграции СДЭК
        """
        token = TokenManager._read_token_from_file()
        if not token:
            token = await client.auth()
            TokenManager.write_token_to_file(token)
        return token
