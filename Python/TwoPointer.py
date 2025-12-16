def twopointer(numbers, target):
    left_index = 0
    right_index = len(numbers) - 1

    # If the last element is less than the target, return an empty list
    if numbers[right_index] < target:
        return []

    # While loop to search for the target
    while numbers[left_index] != target and numbers[right_index] != target:
        if left_index < target:
            left_index += 1

        if right_index > target:
            right_index -= 1

        # If the target is found at the left index, return the index (1-based)
        if numbers[left_index] == target:
            return [left_index + 1]
        # If the target is found at the right index, return the index (1-based)
        elif numbers[right_index] == target:
            return [right_index + 1]

    return []

# Driver code
arr = [2, 4, 9, 10, 11, 22, 24, 31, 48, 56, 76, 86]
target = 56
target_index = twopointer(arr, target)
print(target_index)
