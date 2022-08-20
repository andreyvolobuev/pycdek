import requests
from pycdek import entities
from pydantic import parse_obj_as
from abc import ABC, abstractmethod, abstractproperty


class Endpoint(ABC):
    _BASE = "https://api.cdek.ru/v2/"

    @abstractproperty
    def _URL(self) -> str:
        """returns endpoint url"""

    @abstractproperty
    def _METHOD(self) -> str:
        """returns endpoint method"""

    @abstractproperty
    def _OBJECT(self):
        """returns target object"""

    @property
    def URL(self) -> str:
        return self._BASE + self._URL

    def __call__(self, *args, **kwargs):
        url = self.URL
        if "%s" in self.URL:
            uuid = getattr(data, "uuid")
            url = self.URL % uuid
        session = getattr(requests, self._METHOD)
        r = session(url, *args, **kwargs)
        if r.status_code == 401:
            raise PermissionError("Headers are invalid")
        print('aaaa\n\n', r.json(), '\n\n\n')
        return parse_obj_as(self._OBJECT, r.json())


class Auth(Endpoint):
    _URL = "oauth/token"
    _METHOD = "post"
    _OBJECT = entities.AccessToken


class NewOrder(Endpoint):
    _URL = "orders"
    _METHOD = "post"
    _OBJECT = entities.OrderCreationResponse


class OrderInfo(Endpoint):
    _URL = "orders/%s"
    _METHOD = "get"


class EditOrder(Endpoint):
    _URL = "orders/%s"
    _METHOD = "patch"


class DeleteOrder(Endpoint):
    _URL = "orders/%s"
    _METHOD = "delete"


class OrderRefusal(Endpoint):
    _URL = "orders/%s/refusal"
    _METHOD = "post"


class IntakeRequest(Endpoint):
    _URL = "intakes"
    _METHOD = "post"


class IntakeInfo(Endpoint):
    _URL = "intakes/%s"
    _METHOD = "get"


class DeleteIntake(Endpoint):
    _URL = "intakes/%s"
    _METHOD = "delete"


class CreateOrderReceipt(Endpoint):
    _URL = "print/orders"
    _METHOD = "post"


class GetOrderReceipt(Endpoint):
    _URL = "print/orders/%s"
    _METHOD = "get"


class CreateOrderBarcode(Endpoint):
    _URL = "print/barcodes"
    _METHOD = "post"


class GetOrderBarcode(Endpoint):
    _URL = "print/barcodes/%s"
    _METHOD = "get"


class CreateDeliveryArrangement(Endpoint):
    _URL = "delivery"
    _METHOD = "post"


class GetDeliveryArrangement(Endpoint):
    _URL = "delivery"
    _METHOD = "get"


class GetPassportData(Endpoint):
    _URL = "passport"
    _METHOD = "get"


class GetOrderCheck(Endpoint):
    _URL = "check"
    _METHOD = "get"


class AddWebhook(Endpoint):
    _URL = "webhooks"
    _METHOD = "post"


class OfficeList(Endpoint):
    _URL = "deliverypoints"
    _METHOD = "get"
    _OBJECT = list[entities.Office]


class RegionsList(Endpoint):
    _URL = "location/regions"
    _METHOD = "get"


class CityList(Endpoint):
    _URL = "location/cities"
    _METHOD = "get"
    _OBJECT = list[entities.City]


class CalculateByTariff(Endpoint):
    _URL = "calculator/tariff"
    _METHOD = "post"


class CalculateByAvailableTariffs(Endpoint):
    _URL = "calculator/tarifflist"
    _METHOD = "post"
    _OBJECT = entities.TariffListResponse


class CalculateCustomsTariff(Endpoint):
    _URL = "ddp"
    _METHOD = "post"
