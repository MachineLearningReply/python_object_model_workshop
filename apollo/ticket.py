from pathlib import Path
from datetime import datetime
from .seat import Seat
from .stage import Stage


class Ticket:
    def __init__(self, stage: Stage, seat: Seat):
        self.stage = stage
        self.seat = seat
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Ticket for Stage {self.stage.name} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}, Seat {str(self.seat)}"

    def save_ticket(self, path: Path):
        #d = path / "tickets"
        #d.mkdir()
        #p = d / 'ticket.txt'
        path.write_text(str(self))