"""Determine if a user-entered character is uppercase or lowercase."""


def uppercase(character):
    """Return True if the given character is uppercase A-Z."""
    return len(character) == 1 and character.isalpha() and character.isupper()


def lowercase(character):
    """Return True if the given character is lowercase a-z."""
    return len(character) == 1 and character.isalpha() and character.islower()


def main():
    try:
        # Read user input 
        input_value = input("Enter a single alphabetic character: ").strip()

        # Validate exactly one character and that it is alphabetic
        if len(input_value) != 1 or not input_value.isalpha():
            print("Please enter exactly one alphabetic character (A-Z or a-z).")
            return

        # Determine case using helper functions
        if uppercase(input_value):
            print("The character is UPPERCASE.")
        elif lowercase(input_value):
            print("The character is lowercase.")
        else:
            # This branch handles unexpected cases
            print("The character is neither uppercase nor lowercase.")
    except Exception:
        # Generic guard; input() rarely raises other exceptions in this context
        print("An unexpected error occurred while reading input.")


if __name__ == "__main__":
    main()


