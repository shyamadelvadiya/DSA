def largest_element(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

numbers = [10, 25, 7, 40, 15]
print(largest_element(numbers))
