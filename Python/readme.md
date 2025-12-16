# 🧠 Python Algorithms

This repository contains Python implementations of essential algorithms, focusing on sorting and searching techniques. The current algorithms included are:

## 📚 Table of Contents

1. [Merge Sort](#-merge-sort)
2. [Binary Search](#-binary-search)
3. [Prefix Sum](#-prefix-sum)
4. [Linked List](#-linked-list)
5. [Stack](#-stack)
6. [Queue](#-queue)
7. [Sliding Window](#-sliding-window)
8. [Prerequisites](#-prerequisites)

---
 
## ⚡ Merge Sort

Merge Sort is a classic Divide and Conquer algorithm introduced by *John von Neumann* in 1945.  
It recursively splits an array into halves, sorts each half, and then merges them back together in sorted order.

### 🧩 Key Features

Property                    | Description 
----------------------------|---------------------------------------------------
**Time Complexity**          | O(n log n)
**Space Complexity**         | O(n)
**Stability**                | ✅ Yes (preserves relative order of equal elements)

---
 
### 🔍 Implementation Steps
 
#### 1️⃣ Divide the Array:
   - Split the array into two halves using the middle index.  
   ```python
      middle = (left + right) // 2
      left: starting index
      right: ending index
   ```

#### 2️⃣ Recursively Sort Each Half:
   - Sort the left half:
   ```python
      merge_sort(arr, left, middle)
   ```
   - Sort the right half:
   ```python
      merge_sort(arr, middle + 1, right)
   ```

#### 3️⃣ Merge the Sorted Halves:
   - Combine the two sorted halves into one sorted array:  
   ```python
      merge(arr, left, middle, right)
   ```

#### 4️⃣ Merge Sort Template:  
```python
def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    L = arr[left:middle + 1]
    R = arr[middle + 1:right + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)

def print_array(arr):
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original Array:")
    print_array(arr)
    
    merge_sort(arr, 0, len(arr) - 1)

    print("\nSorted Array:")
    print_array(arr)
Output:
# Original Array:
38 27 43 3 9 82 10

# Sorted Array:
3 9 10 27 38 43 82
```

## ⚡ Binary Search

Binary Search efficiently finds an element’s position in a sorted array by repeatedly dividing the search space in half.
📘 Tip: Binary Search only works on sorted data.

### 🧩 Key Features

Property | Description
----------------------------|---------------------------------------------------
Time Complexity | O(log n)
Space Complexity | O(1)
Applicability | Requires a sorted array

### 🧠 Implementation Steps
#### 1️⃣ Set the Initial Boundaries:
Initialize two pointers — left and right — representing the search boundaries.
At the start:
python
Copy code
left = 0
right = len(arr) - 1
#### 2️⃣ Implement the Loop:
- Calculate the middle index of the current search interval:
middle = left + (right - left) // 2
- Compare the middle element with the target:
- If they are equal, return the middle index.
- If the middle element is less than the target, adjust the left boundary to middle + 1 (search in the right half).
- If the middle element is greater than the target, adjust the right boundary to middle - 1 (search in the left half).
python
Copy code
while left <= right:
    middle = left + (right - left) // 2
    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        left = middle + 1
    else:
        right = middle - 1
#### 3️⃣ Return the Result:
If the loop ends without finding the target:
```python
      return -1; // ❌ Target not found
```
#### 4️⃣ Binary Search Template:
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    target = 7

    result = binary_search(arr, target)
    if result == -1:
        print("Element not found in the array.")
    else:
        print(f"Element found at index: {result}")
Output:
Element found at index: 3
```
