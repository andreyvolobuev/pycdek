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


class ProblemCode(IntEnum):
    WRONG_PHONE = 1
    PACKAGE_NOT_READY = 9
    DENIED_TO_PAY = 11
    NO_CONTACT = 13
    ORGANIZATION_UNAVAILABLE = 17
    ADDRESS_CHANGED = 19
    LATE = 35
    SELF_PICK_UP = 36
    POST_OVERFILL = 37
    POST_OUT_OF_SERVICE = 38
    PACKAGE_WONT_FIT = 39
    DENY_TO_ACCEPT = 40
    ORDER_CANCEL = 41
    ENTRY_PASS_NEEDED = 42
    PASS_NEEDS_PAYMENT = 43
    CLOSED_PROPERTY = 44
    NO_ID = 45
    CITY_CHANGE = 46
    NO_ADDRESS = 47
    DELIVERY_TO_POST = 48
    DANGEROUS_CARGO = 49
    DENY_ADDRESS = 52
    INTERVAL_CHANGED = 53
    POST_APP_OUT_OF_SERVICE = 54
    PACKAGE_NOT_FOUND = 55
    PASS_TO_PVZ = 56
    CANT_DELIVER_TO_PVZ = 57


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
    ECONOM_WH_WH = 234
    ECONOM_WH_DOOR = 233
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


