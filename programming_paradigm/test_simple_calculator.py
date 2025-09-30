import sys
import unittest

# ---------------------------
# Calculator Functions
# ---------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# ---------------------------
# Unit Tests
# ---------------------------

class TestSimpleCalculator(unittest.TestCase):

    # Test addition
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)

    # Test subtraction
    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)

    # Test multiplication
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 10), 0)

    # Test division
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-9, 3), -3)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


# ---------------------------
# Command Line Interface
# ---------------------------

def main():
    if len(sys.argv) == 1:
        # No arguments → run unit tests
        unittest.main(argv=[sys.argv[0]])
    elif len(sys.argv) == 4:
        operation = sys.argv[1]
        try:
            num1 = float(sys.argv[2])
            num2 = float(sys.argv[3])
        except ValueError:
            print("Error: Please enter numeric values only.")
            sys.exit(1)

        try:
            if operation == "add":
                print(add(num1, num2))
            elif operation == "sub":
                print(subtract(num1, num2))
            elif operation == "mul":
                print(multiply(num1, num2))
            elif operation == "div":
                print(divide(num1, num2))
            else:
                print("Error: Unknown operation. Use add, sub, mul, or div.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    else:
        print("Usage:")
        print("  Run tests: python simple_calculator.py")
        print("  Run operation: python simple_calculator.py <add|sub|mul|div> <num1> <num2>")


# ---------------------------
# Run Program
# ---------------------------

if __name__ == "__main__":
    main()
