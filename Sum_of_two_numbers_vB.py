def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please provide two valid numbers.")

    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

if __name__ == '__main__':
    main()