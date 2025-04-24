# Untuk musuh dalam game

class Goblin:
    def __init__(self):
        self.id = 2
        self.attributes = {
            'level': 1,
            'xp': 20,
            'Health': 100,
            'Mana': 5,
            'Strength': 10,
            'Defense': 5,
            'Stamina': 50,
            'Speed': 15
        }
        self.weapon = ["Knife", 6]
        self.armor = ["None", 0]
        self.gold = 0