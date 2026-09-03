import re
import os
import subprocess

INCOME_ALLOCATION_RULES = {
    "savings": 0.30,
    "living": 0.20,
    "food": 0.30,
    "transport": 0.10,
    "shopping": 0.05,
    "health": 0.05
}

input_filepath = "DailyUpdate.txt"
cache_filepath = "cache.txt"

TEMPLATE = """food: 
transport: 
living: 
shopping: 
health: 
savings: 
income: 
"""

def read_file(input_file=input_filepath):
    categories = {}
    if not os.path.exists(input_file):
        return categories

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().strip('\u200b').strip('\xa0')

            if ":" in line:
                category, raw_values = line.split(":", 1)
                category = category.strip().lower()
                numbers = [float(n) for n in re.findall(r'[-+]?[\d.]+', raw_values)]
                categories[category] = sum(numbers) if numbers else 0.0

    return categories

def update_cache(input_file=input_filepath, cache_file=cache_filepath, rules=INCOME_ALLOCATION_RULES):
    daily_data = read_file(input_file)
    income = daily_data.pop("income", 0.0)
    expenses = daily_data

    income_additions = {cat.lower(): income * ratio for cat, ratio in rules.items()} if income > 0 else {}

    updated_lines = []
    category_balances = {}
    total_balance = 0.0

    with open(cache_file, "r", encoding="utf-8") as f:
        for line in f:
            raw_line = line.rstrip("\n")
            stripped = raw_line.strip().strip('\u200b').strip('\xa0')

            if ":" in stripped:
                category_name, raw_val = stripped.split(":", 1)
                key = category_name.strip().lower()

                current_match = re.search(r'[-+]?[\d.]+', raw_val)
                current_balance = float(current_match.group()) if current_match else 0.0

                added = income_additions.get(key, 0.0)
                spent = expenses.get(key, 0.0)
                new_balance = current_balance + (added - spent)*1000

                formatted_val = f"{int(new_balance)}" if new_balance.is_integer() else f"{new_balance:.2f}"
                updated_lines.append(f"{category_name}: {formatted_val}")
                
                category_balances[category_name.strip().capitalize()] = new_balance
                total_balance += new_balance
            else:
                updated_lines.append(raw_line)

    # Save to cache
    with open(cache_file, "w", encoding="utf-8") as f:
        f.write("\n".join(updated_lines) + "\n")

    # Display in terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===================================")
    print("       CURRENT BUDGET BALANCES     ")
    print("===================================")
    if income > 0:
        print(f" Income Added : +{income*1000:,.0f}\n")
    for cat, bal in category_balances.items():
        val_str = f"{int(bal):,}" if bal.is_integer() else f"{bal:,.2f}"
        print(f"  {cat:<15}: {val_str}")
    print("-----------------------------------")
    tot_str = f"{int(total_balance):,}" if total_balance.is_integer() else f"{total_balance:,.2f}"
    print(f"  TOTAL AVAILABLE : {tot_str}")
    print("===================================\n")

def reset_input_file(input_file=input_filepath):
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(TEMPLATE)

if __name__ == "__main__":
    update_cache()
    reset_input_file()
    
    while True:
            choice = input("Option [add: add transaction | exit: exit the app | config: edit cache | clear: reset cache]: ").strip().lower()
            
            if choice == 'add':
                exit(10)
                
            elif choice == 'exit':
                print("Exiting Budget Manager. Have a great day!")
                exit(0)
                
            elif choice == 'config':
                print("Opening cache.txt for manual editing...")
                subprocess.run(["start", "", cache_filepath], shell=True)
                
            elif choice == 'clear':
                print("Running ClearCache.py...")
                subprocess.run(["python", "ClearCache.py"])
                exit(10)
                
            else:
                print("Invalid command. Please enter 'y', 'n', 'config', or 'clear'.")