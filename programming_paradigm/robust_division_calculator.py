# robust_division_calculator_cli.py

import sys

def safe_divide(numerator, denominator):
    """Safely divide two numbers with error handling."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."


def main():
    if len(sys.argv) != 3:
        print("Usage: python robust_division_calculator_cli.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)


if __name__ == "__main__":
    main()
