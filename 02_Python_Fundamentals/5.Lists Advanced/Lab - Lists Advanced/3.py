stores = {}
command = input()

while command != "Go Shopping!":
    info = command.split("->")
    type_command = info[0]

    if type_command == "Add":
        store = info[1]
        data = info[2]
        if store not in stores:
            stores[store] = set()
        for item in data:
            stores[store].add(item.strip())

    elif type_command == "Important":
        store = info[1]
        data = info[2]
        if store not in stores:
            stores[store] = set()
        for item in data:
            if item not in store:
                stores[store].add(item.strip())

    elif type_command == "Remove":
        store = info[1]
        if store in stores and not any(item.startswith("!") for item in stores[store]):
            del stores[store]

    command = input()

for store, data in sorted(stores.items()):
    print(store)
    for item in data:
        print(f"  {item}")



