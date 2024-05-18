from src.basic_calculator import add, divide, multiply, subtract


def main():
    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 5 and 3:", subtract(5, 3))
    print("Multiplication of 5 and 3:", multiply(5, 3))
    print("Division of 5 and 3:", divide(5, 3))
    print("Division of 5 and 0:", divide(5, 0))  # Test division by zero
    print("Addition with incorrect types:", add(5, "three"))  # Test type check

if __name__ == "__main__":
    main()