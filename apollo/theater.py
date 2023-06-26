from typing import List, Dict
import time
from .enums import Category
from .stage import Stage
from .ticket import Ticket
from .errors import StageNotFoundError


class Theater:
    def __init__(self):
        self.stages = {}

    def add_stage(self, stage: Stage):
        self.stages[stage.name] = stage

    def remove_stage(self, stage:Stage):
        del self.stages[stage.name]

    def get_stage(self, stage_name: str) -> Stage:
        stage = self.stages.get(stage_name)
        if not stage:
            raise StageNotFoundError(f"Stage '{stage_name}' not found in theater")
        return stage

    def get_seat(self, stage_name: str, seat_code: str):
        stage = self.get_stage(stage_name)
        return stage.get_seat(seat_code)

    def get_available_seats(self, stage_name: str, category: Category = None) -> List[Dict]:
        stage = self.get_stage(stage_name)
        seats = stage.get_available_seats(category)
        return [{"code": str(seat), "category": seat.category.name} for seat in seats]

    def get_best_available_seat(self, stage_name: str, category: Category = None) -> str:
        stage = self.get_stage(stage_name)
        seat = stage.get_best_available_seat(category)
        return str(seat)

    def get_seat_price(self, stage_name: str, seat_code: str) -> float:
        stage = self.get_stage(stage_name)
        return stage.get_seat_price(seat_code)

    def buy_ticket(self, stage_name: str, seat_code: str) -> Ticket:
        stage = self.get_stage(stage_name)
        seat = stage.reserve_seat(seat_code)
        return Ticket(stage, seat)

    def clean_theater(self): 
        time.sleep(30)
        return True