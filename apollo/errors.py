
class TheaterError(Exception):
    """Base class for theater-related errors"""


class StageNotFoundError(TheaterError):
    """Raised when a stage is not found"""


class SeatNotFoundError(TheaterError):
    """Raised when a seat is not found"""


class SeatAlreadySoldError(TheaterError):
    """Raised when a seat is already sold"""


class InsufficientSeatsError(TheaterError):
    """Raised when there are not enough available seats in a stage"""
