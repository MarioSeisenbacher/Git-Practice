from __future__ import annotations

def split_name(full_name: str) -> list[str]:
    """
    Split a full name into its parts (by whitespace) and return them as a list.
    Raises:
        TypeError: if full_name is not a string
        ValueError: if full_name is empty/only whitespace
    """
    if not isinstance(full_name, str):
        raise TypeError("full_name must be a string")

    parts = full_name.strip().split()  # handles multiple spaces/tabs nicely
    if not parts:
        raise ValueError("full_name cannot be empty")
    return parts


def main() -> None:
    print("Hello World")

    # Use a literal instead of appends; use clear naming.
    names = [
        "Alexander Schuster",
        "Mario Zeller",
        "Jakob Lonauer",
    ]

    results: list[list[str]] = []
    for full_name in names:
        try:
            parts = split_name(full_name)
        except (TypeError, ValueError) as exc:
            # Avoid bare except: only catch what you expect.
            print(f"Skipping {full_name!r}: {exc}")
        else:
            # Keep functions pure; print/use the result outside the function.
            print(parts)
            results.append(parts)

    # Optional: summary of all processed names
    print("All split names:", results)


if __name__ == "__main__":
    main()
