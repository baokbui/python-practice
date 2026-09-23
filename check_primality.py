# Checks if the number is a prime or not
import math

def checkPrime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
        
    return True

number = int(input("Give me a number to check: "))
result = checkPrime(number)
if result:
    print(f"{number} is a prime number!")
else:
    print(f"{number} is not a prime number.")