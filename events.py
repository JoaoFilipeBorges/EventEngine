import random

from entities import GameState


class Event:
    def __init__(self, name, probability, effect):
        self.name = name
        self.probability = probability
        self.effect = effect

    def trigger(self, state):
        self.effect(state)
