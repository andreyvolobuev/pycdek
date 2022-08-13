import entities
import endpoints
from auth import TokenManager


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
        return self(endpoints.CityList, r)

    def create_package(self, **kwargs):
        return entities.Package(**kwargs)

    def get_available_tariffs(self, **kwargs):
        r = entities.TariffListRequest(**kwargs)
        return self(endpoints.CalculateByAvailableTariffs, r.json())

    def register_package(self, **kwargs):
        r = entities.OrderCreationRequest(**kwargs)
        return self(endpoints.NewOrder, r.json())


if __name__ == "__main__":
    cdek = CDEK(CLIENT_ID, CLIENT_SECRET)

    cities = cdek.get_cities(city="Москва")
    moscow = cities[0]

    cities = cdek.get_cities(city="Владивосток")
    vladivostok = cities[0]

    package = cdek.create_package(weight=1)

    tariffs = cdek.get_available_tariffs(
        from_location=moscow, to_location=vladivostok, packages=[package]
    )

    tariff = tariffs.cheapest

    package = cdek.register_package(
        tariff=tariff,
        from_location=moscow,
        to_location=vladivostok,
        packages=[package],
        services=[],
    )

    print(package)
