def create_shop():
    return {
        "Sword": {"price": 50, "category": "Weapons", "attack": 5},
        "Shield": {"price": 40, "category": "Armor", "defense": 5},
        "Health Potion": {"price": 20, "category": "Potions", "heal": 25}
    }


def show_shop(shop):
    print("\n🏪 SHOP ITEMS")
    for item, data in shop.items():
        print(f"{item} - {data['price']} gold")


def buy_item(inventory, shop, player):
    show_shop(shop)
    choice = input("Enter item to buy: ").strip()

    if choice not in shop:
        print("❌ Item not found.")
        return

    price = shop[choice]["price"]

    if player["gold"] < price:
        print("❌ Not enough gold.")
        return

    player["gold"] -= price
    category = shop[choice]["category"]

    if choice in inventory[category]:
        inventory[category][choice]["quantity"] += 1
    else:
        inventory[category][choice] = {"quantity": 1}

    print(f"✅ Bought {choice}!")


def sell_item(inventory, shop, player):
    show_inventory = False

    print("\n💰 SELL ITEMS")
    for category, items in inventory.items():
        for item in items:
            print("-", item)

    choice = input("Enter item to sell: ").strip()

    for category, items in inventory.items():
        if choice in items and items[choice]["quantity"] > 0:
            price = shop.get(choice, {}).get("price", 10)
            player["gold"] += price
            items[choice]["quantity"] -= 1
            print(f"✅ Sold {choice} for {price} gold.")
            return

    print("❌ Item not available to sell.")
