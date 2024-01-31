#!/usr/bin/env python3
"""
define server Class
"""

import csv
from math import ceil
from typing import List, Tuple, Dict


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns list of rows"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        idx_range = self.dataset()

        if start_idx > len(idx_range):
            return []

        return idx_range[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary"""

        start_idx, end_idx = index_range(page, page_size)
        data = self.get_page(page, page_size)
        page_size = len(data)

        if start_idx > 0:
            prev_page = page - 1
        else:
            prev_page = None

        if end_idx < len(self.__dataset):
            next_page = page + 1
        else:
            next_page = None

        page_count = ceil(len(self.__dataset) / page_size)

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': page_count
        }
