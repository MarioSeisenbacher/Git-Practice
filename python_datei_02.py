from __future__ import annotations

def check_type(name: str) -> None:
    """
    split_string method is used to split a full_name into its constituents e.g. "Jakob Lonauer" -> "Jakob", "Lonauer"
    
    """
    if not isinstance(name, str):
        raise TypeError("full_name must be a String")

    parts = name.strip().split()
    return parts

def main():
    results = []
    name_array = [
        "Jakob Lonauer",
        "Alexander Schuster",
        "Michael Gruber",
    ]
    for name in name_array:
        parts = check_type(name)
        results.append(parts)

    print(results)    



if __name__ == "__main__":
    main()

print("Hello World")
print("Jesus Maria")
print("Jesus NAVA")