class ServiceCode(str, Enum):
    INSURANCE: str = "INSURANCE"
    TAKE_SENDER: str = "TAKE_SENDER"
    DELIV_RECEIVER: str = "DELIV_RECEIVER"
    TRYING_ON: str = "TRYING_ON"
    PART_DELIV: str = "PART_DELIV"
    REVERSE: str = "REVERSE"
    DANGER_CARGO: str = "DANGER_CARGO"
    SMS: str = "SMS"
    THERMAL_MODE: str = "THERMAL_MODE"
    COURIER_PACKAGE_A2: str = "COURIER_PACKAGE_A2"
    SECURE_PACKAGE_A2: str = "SECURE_PACKAGE_A2"
    SECURE_PACKAGE_A3: str = "SECURE_PACKAGE_A3"
    SECURE_PACKAGE_A4: str = "SECURE_PACKAGE_A4"
    SECURE_PACKAGE_A5: str = "SECURE_PACKAGE_A5"
    NOTIFY_ORDER_CREATED: str = "NOTIFY_ORDER_CREATED"
    NOTIFY_ORDER_DELIVERY: str = "NOTIFY_ORDER_DELIVERY"
    CARTON_BOX_XS: str = "CARTON_BOX_XS"
    CARTON_BOX_S: str = "CARTON_BOX_S"
    CARTON_BOX_M: str = "CARTON_BOX_M"
    CARTON_BOX_L: str = "CARTON_BOX_L"
    CARTON_BOX_500GR: str = "CARTON_BOX_500GR"
    CARTON_BOX_1KG: str = "CARTON_BOX_1KG"
    CARTON_BOX_2KG: str = "CARTON_BOX_2KG"
    CARTON_BOX_3KG: str = "CARTON_BOX_3KG"
    CARTON_BOX_5KG: str = "CARTON_BOX_5KG"
    CARTON_BOX_10KG: str = "CARTON_BOX_10KG"
    CARTON_BOX_15KG: str = "CARTON_BOX_15KG"
    CARTON_BOX_20KG: str = "CARTON_BOX_20KG"
    CARTON_BOX_30KG: str = "CARTON_BOX_30KG"
    BUBBLE_WRAP: str = "BUBBLE_WRAP"
    WASTE_PAPER: str = "WASTE_PAPER"
    CARTON_FILLER: str = "CARTON_FILLER"
    BAN_ATTACHMENT_INSPECTION: str = "BAN_ATTACHMENT_INSPECTION"
    PHOTO_DOCUMENT: str = "PHOTO_DOCUMENT"


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
    value: Сумма в валюте

    value_sum: Сумма НДС

    value_rate: Ставка НДС (значение - 0, 10, 20 и т.п. , null - нет НДС)

    """

    value: float
    value_sum: Optional[float]
    value_rate: Optional[int]


class Threshold(BaseModel):
    """
    threshold: Порог стоимости товара (действует по условию меньше или равно)
        в целых единицах валюты

    sum: Доп. сбор за доставку товаров, общая стоимость которых попадает в интервал

    vat_sum: Сумма НДС, включённая в доп. сбор за доставку

    vat_rate: Ставка НДС (значение - 0, 10, 20 и т.п. , null - нет НДС)

    """

    threshold: int
    sum: float
    vat_sum: Optional[float]
    vat_rate: Optional[int]


class Item(BaseModel):
    """
    name: Наименование товара (может также содержать описание товара: размер, цвет)

    ware_key: Идентификатор/артикул товара

    payment: Оплата за товар при получении
        (за единицу товара в указанной валюте, значение >=0) — наложенный платеж,
        в случае предоплаты значение = 0

    cost: Объявленная стоимость товара
        (за единицу товара в указанной валюте, значение >=0).
        С данного значения рассчитывается страховка

    weight: Вес (за единицу товара, в граммах)

    weight_gross: Вес брутто

    amount: Количество единиц товара (в штуках)

    name_i18n: Наименование на иностранном языке

    brand: Бренд на иностранном языке

    country_code: Код страны в формате  ISO_3166-1_alpha-2

    material: Код материала

    wifi_gsm: Содержит wifi/gsm

    url: Ссылка на сайт интернет-магазина с описанием товара

    """

    name: constr(max_length=255)
    ware_key: Optional[constr(max_length=20)]
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
    url: Optional[constr(max_length=255)]

    @validator("ware_key", always=True)
    def validate_number(cls, v, values):
        if not v:
            return uuid.uuid4().hex[:20]
        return v


class Phone(BaseModel):
    """
    number: Номер телефона

    additional: Дополнительная информация (доп. номер)

    """

    number: constr(max_length=255)
    additional: Optional[constr(max_length=255)]


class Image(BaseModel):
    """
    url: Ссылка на фото
        <OfficeImage url="http://dfdfdf/images/22/47_1_SUR2"/>

    number: Номер фото

    """

    url: constr(max_length=255)
    number: Optional[int]


class Service(BaseModel):
    """
    code: Код дополнительной услуги

    parameter: Параметр дополнительной услуги

    """

    code: ServiceCode
    parameter: Optional[str]


class Problem(BaseModel):
    """
    code: Код проблемы
    create_date: Дата создания проблемы
    """
    code: Optional[ProblemCode]
    create_date: Optional[datetime]


class Error(BaseModel):
    """
    code: Код ошибки
    message: Описание ошибки
    """

    code: str
    message: str


class Warning(BaseModel):
    """
    code: Код предупреждения
    message: Описание предупреждения
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
    code: Код населенного пункта СДЭК
    fias_guid: Уникальный идентификатор ФИАС
    postal_code: Почтовый индекс
    longitude: Долгота
    latitude: Широта
    country_code: Код страны в формате  ISO_3166-1_alpha-2
    region: Название региона
    sub_region: Название района региона
    city: Название города
    kladr_code: Код КЛАДР
    address: Строка адреса
    """

    city_code: Optional[int]
    fias_guid: Optional[UUID]
    postal_code: Optional[constr(max_length=255)]
    longitude: Optional[float]
    latitude: Optional[float]
    country_code: Optional[constr(min_length=2, max_length=2)]
    region: Optional[constr(max_length=255)]
    sub_region: Optional[constr(max_length=255)]
    city: Optional[constr(max_length=255)]
    kladr_code: Optional[constr(max_length=255)]
    address: constr(max_length=255)


class Status(BaseModel):
    """
    code: Код статуса
    name: Название статуса
    date_time: Дата и время установки статуса (формат yyyy-MM-dd'T'HH:mm:ssZ)
    reason_code: Дополнительный код статуса
    city: Наименование места возникновения статуса
    """

    code: constr(max_length=255)
    name: constr(max_length=255)
    date_time: datetime
    reason_code: Optional[constr(min_length=2, max_length=2)]
    city: Optional[constr(max_length=255)]


class City(BaseModel):
    """
    city: Название населенного пункта.

    fias_guid: Уникальный идентификатор ФИАС населенного пункта

    country_code:
        Код страны населенного пункта в формате ISO_3166-1_alpha-2

    country: Название страны населенного пункта

    region: Название региона населенного пункта

    region_code: Код региона СДЭК

    fias_region_guid:
        Уникальный идентификатор ФИАС региона населенного пункта

    sub_region: Название района региона населенного пункта

    postal_codes: Массив почтовых индексов

    longitude: Долгота центра населенного пункта

    latitude: Широта центра населенного пункта

    time_zone: Часовой пояс населенного пункта

    payment_limit:
        Ограничение на сумму наложенного платежа в населенном пункте

    errors: Список ошибок

    """
    code: str
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
    country_codes: Массив кодов стран в формате  ISO_3166-1_alpha-2

    region_code: Код региона СДЭК

    fias_region_guid: Уникальный идентификатор ФИАС региона

    fias_guid: Уникальный идентификатор ФИАС населенного пункта

    postal_code: Почтовый индекс

    code: Код населенного пункта СДЭК

    city: Название населенного пункта. Должно соответствовать полностью

    page: Номер страницы выборки результата. По умолчанию 0

    size: Ограничение выборки результата. По умолчанию 1000

    lang: Локализация. По умолчанию "rus"

    payment_limit: Ограничение на сумму наложенного платежа:
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
    company: Наименование компании

    name: Ф.И.О контактного лица

    email: Эл. адрес

    phones: Список телефонов

    passport_series: Серия паспорта

    passport_number: Номер паспорта

    passport_date_of_issue: Дата выдачи паспорта

    passport_organization: Орган выдачи паспорта

    passport_date_of_birth: Дата рождения

    tin: ИНН

    passport_requirements_satisfied:
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
    passport_requirements_satisfied: Optional[bool]

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
    name: Наименование истинного продавца

    inn: ИНН истинного продавца

    phone: Телефон истинного продавца

    ownership_form: Код формы собственности

    address: Адрес истинного продавца.
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
    number: Номер упаковки
        (можно использовать порядковый номер упаковки заказа или номер заказа),
        уникален в пределах заказа. Идентификатор заказа в ИС Клиента

    weight: Общий вес (в граммах)

    length: Габариты упаковки. Длина (в сантиметрах)

    width: Габариты упаковки. Ширина (в сантиметрах)

    height: Габариты упаковки. Высота (в сантиметрах)

    comment: Комментарий к упаковке

    items: Позиции товаров в упаковке

    """

    number: Optional[constr(max_length=30)]
    weight: int
    length: Optional[int]
    width: Optional[int]
    height: Optional[int]
    comment: Optional[constr(max_length=255)]
    items: Optional[list[Item]]

    @validator("number", always=True)
    def validate_number(cls, v, values):
        if not v:
            return uuid.uuid4().hex[:30]
        return v


