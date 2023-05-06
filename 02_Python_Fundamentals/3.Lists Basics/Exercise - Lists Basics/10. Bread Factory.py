stores = {}

while True:
    command = input()
    if command == "Go Shopping!":
        break

    tokens = command.split("->")
    instruction = tokens[0]
    store_name = tokens[1]

    if instruction == "Add":
        items = tokens[2].split(",")
        if store_name not in stores:
            stores[store_name] = set()
        for item in items:
            stores[store_name].add(item.strip())

    elif instruction == "Important":
        item = tokens[2].strip()
        if store_name not in stores:
            stores[store_name] = set()
        stores[store_name].add(item)
        for other_store in stores:
            if other_store != store_name and item in stores[other_store]:
                stores[other_store].remove(item)

    elif instruction == "Remove":
        if store_name in stores and not any(item.startswith("!") for item in stores[store_name]):
            del stores[store_name]

# print the final list of stores and items
for store, items in sorted(stores.items()):
    print(store)
    for item in items:
        print(f"  {item}")
