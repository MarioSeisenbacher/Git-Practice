from __future__ import annotations

def split_name(full_name: str) -> list[str]:
    """
    Split a full name into its constituents (by whitespace) and return
    
    
    """

    if not isinstance(full_name, str):
        raise TypeError
    
    parts = full_name.strip().split()
    if not parts:
        raise ValueError("full_name cannot be empty")
    return parts

def main() -> None:

    names = [
        "Alexander Schuster",
        "Mario Zeller",
        "Michael Gruber",
    ]
    results: list[list[str]] = []
    for full_name in names:
        try:
            parts = split_name(full_name)
        except(TypeError, ValueError) as exc:
            # Avoid bar except only catch what you expect !
            print(f"Skipping {full_name!r}: {exc}")
        else:
            print(parts)
            results.append(parts)

        print("All split names:", results)
if __name__ == "__main__":
    main()