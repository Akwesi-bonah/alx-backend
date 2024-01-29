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
