import pytest
from apollo.enums import Category
from apollo.errors import StageNotFoundError, SeatNotFoundError, SeatAlreadySoldError
from apollo.stage import Stage

# Tests for the Theater class
def test_add_stage(sample_theater):
    name = "New Stage"
    num_rows = 3
    num_seats_per_row = 4
    category_prices = {
        Category.STANDARD: 8.0,
        Category.VIP: 18.0,
        Category.PREMIUM: 28.0
    }
    stage = Stage(name, num_rows, num_seats_per_row, category_prices)
    sample_theater.add_stage(stage)
    assert sample_theater.get_stage(name) == stage


def test_get_stage(sample_theater):
    stage_name = "Test Stage"
    stage = sample_theater.get_stage(stage_name)
    assert stage.name == stage_name


def test_get_stage_invalid(sample_theater):
    stage_name = "Invalid Stage"
    with pytest.raises(StageNotFoundError):
        sample_theater.get_stage(stage_name)

def test_get_nonexistent_seat(sample_theater):
    seat_code = "A0"
    with pytest.raises(SeatNotFoundError):
        sample_theater.get_seat("Test Stage", seat_code)

@pytest.mark.slow
def test_clean_theather(sample_theater):
    assert sample_theater.clean_theater()
