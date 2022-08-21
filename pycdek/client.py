import uuid
from pycdek import entities
from pycdek import endpoints
from pycdek.auth import TokenManager


class CDEK:
    def __init__(self, client_id: str = None, client_secret: str = None):
        self.credentials = entities.ClientCredentials(
            client_id=client_id, client_secret=client_secret
        )
        self.token = TokenManager.get_token(self.credentials)

    def __call__(self, Endpoint, *args, **kwargs):
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

    def get_location(self, address, city):
        return entities.Location(
            code=city.code, 
            longitude=city.longitude,
            latitude=city.latitude,
            country_code=city.country_code,
            region=city.region,
            sub_region=city.sub_region,
            city=city.city,
            address=address
        )

    def create_package(
            self, 
            name, 
            weight,
            ware_key=None,
            payment=None,
            cost=None,
            vat_sum=None,
            vat_rate=None,
            amount=1
        ):
        item = entities.Item(
            name=name,
            ware_key=ware_key or uuid.uuid4().hex[:20],
            payment=entities.Money(
                value=payment if payment else 0,
                vat_sum=vat_sum,
                vat_rate=vat_rate
            ),
            cost=cost or 0,
            weight=weight,
            amount=amount
        )
        return entities.Package(weight=weight, items=[item])

    def get_available_tariffs(self, **kwargs):
        r = entities.TariffListRequest(**kwargs)
        return self(endpoints.CalculateByAvailableTariffs, r.json())

    def register_package(self, **kwargs):
        r = entities.OrderCreationRequest(**kwargs)
        return self(endpoints.NewOrder, r.json())

    def get_contact(self, name, phones):
        phone_list = []
        if not isinstance(phones, list):
            phones = [phones]
        for phone in phones:
            phone_list.append(entities.Phone(number=phone))
        return entities.Contact(name=name, phones=phone_list)

    def get_office(self, **kwargs):
        r = entities.OfficeListRequest(**kwargs)
        return self(endpoints.OfficeList, r.dict())
