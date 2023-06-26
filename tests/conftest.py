import pytest 
from itertools import product
from apollo.enums import Category
from apollo.stage import Stage
from apollo.theater import Theater

# Fixture to create a sample stage object for testing
@pytest.fixture
def sample_stage():
    name = "Test Stage"
    num_rows = 4
    num_seats_per_row = 5
    category_prices = {
        Category.STANDARD: 10.0,
        Category.VIP: 20.0,
        Category.PREMIUM: 30.0
    }

    stage = Stage(name, num_rows, num_seats_per_row, category_prices)

    # Assign categories to seats for testing
    for (row, _), seat in zip(product(range(num_rows), range(num_seats_per_row)), stage.seats):
        if row == 0: 
            seat.category = Category.VIP
        elif row == 1: 
            seat.category = Category.PREMIUM
        else: 
            seat.category = Category.STANDARD

    yield stage


# Fixture to create a sample theater object with a sample stage added
@pytest.fixture
def sample_theater(sample_stage):
    theater = Theater()
    theater.add_stage(sample_stage)
    yield theater
    theater.remove_stage(sample_stage)


@pytest.fixture
def sample_ticket(sample_theater): 
    ticket = sample_theater.buy_ticket("Test Stage", "A1")
    yield ticket