class TariffListRequest(BaseModel):
    """
    date: Дата и время планируемой передачи заказа
        По умолчанию - текущая

    type: Тип заказа:
        1 - "интернет-магазин"
        2 - "доставка"
        По умолчанию - 1

    currency: Валюта, в которой необходимо произвести расчет.
        По умолчанию - валюта договора

    lang: Язык вывода информации о тарифах
        Возможные значения: rus, eng, zho
        По умолчанию - rus

    from_location: Адрес отправления

    to_location: Адрес получения

    packages: Список информации по местам (упаковкам)

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
    tariff_code: Код тарифа

    tariff_name: Название тарифа на языке вывода

    tariff_description: Описание тарифа на языке вывода

    delivery_mode: Режим тарифа

    delivery_sum: Стоимость доставки

    period_min: Минимальное время доставки (в рабочих днях)

    period_max: Максимальное время доставки (в рабочих днях)

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
    tariff_codes: Доступные тарифы

    errors: Список ошибок
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
    postal_code: Почтовый индекс города, для которого необходим список офисов

    city_code: Код города по базе СДЭК

    type: Тип офиса, может принимать значения:
        «PVZ» - для отображения только складов СДЭК;
        «POSTAMAT» - для отображения постаматов СДЭК;
        «ALL» - для отображения всех ПВЗ независимо от их типа.

        При отсутствии параметра принимается значение по умолчанию «ALL»

    country_code: Код страны в формате ISO_3166-1_alpha-2
        (см. “Общероссийский классификатор стран мира”)

    region_code: Код региона по базе СДЭК

    have_cashless: Наличие терминала оплаты, может принимать значения:
        «1», «true» - есть;
        «0», «false» - нет.

    have_cash: Есть прием наличных, может принимать значения:
        «1», «true» - есть;
        «0», «false» - нет.

    allowed_cod: Разрешен наложенный платеж, может принимать значения:
        «1», «true» - да;
        «0», «false» - нет.

    is_dressing_room: Наличие примерочной, может принимать значения:
        «1», «true» - есть;
        «0», «false» - нет.

    weight_max: Максимальный вес в кг, который может принять офис
        (значения больше 0 - передаются офисы, которые принимают этот вес;
        0 - офисы с нулевым весом не передаются; значение не указано - все офисы)

    weight_min: Минимальный вес в кг, который принимает офис
        (при переданном значении будут выводиться офисы с минимальным
        весом до указанного значения)

    lang: Локализация офиса. По умолчанию "rus".

    take_only: Является ли офис только пунктом выдачи,
        может принимать значения:
        «1», «true» - да;
        «0», «false» - нет.

    is_handout: Является пунктом выдачи, может принимать значения:
        «1», «true» - да;
        «0», «false» - нет.

    """

    postal_code: Optional[int]
    city: Optional[City]
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

    @validator("city_code", always=True)
    def validate_city_code(cls, v, values):
        return values['city'].code


