def forLoop(numbers):
    result = []
    for num in numbers:
        if num in result:
            continue
        else:
            result.append(num)
    return result

def sets(numbers): 
    result = set(numbers)   #Unordered and Unindexed (can't access like lists)
    return result

numbers = [1, 3, 4, 6, 3, 2, 2, 5, 7, 9, 1, 0, 8]
names = ["Michele", "Robin", "Sara", "Michele"]
print(forLoop(numbers))
print(sets(names))