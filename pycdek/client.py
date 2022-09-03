from pycdek import entities
from pycdek import endpoints
from pycdek.auth import TokenManager
from typing import Optional, Union
from uuid import UUID


class CDEK:
    def __init__(self, client_id: str = None, client_secret: str = None):
        self.credentials = entities.ClientCredentials(
            client_id=client_id, client_secret=client_secret
        )
        self.token = TokenManager.get_token(self.credentials)

    def __call__(self, Endpoint: endpoints.Endpoint, *args, **kwargs):
        endpoint = Endpoint()
        try:
            return endpoint(*args, headers=self.headers, **kwargs)
        except PermissionError as e:
            self.token = TokenManager.gen_new_token(self.credentials)
            TokenManager.write_token_to_file(self.token)
            return self(Endpoint, *args, **kwargs)

    @property
    def headers(self):
        if not self.token.is_valid():
            self.token = TokenManager.gen_new_token(self.credentials)
            TokenManager.write_token_to_file(self.token)
        headers = entities.Headers(Authorization=self.token.access_token)
        return headers.dict(by_alias=True)

    def get_cities(self, **kwargs):
        r = entities.CitySearchRequest(**kwargs)
        return self(endpoints.CityList, r.dict())

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

    def get_available_tariffs(self, **kwargs) -> entities.TariffListResponse:
        r = entities.TariffListRequest(**kwargs)
        return self(endpoints.CalculateByAvailableTariffs, r.json())

    def register_order(self, **kwargs) -> entities.OrderInfoResponse:
        r = entities.OrderCreationRequest(**kwargs)
        return self(endpoints.NewOrder, r.json())

    def get_contact(self, name: str, phones: Union[str | list]) -> entities.Contact:
        phone_list = []
        if not isinstance(phones, list):
            phones = [phones]
        for phone in phones:
            phone_list.append(entities.Phone(number=phone))
        return entities.Contact(name=name, phones=phone_list)

    def get_office(self, **kwargs) -> list[entities.Office]:
        r = entities.OfficeListRequest(**kwargs)
        return self(endpoints.OfficeList, r.dict())

    def get_order_info(self, uuid: Union[str | UUID]) -> entities.OrderInfoResponse:
        if isinstance(uuid, UUID):
            uuid = str(uuid)
        return self(endpoints.OrderInfo, uuid=uuid)