class WorkTime(BaseModel):
    """
    day: Порядковый номер дня начиная с единицы.
        Понедельник = 1, воскресенье = 7.

    time: Период работы в эти дни.
        Если в этот день не работают, то не отображается.

    """

    day: WeekDay
    time: constr(max_length=20)


class WorkTimeException(BaseModel):
    """
    date: Дата

    time: Период работы в указанную дату. Если в этот день не работают, то не отображается.

    is_working: Признак рабочего/нерабочего дня в указанную дату

    """

    date: date
    time: Optional[constr(max_length=20)]
    is_working: bool


class PostamatCell(BaseModel):
    """
    width: Ширина (см)

    height: Высота (см)

    depth: Глубина (см)

    """

    width: float
    height: float
    depth: float


class Office(BaseModel):
    """
    code: Код

    name: Название

    location: Адрес офиса

    address_comment: Описание местоположения

    nearest_station: Ближайшая станция/остановка транспорта

    nearest_metro_station: Ближайшая станция метро

    work_time: Режим работы, строка вида «пн-пт 9-18, сб 9-16»

    phones: Список телефонов

    email: Адрес электронной почты

    note: Примечание по офису

    type: Тип ПВЗ: PVZ — склад СДЭК, POSTAMAT — постамат СДЭК

    owner_сode: Принадлежность офиса компании:
        cdek — офис принадлежит компании СДЭК
        InPost — офис принадлежит компании InPost

    take_only: Является ли офис только пунктом выдачи
        или также осуществляет приём грузов

    is_handout: Является пунктом выдачи

    is_dressing_room: Есть ли примерочная

    have_cashless: Есть безналичный расчет

    have_cash: Есть приём наличных

    allowed_cod: Разрешен наложенный платеж в ПВЗ

    site: Ссылка на данный офис на сайте СДЭК

    office_image_list: Все фото офиса (кроме фото как доехать).

    work_time_list: График работы на неделю.
        Вложенный тег с атрибутами day и periods.

    work_time_exceptions: Исключения в графике работы офиса

    weight_min: Минимальный вес (в кг.), принимаемый в ПВЗ (> WeightMin)

    weight_max: Максимальный вес (в кг.), принимаемый в ПВЗ (<=WeightMax)

    fulfillment: Наличие зоны фулфилмента

    dimensions: Перечень максимальных размеров ячеек
        (только для type = POSTAMAT)

    errors: Список ошибок

    """

    code: constr(max_length=10)
    name: constr(max_length=50)
    location: Location
    address_comment: Optional[constr(max_length=255)]
    nearest_station: Optional[constr(max_length=120)]
    nearest_metro_station: Optional[constr(max_length=50)]
    work_time: constr(max_length=100)
    phones: list[Phone]
    email: Optional[constr(max_length=255)]
    note: Optional[constr(max_length=255)]
    type: OfficeType
    owner_code: OfficeOwner
    take_only: bool
    is_handout: bool
    is_dressing_room: bool
    have_cashless: bool
    have_cash: bool
    allowed_cod: bool
    site: Optional[constr(max_length=255)]
    office_image_list: Optional[list[Image]]
    work_time_list: list[WorkTime]
    work_time_exceptions: Optional[list[WorkTimeException]]
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
    type: Тип заказа:
        1 - "интернет-магазин" (только для договора типа "Договор с ИМ")
        2 - "доставка" (для любого договора)

        По умолчанию - 1

    number: Номер заказа в ИС Клиента
        (если не передан, будет присвоен номер заказа в ИС СДЭК - uuid)
        Только для заказов "интернет-магазин"

    tariff_code: Код тарифа

    comment: Комментарий к заказу

    developer_key: Ключ разработчика

    shipment_point: Код ПВЗ СДЭК, на который будет производиться
        забор отправления, либо самостоятельный привоз клиентом

    delivery_point: Код ПВЗ СДЭК, на который будет доставлена посылка

    date_invoice: Дата инвойса
        Только для заказов "интернет-магазин"

    shipper_name: Грузоотправитель
        Только для заказов "интернет-магазин"

    shipper_address: Адрес грузоотправителя
        Только для заказов "интернет-магазин"

    delivery_recipient_cost: Доп. сбор за доставку, которую ИМ
        берет с получателя.
        Только для заказов "интернет-магазин"

    delivery_recipient_cost_adv: Доп. сбор за доставку (которую
        ИМ берет с получателя) в зависимости от суммы заказа
        Только для заказов "интернет-магазин"

    sender: Отправитель

    seller: Реквизиты истинного продавца
        Только для заказов "интернет-магазин"

    recipient: Получатель

    from_location: Адрес отправления

    to_location: Адрес получения

    services: Дополнительные услуги

    packages: Список информации по местам (упаковкам)

    print: Необходимость сформировать печатную форму по заказу
        Может принимать значения:
        barcode - ШК мест (число копий - 1)
        waybill - квитанция (число копий - 2)

    """

    type: Optional[OrderType]
    number: Optional[constr(max_length=32)]
    tariff: Tariff
    tariff_code: Optional[int]
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

    @validator("tariff_code", always=True)
    def validate_tariff_code(cls, v, values):
        return values['tariff'].tariff_code

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
    def validate_international(cls, v, values, **kwargs):
        field = kwargs.get("field")
        tariff = values.get("tariff")
        if tariff_is_international(tariff):
            if v:
                return v
            else:
                raise ValueError(
                    f"You have to provide {field.name} in case of international order"
                )
        return v

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
    uuid: Идентификатор заказа в ИС СДЭК
    type: Тип связанной сущности
        Может принимать значения:
        waybill - квитанция к заказу
        barcode - ШК места к заказу
    """

    uuid: UUID
    is_return: bool
    is_reverse: bool
    type: Optional[OrderType]
    cdek_number: str
    number: Optional[constr(max_length=40)]
    delivery_mode: Optional[DeliveryMode]
    tariff_code: int
    comment: Optional[constr(max_length=255)]
    developer_key: Optional[str]
    shipment_point: Optional[str]
    delivery_point: Optional[str]
    date_invoice: Optional[date]
    shipper_name: Optional[constr(max_length=255)]
    shipper_address: Optional[constr(max_length=255)]
    delivery_recipient_cost: Optional[Money]
    delivery_recipient_cost_adv: Optional[Threshold]
    sender: Contact
    seller: Optional[Seller]
    recipient: Contact
    from_location: Location
    to_location: Location
    services: Optional[list[Service]]
    packages: list[Package]
    delivery_problem: Optional[list[Problem]]
    delivery_detail: dict
    transacted_payment: Optional[bool]
    statuses: Optional[list[Status]]
    calls: Optional[dict]



