# Untuk musuh dalam game

class Goblin:
    def __init__(self):
        self.name = "Goblin"
        self.id = 2
        self.attributes = {
            'level': 1,
            'xp': 20,
            'Health': 100,
            'Mana': 5,
            'Magic_Power': 0,
            'Physical_Power': 10,
            'Physical_Defense': 5,
            'Magic_Defense': 2,
            'Stamina': 50,
            'Speed': 15
        }

        # Max values
        self.max_health = 100
        self.max_mana = 5
        self.max_stamina = 50

        self.weapon = ["Knife", 6]
        self.armor = ["None", 0]
        self.gold = 10

        self.is_dead = False

        # NEW: Status effect list
        self.status_effects = []

    def take_damage(self, amount):
        self.attributes['Health'] -= amount
        print(f"{self.name} took {amount} damage. Remaining HP: {self.attributes['Health']}")
        self.apply_debuff_check()

    def apply_debuff_check(self):
        if self.attributes['Health'] <= 0:
            self.is_dead = True
            print(f"{self.name} has died.")

    def add_status_effect(self, effect):
        self.status_effects.append(effect)
        print(f"{self.name} is now affected by {type(effect).__name__}!")

    def process_status_effects(self):
        for effect in self.status_effects[:]:
            effect.apply(self)
            if effect.duration <= 0:
                self.status_effects.remove(effect)
                print(f"{type(effect).__name__} has worn off from {self.name}.")
