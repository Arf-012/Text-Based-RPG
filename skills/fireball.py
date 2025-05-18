from skills.status_effect.burn import Burn
import player.player as Player

class Fireball:
    def __init__(self):
        self.id = 1
        self.attributes = {
            'level': 1,
            'Mana_cost': 10,
            'Stamina_cost': 5,
            'Accuracy': 80,  # persen (%)
            'Cooldown': 5
        }
        self.type = "Magic"
        self.element = "Fire"
        self.range = "Long"
        self.description = "A powerful fireball that deals damage to enemies and may inflict burn."

    def use(self, user, target):
        """user = caster (player atau musuh), target = musuh atau player"""
        import random

        print(f"{user.name} casts Fireball on {target.name}!")
        
        if random.randint(1, 100) <= self.attributes['Accuracy']:
            magic_power = user.attributes['Magic_Power']
            base_damage = magic_power * 1.5  # Scaling Fireball dari Magic Power
            print(f"Fireball hits! {target.name} takes {base_damage:.1f} damage.")
            target.take_damage(base_damage)

            # Beri efek burn
            burn_effect = Burn(magic_power // 4)  # Damage Burn 25% dari Magic Power
            target.add_status_effect(burn_effect)
            print(f"{target.name} is now Burning! 🔥")
        else:
            print(f"{user.name}'s Fireball missed!")
