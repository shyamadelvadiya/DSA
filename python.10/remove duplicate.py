def merge_lists(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(merge_lists(list1, list2))
