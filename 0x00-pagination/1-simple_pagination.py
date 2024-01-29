#!/usr/bin/python3
"""
define server Class
"""

import csv
import math
from typing import List, Tuple


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
            assert type(page) == int and page > 0
            assert type(page_size) == int and page_size > 0

            start_idx, end_idx = index_range(page, page_size )
            idx_range = self.dataset()

            if start_idx > len(idx_range):
                return []
            
            return idx_range[start_idx:end_idx]
    



if __name__ == "__main__":
    
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")


    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))