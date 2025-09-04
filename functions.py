"""Compute and display the area and perimeter of a square."""

def compute_square_area(side_length):
    """Return the area of a square given its side length."""
    return side_length * side_length


def compute_square_perimeter(side_length):
    """Return the perimeter of a square given its side length."""
    return 4 * side_length


def main():
    try:
        # Ask for the side length 
        side_str = input("Enter the side length of the square: ").strip()
        side = float(side_str)
        # Validate the input  (no negative lengths)
        if side < 0:
            print("Please enter a positive number to represent the side length.")
            return
        # Compute results using the helper function
        area = compute_square_area(side)
        perimeter = compute_square_perimeter(side)
        # Display the results
        print(f"Area of the square is {area}")
        print(f"Perimeter of the square is {perimeter}")
    except ValueError:
        # Handle cases where the input is not a number
        print("Invalid input. Please enter a numeric value for the side length.")


if __name__ == "__main__":
    main()


