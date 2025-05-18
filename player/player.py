import random
import role.role as Role

class Player:
    def __init__(self, name, element, role):
        self.name = name
        self.element = element
        self.role = role or Role.Role({})  # Default role
        self.id = 1
        self.location = 'Start'

        self.attributes = {
            'level': 1,
            'xp': 0,
            'xp_limit': 100,
            'stat_points': 0,
            'Health': 100,
            'Mana': 10,
            'Magic_Power': 0,
            'Physical_Power': 10,
            'Physical_Defense': 15,
            'Magic_Defense': 5,
            'Stamina': 100,
            'Speed': 20
        }

        # Apply role bonuses
        for stat, bonus in self.role.bonuses.items():
            if stat in self.attributes:
                self.attributes[stat] += bonus
            else:
                self.attributes[stat] = bonus

        # Max values
        self.max_health = 100
        self.max_mana = 10
        self.max_stamina = 100

        self.weapon = ["Pedang Karat", 6]
        self.armor = ["None", 0]
        self.gold = 0

        self.is_dead = False
        self.status_effects = []

    def gain_xp(self, amount):
        self.attributes['xp'] += amount
        print(f"{self.name} gained {amount} XP.")
        while self.attributes['xp'] >= self.attributes['xp_limit']:
            self.level_up()

    def level_up(self):
        self.attributes['xp'] -= self.attributes['xp_limit']
        self.attributes['level'] += 1
        self.attributes['xp_limit'] *= 2
        gained_points = self.attributes['level'] * 2
        self.attributes['stat_points'] += gained_points
        print(f"Level up! {self.name} is now level {self.attributes['level']} and earned {gained_points} stat points.")

    def rest(self, minutes):
        heal_amount = minutes * 10
        mana_restore = minutes * 5
        stamina_restore = minutes * 15

        self.attributes['Health'] = min(self.attributes['Health'] + heal_amount, self.max_health)
        self.attributes['Mana'] = min(self.attributes['Mana'] + mana_restore, self.max_mana)
        self.attributes['Stamina'] = min(self.attributes['Stamina'] + stamina_restore, self.max_stamina)

        print(f"{self.name} rested for {minutes} minute(s). Restored {heal_amount} HP, {mana_restore} MP, {stamina_restore} Stamina.")

    def apply_debuff_check(self):
        if self.attributes['Health'] <= 0:
            self.is_dead = True
            print(f"{self.name} has died.")

        if self.attributes['Mana'] < self.max_mana * 0.1:
            print("⚠️ Low Mana! Mana debuff applied.")

        if self.attributes['Stamina'] < self.max_stamina * 0.15:
            print("⚠️ Fatigue! Stamina debuff applied.")

    def take_damage(self, amount):
        self.attributes['Health'] -= amount
        print(f"{self.name} took {amount} damage. Remaining HP: {self.attributes['Health']}")
        self.apply_debuff_check()

    def add_status_effect(self, effect):
        self.status_effects.append(effect)
        print(f"{self.name} is now affected by {type(effect).__name__}!")

    def process_status_effects(self):
        for effect in self.status_effects[:]:  # Salinan list biar aman hapus saat looping
            effect.apply(self)
            if effect.duration <= 0:
                self.status_effects.remove(effect)
                print(f"{type(effect).__name__} has worn off from {self.name}.")

class Inventory:
    def __init__(self):
        self.items = {
            "C1": ["Coins", 0]  # ID: [Item Name, Count]
        }
        self.max_items = 20

    def add_item(self, item_id, item_name):
        if len(self.items) < self.max_items:
            if item_id in self.items:
                self.items[item_id][1] += 1
            else:
                self.items[item_id] = [item_name, 1]
        else:
            print("Inventory is full!")
