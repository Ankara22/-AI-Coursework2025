"""Prompt the user for 5 numeric values, then display their average."""


def main():
    values = []
    count_required = 5

    # Keep asking until we have exactly 5 valid numbers
    while len(values) < count_required:
        try:
            remaining = count_required - len(values)
            prompt = f"Enter a number ({remaining} remaining): "
            value_str = input(prompt).strip()
            value = float(value_str)
            values.append(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    average = sum(values) / count_required
    print(f"You entered: {values}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()

