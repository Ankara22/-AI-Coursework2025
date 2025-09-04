"""Translate the given pseudocode into Python.

BEGIN
SET x TO 0, y TO 20
REPEAT
SUBTRACT 4 FROM y
ADD 2/y TO x
UNTIL y IS LESS THAN 6
DISPLAY x
END
"""


def main():
    x = 0
    y = 20

    # REPEAT UNTIL is like a do-while; execute body then test
    while True:
        y -= 4
        x += 2 / y
        if y < 6:
            break

    print(x)

if __name__ == "__main__":
    main()


