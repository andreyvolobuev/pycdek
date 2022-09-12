# Pycdek
CDEK API v2.0 will be implemented (https://api-docs.cdek.ru/29923741.html)



## Installation

```
git clone https://github.com/andreyvolobuev/pycdek
cd pycdek
python3 setup.py
```



## Example

1. Get your CLIENT_ID and CLIENT_SECRET [here](https://lk.cdek.ru/integration): 

![CDEK CREDENTIALS](cdek_credentials.png "CDEK Credentials")


```
import asyncio
from pycdek import CDEK


CLIENT_ID = '................................'
CLIENT_SECRET = '................................'


def main():
    cdek = CDEK(CLIENT_ID, CLIENT_SECRET)

    moscow = await cdek.get_cities(city="Москва")
    from_location = cdek.get_location("Тверская 1", moscow[0])
    # OR
    # shipment_points = await cdek.get_office(city=moscow[0])
    # shipment_point = shipment_points[0]

    vladivostok = await cdek.get_cities(city="Владивосток")
    to_location = cdek.get_location("Светланская 1", vladivostok[1])
    # OR
    # delivery_points = await cdek.get_office(city=vladivostok[1])
    # delivery_point = delivery_points[0]

    package = cdek.create_package(name="Подарок", weight=1)

    tariffs = await cdek.get_available_tariffs(
        from_location=from_location, to_location=to_location, packages=[package]
    )
    tariff = tariffs.fastest

    sender = cdek.get_contact(name="Иванов Иван Иванович", phones=["+79111111111"])
    recipient = cdek.get_contact(name="Петров Петр Петрович", phones=["+79222222222"])

    order = await cdek.register_order(
        tariff=tariff,
        from_location=from_location,
        # shipment_point=shipment_point,
        to_location=to_location,
        # delivery_point=delivery_point,
        packages=[package],
        sender=sender,
        recipient=recipient
    )

    info = await cdek.get_order_info(order.entity.uuid)


if __name__ == '__main__':
    asyncio.run(main())
```


## Testing

```
python3 -m unittest
```