class OrderManipulationRequest(BaseModel):
    """
    request_uuid: Идентификатор запроса в ИС СДЭК

    type: Тип запроса
        Может принимать значения: CREATE, UPDATE, DELETE, AUTH, GET

    date_time: Дата и время установки текущего состояния запроса
        (формат yyyy-MM-dd'T'HH:mm:ssZ)

    state: Текущее состояние запроса
        Может принимать значения:

        ACCEPTED - пройдена предварительная валидация и запрос принят
        WAITING - запрос ожидает обработки (зависит от выполнения другого запроса)
        SUCCESSFUL - запрос обработан успешно
        INVALID - запрос обработался с ошибкой

    errors: Ошибки, возникшие в ходе выполнения запроса

    warnings: Предупреждения, возникшие в ходе выполнения запроса

    """

    request_uuid: Optional[UUID]
    type: OrderManipulationRequestType
    date_time: datetime
    state: OrderManipulationRequestState
    errors: Optional[list[Error]]
    warnings: Optional[list[Warning]]


class OrderCreationResponse(BaseModel):
    """
    entity: Информация о заказе
    requests: Информация о запросе над заказом
    related_entities: Связанные сущности (если в запросе был передан корректный print)
    """

    entity: Optional[Entity]
    requests: list[OrderManipulationRequest]
    related_entities: Optional[Entity]


class OrderInfoResponse(BaseModel):
    """
    entity: Информация о заказе
    requests: Информация о запросе над заказом
    related_entities: Связанные сущности (если в запросе был передан корректный print)
    """

    entity: Optional[Entity]
    requests: list[OrderManipulationRequest]
    related_entities: Optional[Entity]


def tariff_is_international(tariff: Tariff) -> bool:
    return tariff.tariff_code in (
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
