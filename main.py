# Get input from the user
num = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Check if the input number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # Calculate the factorial using a while loop
    while num > 0:
        factorial *= num
        num -= 1

    # Display the factorial
    print("The factorial is:", factorial)
