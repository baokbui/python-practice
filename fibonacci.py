def fibonacci(numbers):
    count = 1

    if numbers == 0:
        result = []
    elif numbers == 1:
        result = [1]
    elif numbers == 2:
        result = [1, 2]
    elif numbers > 2:
        result = [1, 1]
        while count < (numbers-1):
            result.append(result[count] + result[count-1])
            count += 1

    return result


print(fibonacci(10))