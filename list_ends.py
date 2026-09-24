def firstLast(numbers):
    new_list = []
    for i in range(0, len(numbers)):
        if i == 0 or i == len(numbers)-1:
            new_list.append(numbers[i])

    return new_list


a = [5, 10, 15, 20, 25]
result = firstLast(a)
print(result)
