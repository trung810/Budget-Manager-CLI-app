filepath = "cache.txt"

def clear_cache(input_file = filepath):
    with open(input_file, "w", encoding="utf-8") as f:
        f.write("food: 0\n")
        f.write("transport: 0\n")
        f.write("living: 0\n")
        f.write("shopping: 0\n")
        f.write("health: 0\n")
        f.write("savings: 0\n")
    print(f"Cleared cache.")

clear_cache(filepath)