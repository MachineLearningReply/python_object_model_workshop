import pytest
from apollo.enums import Category
from apollo.errors import SeatNotFoundError, SeatAlreadySoldError


# Tests for the Stage class
def test_get_seat(sample_stage):
    seat_code = "A1"
    seat = sample_stage.get_seat(seat_code)
    assert seat.row == "A"
    assert seat.number == 1

@pytest.mark.parametrize('seat_code, expected_error', [("A0", SeatNotFoundError), ("Z1", SeatNotFoundError)])
def test_get_seat_invalid(sample_stage, seat_code, expected_error):
    with pytest.raises(expected_error):
        sample_stage.get_seat(seat_code)


def test_get_available_seats(sample_stage):
    available_seats = sample_stage.get_available_seats(Category.VIP)
    assert len(available_seats) == 5


def test_get_best_available_seat(sample_stage):
    seat = sample_stage.get_best_available_seat(Category.PREMIUM)
    assert seat.row == "B"
    assert seat.number == 1


@pytest.mark.parametrize('seat_code, expected_price', [("B3", 30), ("A2", 20), ("C1", 10), ("D4", 10) ])
def test_get_seat_price(sample_stage, seat_code, expected_price):
    price = sample_stage.get_seat_price(seat_code)
    assert price == expected_price


def test_get_seat_price_invalid(sample_stage):
    seat_code = "Z1"
    with pytest.raises(SeatNotFoundError):
        sample_stage.get_seat_price(seat_code)

@pytest.mark.parametrize('seat_code, expected', [("A3", True), ("B2", True), ("C1", True)])
def test_reserve_seat(sample_stage, seat_code, expected):
    seat = sample_stage.reserve_seat(seat_code)
    assert seat.is_reserved == expected


def test_reserve_seat_already_reserved(sample_stage):
    seat_code = "A1"
    sample_stage.reserve_seat(seat_code)
    with pytest.raises(SeatAlreadySoldError):
        sample_stage.reserve_seat(seat_code)





