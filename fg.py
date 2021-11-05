data = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}


def display_keys(data):
    for key in data.keys():
        print(key)
    print("\n")


def display_values(data):
    for value in data.values():
        print(value)
    print("\n")


def display_items(data):
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    # print(p)
    k = display_keys(data)
    # print(k)
    v = display_values(data)
    # print(v)
    i = display_items(data)
    # print(i)


    print(k)
    print(v)
    print(i)
run()