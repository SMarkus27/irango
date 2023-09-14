from math import ceil


def calculate_skip(limit: int, page: int) -> int:
    return (page - 1) * limit


def calculate_total_pages(total_items: int, limit: int) -> int:
    return ceil(total_items / limit)
