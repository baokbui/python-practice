# Printing out name, age, and year at 100 years old
name = input("Enter your name: ")
age = int(input("Enter you age: "))

currentYear = 2026
birthYear = currentYear - age
year_100 = birthYear + 100

print(f"Hello {name}! You are {age} years old and you will turn 100 at the year {year_100}!")