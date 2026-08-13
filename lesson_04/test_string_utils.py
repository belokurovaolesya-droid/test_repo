import pytest

from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("тест", "Тест"),
        ("hello world", "Hello world"),
        ("04 апреля 2023", "04 апреля 2023"),
        ("123", "123"),
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        (" ", " "),
        ("123abc", "123abc"),
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        (" skypro", "skypro"),
        ("   123", "123"),
        ("   04 апреля 2023", "04 апреля 2023"),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        (" ", ""),
        ("skypro", "skypro"),
        ("skypro   ", "skypro   "),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "S"),
        ("SkyPro", "Pro"),
        ("12345", "3"),
        ("04 апреля 2023", "апреля"),
    ],
)
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "U"),
        ("", "S"),
        ("SkyPro", "s"),
        ("12345", "6"),
    ],
)
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False


@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("Hello World", "l", "Heo Word"),
        ("123123", "123", ""),
    ],
)
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "U", "SkyPro"),
        ("", "a", ""),
        ("SkyPro", "s", "SkyPro"),
        ("123", "4", "123"),
    ],
)
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected