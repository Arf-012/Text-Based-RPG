# Untuk skill

class Fireball:
    def __init__(self):
        self.id = 1
        self.attributes = {
            'level': 1,
            'Mana_cost': 10,
            'Stamina_cost': 5,
            'Accuracy': 80,
            'Cooldown': 5
        }
        self.type = "Magic"
        self.element = "Fire"
        self.range = "Long"
        self.description = "A powerful fireball that deals damage to enemies. It has a chance to burn the target."