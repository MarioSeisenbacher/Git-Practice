def check_string(name: str) -> str:
    if not isinstance(name,str):
        raise ValueError("The variable is not of type sring")
    return name


def split_string(name: str) -> list:
    if check_string(name):
        parts = name.strip().split()
    return parts

def main() -> None:
    name_array = [
        "Jakob Lonauer",
        "Alexander Schuster",
        "Miracle Bear"        
    ]

    results = []

    for name in name_array:
        parts = split_string(name)
        results.append(parts) 
        print(f"Mein Name ist {parts[0]} und mein Nachname lautet {parts[1]}")

    print(f"Hier ist eine Auflistung aller Namen{results}")

    return None


if __name__ == "__main__":
    main()