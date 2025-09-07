from datetime import datetime, timedelta

def count_fridays(start_date: str, end_date: str) -> int:
    """
    Counts the number of Fridays between start_date and end_date (inclusive).
    Dates should be in 'YYYY-MM-DD' format.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    count = 0
    current = start
    while current <= end:
        if current.weekday() == 4:  # 4 is Friday
            count += 1
        current += timedelta(days=1)
    return count

if __name__ == "__main__":
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    fridays = count_fridays(start, end)
    print(f"Number of Fridays between {start} and {end}: {fridays}")