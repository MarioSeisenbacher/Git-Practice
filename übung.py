

def checkType(name) -> bool:
    
    if not isinstance(name, str):
        print("Its a string")
    return name


def split_string(name: list[list[str]]) -> list:
    """Splits a string into parts based on whitespace."""

    if checkType(name):   
        parts = name.strip().split()

    return parts


def main() -> None:
    name_array = [
        "Jakob Lonauer",
        "Max Mustermann",
        "Alexander Schuster"

    ]

    results = []

    for name in name_array:
        parts = split_string(name)
        results.append(parts)

    print(results)


if __name__ == "__main__":
    main()


