# Checks if number is an odd or even
num = int(input("Enter a number: "))
check = int(input("Enter a number to divide by: "))

if num % 4 == 0:
    print(f"The number {num} is a multiple of 4.")
elif num % 2 == 0:
    print(f"The number {num} is an even number.")
else:
    print(f"The number {num} is an odd number.")

if num % check == 0:
    print(f"The number, {num}, divides evenly by the number, {check}.")
else:
    print(f"The number, {num}, does not divide evenly by the number, {check}.")