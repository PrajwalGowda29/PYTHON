print("Prajwal BR\nUSN:1AY24AI083\nSec:O")
def display_inventory(inventory):
    """Display the player's inventory"""
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}")

def add_to_inventory(inventory, added_items):
    """Add loot to the inventory"""
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def print_table(inventory, order=None):
    """Print the inventory as a well-organized table"""
    print("Inventory:")
    print("{:<10} {:<10}".format('Item', 'Count'))
    print("-" * 20)
    
    items = inventory.items()
    if order == "count,asc":
        items = sorted(items, key=lambda x: x[1])
    elif order == "count,desc":
        items = sorted(items, key=lambda x: x[1], reverse=True)
    
    for item, count in items:
        print("{:<10} {:<10}".format(item, count))
    
    print("-" * 20)
    print("Total items:", sum(inventory.values()))

def import_inventory(filename="import_inventory.csv"):
    """Import inventory from a CSV file"""
    import csv
    inventory = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    inventory[row[0]] = int(row[1])
        print(f"Inventory imported from {filename}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found. Starting with empty inventory.")
    except Exception as e:
        print(f"Error importing inventory: {e}")
    return inventory

def export_inventory(inventory, filename="export_inventory.csv"):
    """Export inventory to a CSV file"""
    import csv
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item, count in inventory.items():
                writer.writerow([item, count])
        print(f"Inventory exported to {filename}")
    except Exception as e:
        print(f"Error exporting inventory: {e}")

def main():
    inventory = import_inventory()
    
    if not inventory:  
        inventory = {
            'rope': 1,
            'torch': 6,
            'gold coin': 42,
            'dagger': 1,
            'arrow': 12
        }
    
    while True:
        print("\nFantasy Game Inventory System")
        print("1. Display inventory")
        print("2. Add loot to inventory")
        print("3. Print sorted inventory table")
        print("4. Export inventory")
        print("5. Import inventory")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            loot = input("Enter items to add (comma separated): ").split(',')
            loot = [item.strip() for item in loot if item.strip()]
            inventory = add_to_inventory(inventory, loot)
            print("Items added to inventory!")
        elif choice == "3":
            print("\nSort options: [none], count,asc, count,desc")
            sort_order = input("Enter sort order: ").strip()
            if sort_order in ["", "none", "count,asc", "count,desc"]:
                print_table(inventory, sort_order if sort_order != "none" else None)
            else:
                print("Invalid sort order. Displaying unsorted.")
                print_table(inventory)
        elif choice == "4":
            filename = input("Enter filename to export to (default: export_inventory.csv): ") or "export_inventory.csv"
            export_inventory(inventory, filename)
        elif choice == "5":
            filename = input("Enter filename to import from (default: import_inventory.csv): ") or "import_inventory.csv"
            inventory = import_inventory(filename)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
