import pytest

from src.utils.calculates import calculate_skip, calculate_total_pages


def test_calculate_skip():
    limit = 10
    page = 10

    expected = 90

    result = calculate_skip(limit, page)

    assert result == expected


def test_calculate_skip_invalid_input():
    limit = 10
    page = "10"

    with pytest.raises(TypeError):
        calculate_skip(limit, page)


def test_calculate_total_pages():
    total_items = 100
    limit = 10

    expected = 10

    result = calculate_total_pages(total_items, limit)

    assert result == expected


def test_calculate_total_pages_invalid_input():
    total_items = "100"
    limit = 10

    with pytest.raises(TypeError):
        calculate_total_pages(total_items, limit)


def test_calculate_total_pages_divid_by_zero():
    total_items = 100
    limit = 0

    with pytest.raises(ZeroDivisionError):
        calculate_total_pages(total_items, limit)
