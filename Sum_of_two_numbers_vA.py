import sys

if len(sys.argv) != 3:
    print("Error: Please provide exactly two numbers as command-line arguments.")
    sys.exit()

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except Exception:
    print("Error: Please provide two valid numbers as command-line arguments.")
    sys.exit()

sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")
