from pytest import raises

from leap import NotGregorianYear, Year


def test_is_not_leap_when_not_divisible_by_4():
    assert Year(2001).is_leap() is False


def test_is_leap_when_divisible_by_4():
    assert Year(2004).is_leap() is True


def test_is_not_leap_when_divisible_by_100():
    assert Year(1900).is_leap() is False


def test_is_leap_when_divisible_by_400():
    assert Year(2000).is_leap() is True


def test_raises_not_gregorian_year_when_before_1583():
    with raises(NotGregorianYear):
        Year(1500).is_leap()


def test_converts_to_int_when_float():
    assert Year(2004.2).is_leap() is True


def test_converts_to_int_when_string():
    assert Year("2004").is_leap() is True
