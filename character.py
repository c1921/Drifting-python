# character.py

import random

class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.attributes = {
            'Strength': random.randint(1, 10),
            'Agility': random.randint(1, 10),
            'Charisma': random.randint(1, 10),
            'Intelligence': random.randint(1, 10)
        }
        self.skills = {
            'Running': random.randint(1, 10),
            'Riding': random.randint(1, 10),
            'Management': random.randint(1, 10),
            'Eloquence': random.randint(1, 10),
            'Gathering': random.randint(1, 10)
        }
        self.traits = []

    @staticmethod
    def random_character():
        names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]
        name = random.choice(names)
        return Character(name)