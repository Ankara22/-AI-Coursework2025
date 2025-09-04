"""Ask for a number of days and print the number of seconds."""

def main():
    try:
        # Read the number of days and convert to an integer
        days_str = input("Enter number of days: ").strip()
        days = int(days_str)
        # Validate the value provided (no negative day counts)
        if days < 0:
            print("Please enter a positive integer for days.")
            return
        # Compute seconds in the given number of days
        seconds = days * 24 * 60 * 60
        # Display the computed seconds
        print(f"There are {seconds} seconds in {days} day(s).")
    except ValueError:
        # # Handle non-numeric or empty input 
        print("Invalid input. Please enter a whole number (integer).")

if __name__ == "__main__":
    main()
