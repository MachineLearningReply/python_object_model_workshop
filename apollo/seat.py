from typing import List, Dict
from .enums import Category


class Seat:
    def __init__(self, row: str, number: int):
        self.row = row
        self.number = number
        self._is_reserved = False
        self._category = None

    def __str__(self):
        return f"{self.row}{self.number}"

    @property
    def is_reserved(self):
        return self._is_reserved

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category: Category):
        self._category = category

