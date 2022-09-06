from unittest import IsolatedAsyncioTestCase
from unittest.mock import MagicMock, patch, AsyncMock
from pycdek import CDEK, entities
from tests import data
from uuid import UUID


class TestPycdek(IsolatedAsyncioTestCase):
    @patch(
        "pycdek.client.TokenManager._read_token_from_file",
        return_value=entities.AccessToken(
            access_token="....", expires_in="6000", scope="...", jti="...."
        ),
    )
    def setUp(self, token_mock):
        CLIENT_ID = "................................"
        CLIENT_SECRET = "................................"
        self.cdek = CDEK(CLIENT_ID, CLIENT_SECRET)

    @patch(
        "pycdek.client.TokenManager._read_token_from_file",
        return_value=entities.AccessToken(
            access_token="....", expires_in="6000", scope="...", jti="...."
        ),
    )
    @patch("aiohttp.ClientSession.post")
    @patch("aiohttp.ClientSession.get")
    async def test_create_order(self, get_session, post_session, token_mock):
        r = MagicMock(status=200)
        r.json = AsyncMock(return_value=data.cities_moscow)
        context_manager = MagicMock()
        context_manager.__aenter__.return_value = r
        get_session.return_value = context_manager
        post_session.return_value = context_manager

        cities = await self.cdek.get_cities(city="Москва")
        self.assertIn("44", [city.code for city in cities])

        moscow = cities[0]
        from_location = self.cdek.get_location("Тверская 1", moscow)
        self.assertEqual(from_location.address, "Тверская 1")

        r.json = AsyncMock(return_value=data.cities_vladivostok)
        cities = await self.cdek.get_cities(city="Владивосток")
        self.assertIn("288", [city.code for city in cities])
        
        vladivostok = cities[1]
        to_location = self.cdek.get_location("Светланская 1", vladivostok)
        self.assertEqual(to_location.address, "Светланская 1")

        package = self.cdek.create_package(name="Подарок", weight=1)
        self.assertEqual(package.weight, 1)
        self.assertIn("Подарок", [item.name for item in package.items])

        r.json = AsyncMock(return_value=data.tariffs)
        tariffs = await self.cdek.get_available_tariffs(
            from_location=from_location, to_location=to_location, packages=[package]
        )
        self.assertEqual(31, len(tariffs.tariffs))
        self.assertEqual(696, tariffs.fastest.tariff_code)
        self.assertEqual(234, tariffs.cheapest.tariff_code)
        tariff = tariffs.fastest

        sender = self.cdek.get_contact(
            name="Иванов Иван Иванович", phones=["+79111111111"]
        )
        self.assertEqual("Иванов Иван Иванович", sender.name)
        self.assertIn("+79111111111", [phone.number for phone in sender.phones])

        recipient = self.cdek.get_contact(
            name="Петров Петр Петрович", phones=["+79222222222"]
        )
        self.assertEqual("Петров Петр Петрович", recipient.name)
        self.assertIn("+79222222222", [phone.number for phone in recipient.phones])
        
        r.json = AsyncMock(return_value=data.created_order2)
        order = await self.cdek.register_order(
            tariff=tariff,
            from_location=from_location,
            to_location=to_location,
            packages=[package],
            sender=sender,
            recipient=recipient,
        )

        self.assertEqual(
            UUID("72753034-cc78-4472-8e7f-8cebdc04ff86"), order.entity.uuid
        )
        self.assertEqual("CREATE", order.requests[0].type)
        self.assertEqual("ACCEPTED", order.requests[0].state)

        r.json = AsyncMock(return_value=data.order_info2)
        info = await self.cdek.get_order_info(order.entity.uuid)

        self.assertEqual(UUID("72753034-cc78-4472-8e7f-8cebdc04ff86"), info.entity.uuid)
        self.assertEqual(1, info.entity.type)
        self.assertEqual(tariff.tariff_code, info.entity.tariff_code)
