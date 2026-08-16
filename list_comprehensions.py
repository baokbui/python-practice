# Problem: One line of python that makes a new list with only even numbers
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Solution:
aEven = [num for num in a if num % 2 == 0]
print(aEven)