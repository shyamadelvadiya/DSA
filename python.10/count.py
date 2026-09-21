def count_element(numbers, element):
    count = 0

    for number in numbers:
        if number == element:
            count += 1

    return count

numbers = [1, 2, 2, 3, 2, 4]
print(count_element(numbers, 2))
