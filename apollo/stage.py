from typing import Dict, List

from .errors import SeatNotFoundError, InsufficientSeatsError, SeatAlreadySoldError
from .enums import Category
from .seat import Seat


class Stage:
    def __init__(self, name: str, num_rows: int, num_seats_per_row: int, category_prices: Dict[Category, float]):
        self.name = name
        self.seats = []
        for row in range(1, num_rows + 1):
            row_name = chr(64 + row)  # use alphabetic rows (A, B, C, etc.)
            for seat_number in range(1, num_seats_per_row + 1):
                seat = Seat(row_name, seat_number)
                self.seats.append(seat)
        self.category_prices = category_prices

    def _get_seat(self, row: str, number: int) -> Seat:
        for seat in self.seats:
            if seat.row == row and seat.number == number:
                return seat
        raise SeatNotFoundError

    def get_seat(self, seat_code: str) -> Seat:
        row = seat_code[:-1]
        seat_number = int(seat_code[-1])
        return self._get_seat(row, seat_number)

    def get_available_seats(self, category: Category = None) -> List[Seat]:
        if category:
            return [seat for seat in self.seats if not seat.is_reserved and seat.category == category]
        else:
            return [seat for seat in self.seats if not seat.is_reserved]

    def get_best_available_seat(self, category: Category = None) -> Seat:
        seats = self.get_available_seats(category)
        if not seats:
            raise InsufficientSeatsError("No available seats")
        return seats[0]

    def _get_seat_price(self, seat: Seat) -> float:
        return self.category_prices.get(seat.category, 0)

    def get_seat_price(self, seat_code: str) -> float:
        seat = self.get_seat(seat_code)
        if not seat:
            raise SeatNotFoundError(f"Seat {seat_code} not found in stage {self.name}")
        return self._get_seat_price(seat)

    def reserve_seat(self, seat_code: str) -> Seat:
        seat = self.get_seat(seat_code)
        if not seat:
            raise SeatNotFoundError(f"Seat {seat_code} not found in stage {self.name}")
        if seat.is_reserved:
            raise SeatAlreadySoldError(f"Seat {seat_code} is already reserved")
        seat._is_reserved = True
        return seat
