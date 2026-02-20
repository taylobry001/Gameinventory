def create_starter_inventory():
    return {
        "Weapons": {
            "Sword": {"quantity": 1, "attack": 5}
        },
        "Potions": {
            "Health Potion": {"quantity": 2, "heal": 25}
        },
        "Armor": {}
    }


def show_inventory(inventory):
    print("\n🎒 INVENTORY")
    for category, items in inventory.items():
        print(f"\n{category}:")
        if not items:
            print("  (Empty)")
        for item, data in items.items():
            print(f"  {item} x{data['quantity']}")


def add_item(inventory):
    category = input("Enter category (Weapons/Potions/Armor): ").strip()
    item = input("Enter item name: ").strip()
    quantity = int(input("Enter quantity: "))

    if category not in inventory:
        inventory[category] = {}

    if item in inventory[category]:
        inventory[category][item]["quantity"] += quantity
    else:
        inventory[category][item] = {"quantity": quantity}

    print(f"✅ Added {quantity} {item}(s) to {category}.")


def use_item(inventory, player):
    potions = inventory.get("Potions", {})
    if not potions:
        print("❌ No potions available.")
        return

    print("\n🧪 Available Potions:")
    for item in potions:
        print("-", item)

    choice = input("Enter potion to use: ").strip()

    if choice in potions and potions[choice]["quantity"] > 0:
        player["health"] += potions[choice].get("heal", 0)
        potions[choice]["quantity"] -= 1
        print(f"💚 Used {choice}! Health increased.")
    else:
        print("❌ Potion not available.")


def count_total_items(inventory):
    total = 0
    for category in inventory.values():
        for item in category.values():
            total += item["quantity"]
    return total
