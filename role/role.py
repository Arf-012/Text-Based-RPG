class Role:
    def __init__(self, name: str, description: str, bonuses: dict):
        self.name = name
        self.description = description
        self.bonuses = bonuses  # Contoh: {'Strength': 5, 'Defense': 2}

    def __repr__(self):
        bonus_str = ', '.join(f"+{v} {k}" for k, v in self.bonuses.items())
        return f"{self.name}: {self.description} ({bonus_str})"


# Daftar role tersedia
available_roles = [
    Role(
        name="Warrior",
        description="Petarung jarak dekat dengan kekuatan fisik besar.",
        bonuses={"Physical_Power": 10, "Physical_Defense": 5}
    ),
    Role(
        name="Mage",
        description="Ahli sihir dengan kekuatan magic tinggi.",
        bonuses={"Magic_Power": 12, "Mana": 10}
    ),
    Role(
        name="Rogue",
        description="Gesit dan mematikan dalam serangan cepat.",
        bonuses={"Speed": 8, "Critical Chance": 5}
    ),
    Role(
        name="Tank",
        description="Pelindung kelompok dengan pertahanan sangat tinggi.",
        bonuses={"Physical_Defense": 15, "Health": 20}
    )
]
