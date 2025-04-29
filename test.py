# Untuk Testing dan pencarian Bug

# Tempat Bermain 

# main.py

from player.player import Player
from enemies.goblin import Goblin
from skills.status_effect.burn import Burn

# Inisialisasi player
player = Player()

# Inisialisasi musuh (contoh: Goblin)
goblin = Goblin()

# Fungsi utama game loop
def game_loop():
    print("🎮 Selamat datang di dunia Text RPG!")
    while not player.is_dead:
        print("\n==== Menu Utama ====")
        print("1. Status")
        print("2. Istirahat")
        print("3. Lawan Monster")
        print("4. Keluar Game")

        choice = input("Pilih aksi: ")

        if choice == "1":
            show_status()
        elif choice == "2":
            player.rest(minutes=1)
        elif choice == "3":
            battle(goblin)
        elif choice == "4":
            print("Keluar dari game...")
            break
        else:
            print("Pilihan tidak valid.")

# Tampilkan status player
def show_status():
    print(f"\n{player.name} - Level {player.attributes['level']}")
    for stat, value in player.attributes.items():
        print(f"{stat}: {value}")

# Fungsi battle sederhana
def battle(enemy):
    print(f"\n⚔️ {player.name} bertemu {enemy.name}!")
    turn = 1
    burn_effect = Burn(damage_per_turn=player.attributes['Magic_Power'])

    while not player.is_dead and not enemy.is_dead:
        print(f"\nTurn {turn}")
        action = input("Serang (a) / Keluar (k): ").lower()

        if action == 'a':
            damage = player.attributes['Physical_Power']
            enemy.take_damage(damage)
            print(f"{player.name} menyerang {enemy.name} dengan {damage} damage!")

            # Terapkan efek burn jika musuh belum mati
            if not enemy.is_dead:
                burn_effect.apply(enemy)

        elif action == 'k':
            print("Mundur dari pertempuran!")
            break
        else:
            print("Aksi tidak dikenal.")

        turn += 1
        player.apply_debuff_check()

if __name__ == "__main__":
    game_loop()
