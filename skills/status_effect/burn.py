# skills/status_effect/burn.py

class Burn:
    def __init__(self, attribute_name="Magic_Power", multiplier=1.0):
        self.attribute_name = attribute_name
        self.multiplier = multiplier
        self.duration = 5

    def apply(self, target):
        if self.duration > 0:
            base = target.attributes.get(self.attribute_name, 0)
            scaled_damage = int(base * self.multiplier)

            print(f"{target.name} terbakar! 🔥 Kehilangan {scaled_damage} HP. ({self.duration} turn tersisa)")
            target.take_damage(scaled_damage)
            self.duration -= 1
        else:
            print(f"🔥 Efek Burn telah hilang dari {target.name}.")
            target.remove_status_effect(self)
