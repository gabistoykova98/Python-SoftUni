stores = {}

while True:
    command = input()

    if command == "Go Shopping!":
        break

    tokens = command.split("->")
    action = tokens[0]
    store = tokens[1]

    if action == "Add":
        items = [item.strip() for item in tokens[2].split(",")]
        if store not in stores:
            stores[store] = set()
        stores[store].update(items)

    elif action == "Important":
        item = tokens[2].strip()
        if store not in stores:
            stores[store] = set()
        if item not in stores[store]:
            stores[store].add(item)
        else:
            stores[store].remove(item)
            stores[store].add(item)

    elif action == "Remove":
        if store in stores:
            if any(item in stores[store] for item in stores[store]):
                continue
            del stores[store]

# Print the stores and their items
for store, items in stores.items():
    print(store)
    for item in items:
        print(f"-- {item}")