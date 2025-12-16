def binary_search(numbers, target):
    left_index = 0
    right_index = len(numbers) - 1
    mid_index = (right_index - left_index) // 2
    
    while numbers[mid_index] != target:
        if numbers[mid_index] == target:
            return [mid_index]
        
        if numbers[mid_index] > target:
            right_index = mid_index
        
        if numbers[mid_index] < target:
            left_index = mid_index
        
        if right_index == left_index:
            return [-1]
        
        mid_index = left_index + (right_index - left_index) // 2
    
    return [mid_index]

def main():
    arr = [2, 4, 9, 10, 11, 22, 24, 31, 48, 56, 76, 86]
    x = 10
    result = binary_search(arr, x)
    
    if result[0] == -1:
        print(f"No found index of {x}")
    else:
        print(f"The index of element is {result[0]}")

if __name__ == "__main__":
    main()
