"""Request for a sphere radius and print its volume."""

def main():
    try:
        #  Read the radius value provided by the user
        radius_str = input("Enter the radius of the sphere: ").strip()
        radius = float(radius_str)
        #  Validate the input value
        if radius < 0:
            print("Please enter a positive number for the radius.")
            return
        #  Compute the volume; using 3.142 as an approximation for pi
        volume = (4 / 3) * 3.142 * (radius ** 3)
        #  Display the result
        print(f"The volume of the sphere is {volume}.")
    except ValueError:
        # Handle non-numeric or empty input 
        print("Invalid input. Please enter a numeric value for the radius.")


if __name__ == "__main__":
    main()
