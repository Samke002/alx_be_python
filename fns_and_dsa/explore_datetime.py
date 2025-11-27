from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format and print the current date and time
    formatted_current = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current}")

    return current_date


def calculate_future_date(current_date):
    # Prompt the user for days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)

    # Print the future date in YYYY-MM-DD format
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")


def main():
    # Part 1 – Display current date/time
    current_date = display_current_datetime()

    # Part 2 – Calculate and display a future date
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
