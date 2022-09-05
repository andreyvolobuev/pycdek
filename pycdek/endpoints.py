import aiohttp
from pycdek import entities
from pydantic import parse_obj_as, BaseModel
from abc import ABC, abstractmethod, abstractproperty
from typing import Type


class Endpoint(ABC):
    _BASE = "https://api.cdek.ru/v2/"

    @abstractproperty
    def _URL(self) -> str:
        """returns endpoint url"""

    @abstractproperty
    def _METHOD(self) -> str:
        """returns endpoint method"""

    @abstractproperty
    def _OBJECT(self) -> Type[BaseModel]:
        """returns target object"""

    @property
    def URL(self) -> str:
        return self._BASE + self._URL

    async def __call__(self, params, **kwargs) -> Type[BaseModel]:
        url = self.URL.format(kwargs.get("uuid"))
        session = getattr(kwargs.get("session"), self._METHOD)
        async with session(url, params=params, headers=kwargs.get("headers")) as r:
            if r.status == 401:
                raise PermissionError("Headers are invalid")
            return parse_obj_as(self._OBJECT, await r.json())


class Auth(Endpoint):
    _URL = "oauth/token"
    _METHOD = "post"
    _OBJECT = entities.AccessToken


class NewOrder(Endpoint):
    _URL = "orders"
    _METHOD = "post"
    _OBJECT = entities.OrderInfoResponse


class OfficeList(Endpoint):
    _URL = "deliverypoints"
    _METHOD = "get"
    _OBJECT = list[entities.Office]


class CityList(Endpoint):
    _URL = "location/cities"
    _METHOD = "get"
    _OBJECT = list[entities.City]


class CalculateByAvailableTariffs(Endpoint):
    _URL = "calculator/tarifflist"
    _METHOD = "post"
    _OBJECT = entities.TariffListResponse


class OrderInfo(Endpoint):
    _URL = "orders/{}"
    _METHOD = "get"
    _OBJECT = entities.OrderInfoResponse


class EditOrder(Endpoint):
    _URL = "orders/{}"
    _METHOD = "patch"
    _OBJECT = entities.OrderInfoResponse


class DeleteOrder(Endpoint):
    _URL = "orders/{}"
    _METHOD = "delete"
    _OBJECT = entities.OrderInfoResponse


class OrderRefusal(Endpoint):
    _URL = "orders/{}/refusal"
    _METHOD = "post"
    _OBJECT = entities.OrderInfoResponse


class IntakeRequest(Endpoint):
    _URL = "intakes"
    _METHOD = "post"
    _OBJECT = entities.OrderInfoResponse


class IntakeInfo(Endpoint):
    _URL = "intakes/{}"
    _METHOD = "get"
    _OBJECT = entities.OrderInfoResponse


class DeleteIntake(Endpoint):
    _URL = "intakes/{}"
    _METHOD = "delete"
    _OBJECT = entities.OrderInfoResponse


class CreateOrderReceipt(Endpoint):
    _URL = "print/orders"
    _METHOD = "post"
    _OBJECT = entities.OrderInfoResponse


class GetOrderReceipt(Endpoint):
    _URL = "print/orders/{}"
    _METHOD = "get"
    _OBJECT = entities.OrderInfoResponse


class CreateOrderBarcode(Endpoint):
    _URL = "print/barcodes"
    _METHOD = "post"
    _OBJECT = entities.OrderInfoResponse


class GetOrderBarcode(Endpoint):
    _URL = "print/barcodes/{}"
    _METHOD = "get"
    _OBJECT = entities.OrderInfoResponse


class CreateDeliveryArrangement(Endpoint):
    _URL = "delivery"
    _METHOD = "post"
    _OBJECT = entities.OrderInfoResponse


class GetDeliveryArrangement(Endpoint):
    _URL = "delivery"
    _METHOD = "get"
    _OBJECT = entities.OrderInfoResponse


class GetPassportData(Endpoint):
    _URL = "passport"
    _METHOD = "get"
    _OBJECT = entities.OrderInfoResponse


class GetOrderCheck(Endpoint):
    _URL = "check"
    _METHOD = "get"
    _OBJECT = entities.OrderInfoResponse


class AddPrealert(Endpoint):
    _URL = "prealert"
    _METHOD = "post"
    _OBJECT = entities.OrderInfoResponse


class GetPrealert(Endpoint):
    _URL = "prealert/{}"
    _METHOD = "get"
    _OBJECT = entities.OrderInfoResponse


class AddWebhook(Endpoint):
    _URL = "webhooks"
    _METHOD = "post"
    _OBJECT = entities.OrderInfoResponse


class RegionsList(Endpoint):
    _URL = "location/regions"
    _METHOD = "get"


class CalculateByTariff(Endpoint):
    _URL = "calculator/tariff"
    _METHOD = "post"


class CalculateCustomsTariff(Endpoint):
    _URL = "ddp"
    _METHOD = "post"
