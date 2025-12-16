def pivot_index(nums):
    total_sum = sum(nums)  # Calculate the total sum of the array elements
    
    left_sum = 0
    # Iterate through the array to find the pivot index
    for i in range(len(nums)):
        # The right sum for index i is total_sum minus left_sum minus nums[i]
        right_sum = total_sum - left_sum - nums[i]

        # If left sum equals right sum, we've found the pivot index
        if left_sum == right_sum:
            return i

        # Update the left sum for the next iteration
        left_sum += nums[i]

    # If no pivot index is found, return -1
    return -1

# Example usage
nums1 = [1, 7, 3, 6, 5, 6]
nums2 = [1, 2, 3]
nums3 = [2, 1, -1]

print("Pivot Index of nums1:", pivot_index(nums1))  # Expected output: 3
print("Pivot Index of nums2:", pivot_index(nums2))  # Expected output: -1
print("Pivot Index of nums3:", pivot_index(nums3))  # Expected output: 0
