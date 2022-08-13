import uuid
from enum import Enum, IntEnum, auto
from uuid import UUID
from typing import Optional, Literal
from pydantic import BaseModel, Field, ValidationError, validator, constr, conlist
from datetime import datetime, timedelta, date


class Currency(IntEnum):
    RUB = 1
    KZT = 2
    USD = 3
    EUR = 4
    GBP = 5
    CNY = 6
    BYN = 7
    UAH = 8
    KGS = 9
    AMD = 10
    TRL = 11
    THB = 12
    KRW = 13
    AED = 14
    UZS = 15
    MNT = 16
    PLN = 17
    AZN = 18
    GEL = 19


class DeliveryMode(IntEnum):
    DOOR_DOOR = 1
    DOOR_WAREHOUSE = 2
    WAREHOUSE_DOOR = 3
    WAREHOUSE_WAREHOUSE = 4
    DOOR_POSTMATE = 6
    WAREHOUSE_POSTMATE = 7


class OrderType(IntEnum):
    ECOMMERCE = 1
    DELIVERY = 2


class WeekDay(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class OwnershipForm(IntEnum):
    AO = 9
    ZAO = 61
    IP = 63
    OAO = 119
    OOO = 137
    PAO = 147


class Language(str, Enum):
    RUSSIAN: str = "rus"
    ENGLISH: str = "eng"
    CHINESE: str = "zho"


class OfficeType(str, Enum):
    PVZ: str = "PVZ"
    POSTAMAT: str = "POSTAMAT"
    ALL: str = "ALL"


class OfficeOwner(str, Enum):
    CDEK: str = "cdek"
    INPOST: str = "InPost"


class TariffCode(IntEnum):
    # ECOMMERCE TARIFFS
    INTERNATIONAL_DOCS = 7
    INTERNATIONAL_CARGO = 8
    PARCEL_WH_WH = 136
    PARCEL_WH_DOOR = 137
    PARCEL_DOOR_WH = 138
    PARCEL_DOOR_DOOR = 139
    PARCEL_DOOR_POST = 366
    PARCEL_WH_POST = 368
    ECONOM_WH_WH = 233
    ECONOM_WH_DOOR = 234
    ECONOM_WH_POST = 378
    CDEK_EXPRESS_WH_WH = 291
    CDEK_EXPRESS_WH_DOOR = 294
    CDEK_EXPRESS_DOOR_WH = 295
    CDEK_EXPRESS_DOOR_DOOR = 293
    BLITZ_EXPRESS_01 = 66
    BLITZ_EXPRESS_02 = 67
    CHINESE_EXP_WH_DOOR = 246
    CHINESE_EXP_WH_WH = 243
    CHINESE_EXP_DOOR_WH = 247
    CHINESE_EXP_DOOR_DOOR = 245
    # DELIVERY TARIFFS
    EXPRESS_LIGHT_DOOR_DOOR = 1
    SUPER_EXPRESS_18 = 3
    ECONOM_EXPRESS_WH_WH = 5
    EXPRESS_LIGHT_WH_WH = 10
    EXPRESS_LIGHT_WH_DOOR = 11
    EXPRESS_LIGHT_DOOR_WH = 12
    EXPRESS_HIGHLOAD_WH_WH = 15
    EXPRESS_HIGHLOAD_WH_DOOR = 16
    EXPRESS_HIGHLOAD_DOOR_WH = 17
    EXPRESS_HIGHTLOAD_DOOR_DOOR = 18
    SUPER_EXPRESS_9 = 57
    SUPER_EXPRESS_10 = 58
    SUPER_EXPRESS_12 = 59
    SUPER_EXPRESS_14 = 60
    SUPER_EXPRESS_16 = 61
    HIGHWAY_EXPRESS_WH_WH = 62
    HIGHWAY_SUPER_EXPRESS_WH_WH = 63
    ECONOM_EXPRESS_DOOR_DOOR = 118
    ECONOM_EXPRESS_WH_DOOR = 119
    ECONOM_EXPRESS_DOOR_WH = 120
    HIGHWAY_EXPRESS_DOOR_DOOR = 121
    HIGHWAY_EXPRESS_WH_DOOR = 122
    HIGHWAY_EXPRESS_DOOR_WH = 123
    HIGHWAY_SUPER_EXPRESS_DOOR_DOOR = 124
    HIGHWAY_SUPER_EXPRESS_WH_DOOR = 125
    HIGHWAY_SUPER_EXPRESS_DOOW_WH = 126
    EXPRESS_LIGHT_DOOR_POST = 361
    EXPRESS_LIGHT_WH_PSOT = 363
    EXPRESS_DOOR_DOOR = 480
    EXPRESS_DOOR_WH = 481
    EXPRESS_WH_DOOR = 482
    EXPRESS_WH_WH = 483
    EXPRESS_DOOR_POST = 485
    EXPRESS_WH_POST = 486


class MaterialCode(IntEnum):
    POLYESTER = 1
    NYLON = 2
    FLEECE = 3
    COTTON = 4
    TEXTILE = 5
    LINEN = 6
    VISCOSE = 7
    SILK = 8
    WOOL = 9
    CASHMERE = 10
    SKIN = 11
    LEATHERETTE = 12
    FAUX = 13
    SUEDE = 14
    POLYURETHANE = 15
    SPANDEX = 16
    RUBBER = 17


class ServiceCode(Enum):
    INSURANCE = auto()
    TAKE_SENDER = auto()
    DELIV_RECEIVER = auto()
    TRYING_ON = auto()
    PART_DELIV = auto()
    REVERSE = auto()
    DANGER_CARGO = auto()
    SMS = auto()
    THERMAL_MODE = auto()
    COURIER_PACKAGE_A2 = auto()
    SECURE_PACKAGE_A2 = auto()
    SECURE_PACKAGE_A3 = auto()
    SECURE_PACKAGE_A4 = auto()
    SECURE_PACKAGE_A5 = auto()
    NOTIFY_ORDER_CREATED = auto()
    NOTIFY_ORDER_DELIVERY = auto()
    CARTON_BOX_XS = auto()
    CARTON_BOX_S = auto()
    CARTON_BOX_M = auto()
    CARTON_BOX_L = auto()
    CARTON_BOX_500GR = auto()
    CARTON_BOX_1KG = auto()
    CARTON_BOX_2KG = auto()
    CARTON_BOX_3KG = auto()
    CARTON_BOX_5KG = auto()
    CARTON_BOX_10KG = auto()
    CARTON_BOX_15KG = auto()
    CARTON_BOX_20KG = auto()
    CARTON_BOX_30KG = auto()
    BUBBLE_WRAP = auto()
    WASTE_PAPER = auto()
    CARTON_FILLER = auto()
    BAN_ATTACHMENT_INSPECTION = auto()
    PHOTO_DOCUMENT = auto()


class OrderManipulationRequestType(str, Enum):
    CREATE: str = "CREATE"
    UPDATE: str = "UPDATE"
    DELETE: str = "DELETE"
    AUTH: str = "AUTH"
    GET: str = "GET"


class OrderManipulationRequestState(str, Enum):
    ACCEPTED: str = "ACCEPTED"
    WAITING: str = "WAITING"
    SUCCESSFUL: str = "SUCCESSFUL"
    INVALID: str = "INVALID"


class PrintForm(str, Enum):
    BARCODE: str = "barcode"
    WAYBILL: str = "waybill"


class Money(BaseModel):
    """
    :param value: Сумма в валюте

    :param value_sum: Сумма НДС

    :param value_rate: Ставка НДС (значение - 0, 10, 20 и т.п. , null - нет НДС)

    """

    value: float
    value_sum: Optional[float]
    value_rate: Optional[int]


class Threshold(BaseModel):
    """
    :param threshold: Порог стоимости товара (действует по условию меньше или равно)
        в целых единицах валюты

    :param sum: Доп. сбор за доставку товаров, общая стоимость которых попадает в интервал

    :param vat_sum: Сумма НДС, включённая в доп. сбор за доставку

    :param vat_rate: Ставка НДС (значение - 0, 10, 20 и т.п. , null - нет НДС)

    """

    threshold: int
    sum: float
    vat_sum: Optional[float]
    vat_rate: Optional[int]


class Item(BaseModel):
    """
    :param name: Наименование товара (может также содержать описание товара: размер, цвет)

    :param ware_key: Идентификатор/артикул товара

    :param payment: Оплата за товар при получении
        (за единицу товара в указанной валюте, значение >=0) — наложенный платеж,
        в случае предоплаты значение = 0

    :param cost: Объявленная стоимость товара
        (за единицу товара в указанной валюте, значение >=0).
        С данного значения рассчитывается страховка

    :param weight: Вес (за единицу товара, в граммах)

    :param weight_gross: Вес брутто

    :param amount: Количество единиц товара (в штуках)

    :param name_i18n: Наименование на иностранном языке

    :param brand: Бренд на иностранном языке

    :param country_code: Код страны в формате  ISO_3166-1_alpha-2

    :param material: Код материала

    :param wifi_gsm: Содержит wifi/gsm

    :param url: Ссылка на сайт интернет-магазина с описанием товара

    """

    name: constr(max_length=255)
    ware_key: constr(max_length=20)
    payment: Money
    cost: float
    weight: int
    weight_gross: Optional[int]
    amount: int
    name_i18n: Optional[constr(max_length=255)]
    brand: Optional[constr(max_length=255)]
    country_code: Optional[constr(min_length=2, max_length=2)]
    material: Optional[MaterialCode]
    wifi_gsm: Optional[bool]
    url: constr(max_length=255)


class Phone(BaseModel):
    """
    :param number: Номер телефона

    :param additional: Дополнительная информация (доп. номер)

    """

    number: constr(max_length=255)
    additional: Optional[constr(max_length=255)]


class Image(BaseModel):
    """
    :param url: Ссылка на фото
        <OfficeImage url="http://dfdfdf/images/22/47_1_SUR2"/>

    :param number: Номер фото

    """

    url: constr(max_length=255)
    number: int


class Service(BaseModel):
    """
    :param code: Код дополнительной услуги

    :param parameter: Параметр дополнительной услуги

    """

    code: ServiceCode
    parameter: Optional[str]


class Error(BaseModel):
    """
    :param code: Код ошибки
    :param message: Описание ошибки
    """

    code: str
    message: str


class Warning(BaseModel):
    """
    :param code: Код предупреждения
    :param message: Описание предупреждения
    """

    code: str
    message: str


class AccessToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    scope: str
    jti: str
    created_at: Optional[datetime]

    @validator("token_type")
    def check_token_type(cls, v):
        if v == "bearer":
            return v
        raise ValueError("Invalid token type")

    @validator("created_at", always=True)
    def set_created_at(cls, v):
        if v:
            return v
        return datetime.now()

    def is_valid(self):
        return datetime.now() < self.created_at + timedelta(seconds=self.expires_in)


class ClientCredentials(BaseModel):
    grant_type: str = "client_credentials"
    client_id: str
    client_secret: str


class Headers(BaseModel):
    Authorization: str
    ContentType: str = Field("application/json", alias="Content-type")

    @validator("Authorization")
    def validate_auth(cls, v):
        return f"Bearer {v}"


class Location(BaseModel):
    """
    :param code: Код локации (справочник СДЭК)
    """

    code: int


class City(Location):
    """
    :param city: Название населенного пункта.

    :param fias_guid: Уникальный идентификатор ФИАС населенного пункта

    :param country_code:
        Код страны населенного пункта в формате ISO_3166-1_alpha-2

    :param country: Название страны населенного пункта

    :param region: Название региона населенного пункта

    :param region_code: Код региона СДЭК

    :param fias_region_guid:
        Уникальный идентификатор ФИАС региона населенного пункта

    :param sub_region: Название района региона населенного пункта

    :param postal_codes: Массив почтовых индексов

    :param longitude: Долгота центра населенного пункта

    :param latitude: Широта центра населенного пункта

    :param time_zone: Часовой пояс населенного пункта

    :param payment_limit:
        Ограничение на сумму наложенного платежа в населенном пункте

    :param errors: Список ошибок

    """

    city: str
    fias_guid: Optional[UUID]
    country_code: str
    country: str
    region: Optional[str]
    region_code: Optional[int]
    fias_region_guid: Optional[UUID]
    sub_region: Optional[str]
    postal_codes: Optional[list]
    longitude: Optional[float]
    latitude: Optional[float]
    time_zone: Optional[str]
    payment_limit: Optional[float]
    errors: Optional[list[Error]]


class CitySearchRequest(BaseModel):
    """
    :param country_codes: Массив кодов стран в формате  ISO_3166-1_alpha-2

    :param region_code: Код региона СДЭК

    :param fias_region_guid: Уникальный идентификатор ФИАС региона

    :param fias_guid: Уникальный идентификатор ФИАС населенного пункта

    :param postal_code: Почтовый индекс

    :param code: Код населенного пункта СДЭК

    :param city: Название населенного пункта. Должно соответствовать полностью

    :param page: Номер страницы выборки результата. По умолчанию 0

    :param size: Ограничение выборки результата. По умолчанию 1000

    :param lang: Локализация. По умолчанию "rus"

    :param payment_limit: Ограничение на сумму наложенного платежа:
        -1 - ограничения нет;
        0 - наложенный платеж не принимается;
        положительное значение - сумма наложенного платежа не более данного значения.
    """

    country_codes: Optional[list[constr(min_length=2, max_length=2)]]
    region_code: Optional[int]
    fias_region_guid: Optional[UUID]
    fias_guid: Optional[UUID]
    postal_code: Optional[constr(max_length=255)]
    code: Optional[int]
    city: Optional[constr(max_length=255)]
    page: Optional[int]
    size: Optional[int]
    lang: Optional[Language]
    payment_limit: Optional[float]

    @validator("size", always=True)
    def validate_size(cls, v, values):
        if values.get("page") and not v:
            raise ValueError("You have to give size a value if you give value to page")
        return v


class Contact(BaseModel):
    """
    :param company: Наименование компании

    :param name: Ф.И.О контактного лица

    :param email: Эл. адрес

    :param phones: Список телефонов

    :param passport_series: Серия паспорта

    :param passport_number: Номер паспорта

    :param passport_date_of_issue: Дата выдачи паспорта

    :param passport_organization: Орган выдачи паспорта

    :param passport_date_of_birth: Дата рождения

    :param tin: ИНН

    :param passport_requirements_satisfied:
        Требования по паспортным данным удовлетворены
        (актуально для международных заказов):
        true - паспортные данные собраны или не требуются
        false - паспортные данные требуются и не собраны

    """

    company: Optional[constr(max_length=255)]
    name: constr(max_length=255)
    email: Optional[constr(max_length=255)]
    phones: list[Phone]
    passport_series: Optional[constr(max_length=255)]
    passport_number: Optional[constr(max_length=255)]
    passport_date_of_issue: Optional[date]
    passport_organization: Optional[constr(max_length=255)]
    passport_date_of_birth: Optional[date]
    tin: Optional[constr(max_length=255)]
    passport_requirements_satisfied: bool

    @validator("passport_requirements_satisfied", always=True)
    def validate_passport(cls, v, values):
        passport_series = values.get("passport_series")
        passport_number = values.get("passport_number")
        passport_date_of_issue = values.get("passport_date_of_issue")
        passport_organization = values.get("passport_organization")
        passport_date_of_birth = values.get("passport_date_of_birth")
        return (
            True
            if (
                passport_series
                and passport_number
                and passport_date_of_issue
                and passport_organization
                and passport_date_of_birth
            )
            else False
        )


class Seller(BaseModel):
    """
    :param name: Наименование истинного продавца

    :param inn: ИНН истинного продавца

    :param phone: Телефон истинного продавца

    :param ownership_form: Код формы собственности

    :param address: Адрес истинного продавца.
        Используется при печати инвойсов для отображения адреса
        настоящего продавца товара, либо торгового названия

    """

    name: Optional[constr(max_length=255)]
    inn: Optional[constr(max_length=20)]
    phone: Optional[constr(max_length=255)]
    ownership_form: Optional[OwnershipForm]
    address: Optional[constr(max_length=255)]


class Package(BaseModel):
    """
    :param number: Номер упаковки
        (можно использовать порядковый номер упаковки заказа или номер заказа),
        уникален в пределах заказа. Идентификатор заказа в ИС Клиента

    :param weight: Общий вес (в граммах)

    :param length: Габариты упаковки. Длина (в сантиметрах)

    :param width: Габариты упаковки. Ширина (в сантиметрах)

    :param height: Габариты упаковки. Высота (в сантиметрах)

    :param comment: Комментарий к упаковке

    :param items: Позиции товаров в упаковке

    """

    number: Optional[constr(max_length=255)]
    weight: int
    length: Optional[int]
    width: Optional[int]
    height: Optional[int]
    comment: Optional[constr(max_length=255)]
    items: Optional[list[Item]]

    @validator("number", always=True)
    def validate_number(cls, v, values):
        if not v:
            return str(uuid.uuid4())
        return v


class TariffListRequest(BaseModel):
    """
    :param date: Дата и время планируемой передачи заказа
        По умолчанию - текущая

    :param type: Тип заказа:
        1 - "интернет-магазин"
        2 - "доставка"
        По умолчанию - 1

    :param currency: Валюта, в которой необходимо произвести расчет.
        По умолчанию - валюта договора

    :param lang: Язык вывода информации о тарифах
        Возможные значения: rus, eng, zho
        По умолчанию - rus

    :param from_location: Адрес отправления

    :param to_location: Адрес получения

    :param packages: Список информации по местам (упаковкам)

    """

    date: Optional[date]
    type: Optional[OrderType]
    currency: Optional[Currency]
    lang: Optional[Language]
    from_location: Location
    to_location: Location
    packages: list[Package]


class Tariff(BaseModel):
    """
    :param tariff_code: Код тарифа

    :param tariff_name: Название тарифа на языке вывода

    :param tariff_description: Описание тарифа на языке вывода

    :param delivery_mode: Режим тарифа

    :param delivery_sum: Стоимость доставки

    :param period_min: Минимальное время доставки (в рабочих днях)

    :param period_max: Максимальное время доставки (в рабочих днях)

    """

    tariff_code: int
    tariff_name: str
    tariff_description: Optional[str]
    delivery_mode: DeliveryMode
    delivery_sum: float
    period_min: int
    period_max: int


class TariffListResponse(BaseModel):
    """
    :param tariff_codes: Доступные тарифы

    :param errors: Список ошибок
    """

    tariffs: Optional[list[Tariff]] = Field(alias="tariff_codes")
    cheapest: Optional[Tariff]
    fastest: Optional[Tariff]
    errors: Optional[list[Error]]

    @validator("cheapest", always=True)
    def get_cheapest(cls, v, values, **kwargs):
        tariffs = values.get("tariffs")
        if tariffs:
            return min(tariffs, key=lambda item: item.delivery_sum)
        return None

    @validator("fastest", always=True)
    def get_fastest(cls, v, values, **kwargs):
        tariffs = values.get("tariffs")
        if tariffs:
            return min(
                tariffs, key=lambda item: (item.period_min + item.period_max) / 2
            )
        return None


class OfficeListRequest(BaseModel):
    """
    :param postal_code: Почтовый индекс города, для которого необходим список офисов

    :param city_code: Код города по базе СДЭК

    :param type: Тип офиса, может принимать значения:
        «PVZ» - для отображения только складов СДЭК;
        «POSTAMAT» - для отображения постаматов СДЭК;
        «ALL» - для отображения всех ПВЗ независимо от их типа.

        При отсутствии параметра принимается значение по умолчанию «ALL»

    :param country_code: Код страны в формате ISO_3166-1_alpha-2
        (см. “Общероссийский классификатор стран мира”)

    :param region_code: Код региона по базе СДЭК

    :param have_cashless: Наличие терминала оплаты, может принимать значения:
        «1», «true» - есть;
        «0», «false» - нет.

    :param have_cash: Есть прием наличных, может принимать значения:
        «1», «true» - есть;
        «0», «false» - нет.

    :param allowed_cod: Разрешен наложенный платеж, может принимать значения:
        «1», «true» - да;
        «0», «false» - нет.

    :param is_dressing_room: Наличие примерочной, может принимать значения:
        «1», «true» - есть;
        «0», «false» - нет.

    :param weight_max: Максимальный вес в кг, который может принять офис
        (значения больше 0 - передаются офисы, которые принимают этот вес;
        0 - офисы с нулевым весом не передаются; значение не указано - все офисы)

    :param weight_min: Минимальный вес в кг, который принимает офис
        (при переданном значении будут выводиться офисы с минимальным
        весом до указанного значения)

    :param lang: Локализация офиса. По умолчанию "rus".

    :param take_only: Является ли офис только пунктом выдачи,
        может принимать значения:
        «1», «true» - да;
        «0», «false» - нет.

    :param is_handout: Является пунктом выдачи, может принимать значения:
        «1», «true» - да;
        «0», «false» - нет.

    """

    postal_code: Optional[int]
    city_code: Optional[int]
    type: Optional[OfficeType]
    country_code: Optional[constr(min_length=2, max_length=2)]
    region_code: Optional[int]
    have_cashless: Optional[bool]
    have_cash: Optional[bool]
    allowed_cod: Optional[bool]
    is_dressing_room: Optional[bool]
    weight_max: Optional[int]
    weight_min: Optional[int]
    lang: Optional[Language]
    take_only: Optional[bool]
    is_handout: Optional[bool]


class WorkTime(BaseModel):
    """
    :param day: Порядковый номер дня начиная с единицы.
        Понедельник = 1, воскресенье = 7.

    :param time: Период работы в эти дни.
        Если в этот день не работают, то не отображается.

    """

    day: WeekDay
    time: constr(max_length=20)


class WorkTimeException(BaseModel):
    """
    :param date: Дата

    :param time: Период работы в указанную дату. Если в этот день не работают, то не отображается.

    :param is_working: Признак рабочего/нерабочего дня в указанную дату

    """

    date: date
    time: Optional[constr(max_length=20)]
    is_working: bool


class PostamatCell(BaseModel):
    """
    :param width: Ширина (см)

    :param height: Высота (см)

    :param depth: Глубина (см)

    """

    width: float
    height: float
    depth: float


class Office(BaseModel):
    """
    :param code: Код

    :param name: Название

    :param location: Адрес офиса

    :param address_comment: Описание местоположения

    :param nearest_station: Ближайшая станция/остановка транспорта

    :param nearest_metro_station: Ближайшая станция метро

    :param work_time: Режим работы, строка вида «пн-пт 9-18, сб 9-16»

    :param phones: Список телефонов

    :param email: Адрес электронной почты

    :param note: Примечание по офису

    :param type: Тип ПВЗ: PVZ — склад СДЭК, POSTAMAT — постамат СДЭК

    :param owner_сode: Принадлежность офиса компании:
        cdek — офис принадлежит компании СДЭК
        InPost — офис принадлежит компании InPost

    :param take_only: Является ли офис только пунктом выдачи
        или также осуществляет приём грузов

    :param is_handout: Является пунктом выдачи

    :param is_dressing_room: Есть ли примерочная

    :param have_cashless: Есть безналичный расчет

    :param have_cash: Есть приём наличных

    :param allowed_cod: Разрешен наложенный платеж в ПВЗ

    :param site: Ссылка на данный офис на сайте СДЭК

    :param office_image_list: Все фото офиса (кроме фото как доехать).

    :param work_time_list: График работы на неделю.
        Вложенный тег с атрибутами day и periods.

    :param work_time_exceptions: Исключения в графике работы офиса

    :param weight_min: Минимальный вес (в кг.), принимаемый в ПВЗ (> WeightMin)

    :param weight_max: Максимальный вес (в кг.), принимаемый в ПВЗ (<=WeightMax)

    :param fulfillment: Наличие зоны фулфилмента

    :param dimensions: Перечень максимальных размеров ячеек
        (только для type = POSTAMAT)

    :param errors: Список ошибок

    """

    code: constr(max_length=10)
    name: constr(max_length=50)
    location: City
    address_comment: Optional[constr(max_length=255)]
    nearest_station: Optional[constr(max_length=50)]
    nearest_metro_station: Optional[constr(max_length=50)]
    work_time: constr(max_length=100)
    phones: list[Phone]
    email: constr(max_length=255)
    note: Optional[constr(max_length=255)]
    type: OfficeType
    owner_сode: OfficeOwner
    take_only: bool
    is_handout: bool
    is_dressing_room: bool
    have_cashless: bool
    have_cash: bool
    allowed_cod: bool
    site: Optional[constr(max_length=255)]
    office_image_list: Optional[list[Image]]
    work_time_list: list[WorkTime]
    work_time_exceptions: list[WorkTimeException]
    weight_min: Optional[float]
    weight_max: Optional[float]
    fulfillment: bool
    dimensions: Optional[list[PostamatCell]]
    errors: Optional[list[Error]]

    @validator("dimensions")
    def validate_dims(cls, v, values):
        office_type = values.get("type")
        if office_type != OfficeType.POSTAMAT:
            raise ValueError("You only supply dimentions for POSTAMAT Office")
        return v


class OrderCreationRequest(BaseModel):
    """
    :param type: Тип заказа:
        1 - "интернет-магазин" (только для договора типа "Договор с ИМ")
        2 - "доставка" (для любого договора)

        По умолчанию - 1

    :param number: Номер заказа в ИС Клиента
        (если не передан, будет присвоен номер заказа в ИС СДЭК - uuid)
        Только для заказов "интернет-магазин"

    :param tariff_code: Код тарифа

    :param comment: Комментарий к заказу

    :param developer_key: Ключ разработчика

    :param shipment_point: Код ПВЗ СДЭК, на который будет производиться
        забор отправления, либо самостоятельный привоз клиентом

    :param delivery_point: Код ПВЗ СДЭК, на который будет доставлена посылка

    :param date_invoice: Дата инвойса
        Только для заказов "интернет-магазин"

    :param shipper_name: Грузоотправитель
        Только для заказов "интернет-магазин"

    :param shipper_address: Адрес грузоотправителя
        Только для заказов "интернет-магазин"

    :param delivery_recipient_cost: Доп. сбор за доставку, которую ИМ
        берет с получателя.
        Только для заказов "интернет-магазин"

    :param delivery_recipient_cost_adv: Доп. сбор за доставку (которую
        ИМ берет с получателя) в зависимости от суммы заказа
        Только для заказов "интернет-магазин"

    :param sender: Отправитель

    :param seller: Реквизиты истинного продавца
        Только для заказов "интернет-магазин"

    :param recipient: Получатель

    :param from_location: Адрес отправления

    :param to_location: Адрес получения

    :param services: Дополнительные услуги

    :param packages: Список информации по местам (упаковкам)

    :param print: Необходимость сформировать печатную форму по заказу
        Может принимать значения:
        barcode - ШК мест (число копий - 1)
        waybill - квитанция (число копий - 2)

    """

    type: Optional[OrderType]
    number: Optional[constr(max_length=32)]
    tariff: Tariff | int
    comment: Optional[constr(max_length=255)]
    developer_key: Optional[str]
    shipment_point: Optional[Office | constr(max_length=255)]
    delivery_point: Optional[Office | constr(max_length=255)]
    date_invoice: Optional[date]
    shipper_name: Optional[constr(max_length=255)]
    shipper_address: Optional[constr(max_length=255)]
    delivery_recipient_cost: Optional[Money]
    delivery_recipient_cost_adv: Optional[list[Threshold]]
    sender: Optional[Contact]
    seller: Optional[Seller]
    recipient: Optional[Contact]
    from_location: Optional[Location]
    to_location: Optional[Location]
    services: Optional[list[Service]]
    packages: conlist(item_type=Package, max_items=255)
    print: Optional[PrintForm]

    @validator("type", always=True)
    def validate_type(cls, v, values):
        if not v:
            return OrderType.ECOMMERCE
        return v

    @validator("number")
    def validate_number(cls, v, values):
        order_type = values.get("type", OrderType.ECOMMERCE)
        if order_type != OrderType.ECOMMERCE:
            raise ValueError(
                "You only supply order number for orders of type ECOMMERCE"
            )
        return v

    @validator("tariff")
    def validate_tariff(cls, v, values):
        if isinstance(v, Tariff):
            return v.tariff_code
        return v

    @validator("shipment_point", always=True)
    def validate_shipment_point(cls, v, values):
        tariff = values.get("tariff")
        if not tariff:
            raise ValueError("You must provide tariff")
        else:
            if (
                not isinstance(tariff, int)
                and tariff.delivery_mode
                in (
                    DeliveryMode.WAREHOUSE_DOOR,
                    DeliveryMode.WAREHOUSE_WAREHOUSE,
                    DeliveryMode.WAREHOUSE_POSTMATE,
                )
                and not v
            ):
                raise ValueError("You must provide shipping point for this Tariff")
            if isinstance(v, Office):
                return v.code
            return v

    @validator("delivery_point")
    def validate_delivery_point(cls, v, values):
        if isinstance(v, Office):
            return v.code
        return v

    @validator("date_invoice", "shipper_name", "shipper_address", "seller", always=True)
    def validate_date_invoice(cls, v, values, **kwargs):
        field = kwargs.get("field")
        tariff = values.get("tariff")
        if isinstance(tariff, Tariff):
            if tariff_is_international(tariff) and v:
                return v
            else:
                raise ValueError(
                    f"You have to provide {field.name} in case of international order"
                )

        order_type = values.get("type", OrderType.ECOMMERCE)
        if order_type != OrderType.ECOMMERCE:
            raise ValueError(
                f"You only supply {field.name} for orders of type ECOMMERCE"
            )
        return v

    @validator("sender", always=True)
    def validate_sender(cls, v, values):
        order_type = values.get("type", OrderType.ECOMMERCE)
        if order_type == OrderType.DELIVERY and not v:
            raise ValueError(f"You have to supply sender for orders of type DELIVERY")
        return v

    @validator("from_location", always=True)
    def validate_from(cls, v, values):
        tariff = values.get("tariff")
        if (
            isinstance(tariff, Tariff)
            and tariff.delivery_mode
            in (
                DeliveryMode.DOOR_DOOR,
                DeliveryMode.DOOR_WAREHOUSE,
                DeliveryMode.DOOR_POSTMATE,
            )
            and not v
        ):
            raise ValueError(
                "You have to supply from location if shipping from address"
            )
        return v

    @validator("to_location", always=True)
    def validate_to(cls, v, values):
        tariff = values.get("tariff")
        if (
            isinstance(tariff, Tariff)
            and tariff.delivery_mode
            in (DeliveryMode.DOOR_DOOR, DeliveryMode.WAREHOUSE_DOOR)
            and not v
        ):
            raise ValueError("You have to supply to location if shipping to address")
        return v


class Entity(BaseModel):
    """
    :param uuid: Идентификатор заказа в ИС СДЭК
    :param type: Тип связанной сущности
        Может принимать значения:
        waybill - квитанция к заказу
        barcode - ШК места к заказу
    """

    uuid: UUID
    type: Optional[PrintForm]


class OrderManipulationRequest(BaseModel):
    """
    :param request_uuid: Идентификатор запроса в ИС СДЭК

    :param type: Тип запроса
        Может принимать значения: CREATE, UPDATE, DELETE, AUTH, GET

    :param date_time: Дата и время установки текущего состояния запроса
        (формат yyyy-MM-dd'T'HH:mm:ssZ)

    :param state: Текущее состояние запроса
        Может принимать значения:

        ACCEPTED - пройдена предварительная валидация и запрос принят
        WAITING - запрос ожидает обработки (зависит от выполнения другого запроса)
        SUCCESSFUL - запрос обработан успешно
        INVALID - запрос обработался с ошибкой

    :param errors: Ошибки, возникшие в ходе выполнения запроса

    :param warnings: Предупреждения, возникшие в ходе выполнения запроса

    """

    request_uuid: Optional[UUID]
    type: OrderManipulationRequestType
    date_time: datetime
    state: OrderManipulationRequestState
    errors: Optional[list[Error]]
    warnings: Optional[list[Warning]]


class OrderCreationResponse(BaseModel):
    """
    :param entity: Информация о заказе
    :param requests: Информация о запросе над заказом
    :param related_entities: Связанные сущности (если в запросе был передан корректный print)
    """

    entity: Optional[Entity]
    requests: list[OrderManipulationRequest]
    related_entities: Optional[Entity]


def tariff_is_international(tariff: Tariff) -> bool:
    return tariff.code in (
        TariffCode.INTERNATIONAL_DOCS,
        TariffCode.INTERNATIONAL_CARGO,
        TariffCode.CHINESE_EXP_WH_DOOR,
        TariffCode.CHINESE_EXP_WH_WH,
        TariffCode.CHINESE_EXP_DOOR_WH,
        TariffCode.CHINESE_EXP_DOOR_DOOR,
        TariffCode.EXPRESS_DOOR_DOOR,
        TariffCode.EXPRESS_DOOR_WH,
        TariffCode.EXPRESS_WH_DOOR,
        TariffCode.EXPRESS_WH_WH,
        TariffCode.EXPRESS_DOOR_POST,
        TariffCode.EXPRESS_WH_POST,
    )
