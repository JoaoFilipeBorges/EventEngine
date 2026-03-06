import random

from entities import GameState
from events import Event


def cold_storm(state):
    state.temperature -= 10
    state.coal -= 20
    state.morale -= 0.05


def successful_hunt(state):
    state.food += 50
    state.morale += 0.05


def disease_outbreak(state):
    state.sickness += 0.1
    state.morale -= 0.1


events = [
    Event("Cold Storm", 0.2, cold_storm),
    Event("Disease Outbreak", 0.15, disease_outbreak),
    Event("Successful Hunt", 0.25, successful_hunt),
]


class EventEngine:
    def __init__(self, events):
        self.events = events

    def generate_event(self, state):

        for event in self.events:
            if random.random() < event.probability:
                event.trigger(state)
                return event.name

        return "No event"


def simulate_turn(state, engine):

    event_name = engine.generate_event(state)

    # basic consumption
    state.food -= state.population * 0.5
    state.coal -= 5

    return event_name


engine = EventEngine(events)

state = GameState(
    population=80, food=200, coal=150, temperature=-10, morale=0.7, sickness=0.1
)

for turn in range(10):
    event = simulate_turn(state, engine)

    print(f"Turn {turn+1}")
    print("Event:", event)
    print(state)
    print()
