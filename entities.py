from dataclasses import dataclass

@dataclass
class GameState:
    population: int
    food: int
    coal: int
    temperature: int
    morale: float
    sickness: float