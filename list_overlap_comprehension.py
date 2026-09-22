# Makes two random list and prints a list with numbers the two lists have in common
import random

a = random.sample(range(25), 12)
b = random.sample(range(25), 10)

result = [i for i in a if i in b]
print(result)