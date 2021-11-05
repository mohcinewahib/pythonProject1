def short_pattern():
    pattern = {"sequence": 101, "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": 111000, "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": 1100110011001100, "occurrences": 50}
    return pattern


def run():
    print("Analysing patterns...")
    fi = short_pattern
    se = medium_pattern
    th = long_pattern
    group = {fi, se, th}
    for key, value in group.items():
        print(f"{key}: {value}")
run()
