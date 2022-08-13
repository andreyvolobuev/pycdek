import pytest
import entities


def test_currency():
    assert entities.Currency.RUB == 1
    assert entities.Currency(3) == entities.Currency.USD
    assert entities.Currency.CNY == 6
    assert entities.Currency(13) == entities.Currency.KRW
