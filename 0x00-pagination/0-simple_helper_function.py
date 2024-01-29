#!/usr/bin/env python3
"""defines a function index_range"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function that returns start and end index of a page
    Args: 
        page: int
        page_size: int

    return (tuple)
    """

    start_page = (page * page_size) - page_size
    end_page = start_page + page_size

    return (start_page, end_page)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)