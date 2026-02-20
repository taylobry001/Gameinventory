# ============================================
# 🎮 Video Game Inventory System — Activity
# Python Dictionaries
# ============================================
#
# main.py ← Entry point + menu loop
# ============================================

from display import show_banner, show_menu, show_divider
from inventory import create_starter_inventory, show_inventory, add_item, use_item, count_total_items
from shop import create_shop, show_shop, buy_item, sell_item
from player import create_player, show_player_stats, equip_item


def main():
    show_banner()

    # Step 1: Create the player
    player = create_player()
    show_divider()

    # Step 2: Create starter inventory and shop
    inventory = create_starter_inventory()
    shop = create_shop()

    # Step 3: Main game loop
    playing = True
    while playing:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_inventory(inventory)

        elif choice == "2":
            show_player_stats(player)

        elif choice == "3":
            show_shop(shop)

        elif choice == "4":
            buy_item(inventory, shop, player)

        elif choice == "5":
            sell_item(inventory, shop, player)

        elif choice == "6":
            add_item(inventory)

        elif choice == "7":
            use_item(inventory, player)

        elif choice == "8":
            equip_item(inventory, player)

        elif choice == "9":
            total = count_total_items(inventory)
            print(f"\n📊 You have {total} total items across all categories.")

        elif choice == "0":
            print("\n👋 Thanks for playing! See you next time!")
            playing = False

        else:
            print("\n❌ Invalid choice. Try again.")

        if playing:
            show_divider()


if __name__ == "__main__":
    main()
