def create_player():
    return {
        "name": "Hero",
        "gold": 100,
        "health": 100,
        "attack": 10,
        "defense": 5,
        "equipped": None
    }


def show_player_stats(player):
    print("\n🧙 PLAYER STATS")
    for key, value in player.items():
        print(f"{key.capitalize()}: {value}")


def equip_item(inventory, player):
    weapons = inventory.get("Weapons", {})
    if not weapons:
        print("❌ No weapons available to equip.")
        return

    print("\n⚔️ Available Weapons:")
    for item in weapons:
        print("-", item)

    choice = input("Enter weapon to equip: ").strip()
    if choice in weapons:
        player["equipped"] = choice
        print(f"✅ {choice} equipped!")
    else:
        print("❌ Weapon not found.")
