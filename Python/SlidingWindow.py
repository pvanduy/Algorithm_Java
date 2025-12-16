def max_sum(arr, k):
    array_len = len(arr)
    
    # n must be greater than k
    if array_len <= k:
        print("Invalid")
        return -1

    # Compute sum of the first window of size k
    max_sum = sum(arr[:k])

    # Compute sums of remaining windows by
    # removing the first element of the previous
    # window and adding the last element of
    # the current window.
    window_sum = max_sum
    for i in range(k, array_len):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(max_sum(arr, k))
