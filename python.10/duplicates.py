def remove_duplicates(numbers):
    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    return unique

numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))
