def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]

numbers = [10, 25, 7, 40, 15]
print(second_largest(numbers))
