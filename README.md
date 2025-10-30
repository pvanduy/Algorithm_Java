# 🧠 Java Algorithms

This repository contains Java implementations of essential algorithms, focusing on sorting and searching techniques. The current algorithms included are:

## 📚 Table of Contents

1. [Merge Sort](#-merge-sort)
2. [Binary Search](#-binary-search)
3. [Prerequisites](#-prerequisites)

---

## ⚡ Merge Sort

**Merge Sort** is a classic **Divide and Conquer** algorithm introduced by *John von Neumann* in 1945.  
It recursively splits an array into halves, sorts each half, and then merges them back together in sorted order.

### 🧩 Key Features

| Property | Description |
|-----------|--------------|
| **Time Complexity** | O(n log n) |
| **Space Complexity** | O(n) |
| **Stability** | ✅ Yes (preserves relative order of equal elements) |

---

### 🔍 Implementation Steps

#### 1️⃣ Divide the Array:
   - Split the array into two halves using the middle index.  
     ```java
        int middle = (l + r) / 2;
        l: starting index
        r: ending index
      ```

#### 2️⃣ Recursively Sort Each Half:
   - Sort the left half:
     ```java
        mergeSort(arr, l, middle);
     ```
   - Sort the right half:
      ```java
        mergeSort(arr, middle + 1, r);
     ```
#### 3️⃣ Merge the Sorted Halves
   - Combine the two sorted halves into one sorted array:  
      ```java
        merge(arr, l, middle, r);
     ```
#### 4️⃣ Merge Sort Template:  

```java
// MergeSort.java
public class MergeSort {

    // Main function to test the algorithm
    public static void main(String[] args) {
        int[] arr = {38, 27, 43, 3, 9, 82, 10};

        System.out.println("Original Array:");
        printArray(arr);

        mergeSort(arr, 0, arr.length - 1);

        System.out.println("\nSorted Array:");
        printArray(arr);
    }

    // Step 1️⃣: Divide the array recursively
    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            // Find the middle point
            int middle = (left + right) / 2;

            // Sort first and second halves
            mergeSort(arr, left, middle);
            mergeSort(arr, middle + 1, right);

            // Step 2️⃣: Merge the sorted halves
            merge(arr, left, middle, right);
        }
    }

    // Step 3️⃣: Merge two sorted subarrays into one
    public static void merge(int[] arr, int left, int middle, int right) {
        // Sizes of two subarrays to be merged
        int n1 = middle - left + 1;
        int n2 = right - middle;

        // Create temporary arrays
        int[] L = new int[n1];
        int[] R = new int[n2];

        // Copy data to temp arrays
        for (int i = 0; i < n1; ++i)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[middle + 1 + j];

        // Merge the temp arrays back into arr[l..r]
        int i = 0, j = 0;
        int k = left;

        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of L[] if any
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        // Copy remaining elements of R[] if any
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Utility function to print an array
    public static void printArray(int[] arr) {
        for (int value : arr)
            System.out.print(value + " ");
        System.out.println();
    }
}
```
![image](https://github.com/user-attachments/assets/542f7e1c-b49b-4304-abb4-3a9a0a737189)


## ⚡Binary Search
Binary Search efficiently finds an element’s position in a sorted array by repeatedly dividing the search space in half.  
📘 Tip: Binary Search only works on sorted data.  

### 🧩 Key Features
| Property             | Description               |
| -------------------- | ------------------------- |
| **Time Complexity**  | O(log n)                  |
| **Space Complexity** | O(1)                      |
| **Applicability**    | Requires a sorted array   |


### 🧠 Implementation Steps

#### 1️⃣ Set the Initial Boundaries
Initialize two pointers — `left` and `right` — representing the search boundaries.  
At the start:
   ```java
      int left = 0;
      int right = arr.length - 1;
   ```

#### 2️⃣ Implement the Loop
- Calculate the middle index of the current search interval:  `int middle = left + (right - left) / 2;`
   - Compare the middle element with the target:
        - If they are equal, return the middle index.
        - If the middle element is less than the target, adjust the left boundary to middle + 1 (search in the right half).
        - If the middle element is greater than the target, adjust the right boundary to middle - 1 (search in the left half).
```java
   while (left <= right) {
       int middle = left + (right - left) / 2; // Prevents overflow
   
       if (arr[middle] == target)
           return middle; // ✅ Found the element
       else if (arr[middle] < target)
           left = middle + 1;  // 🔍 Search in the right half
       else
           right = middle - 1; // 🔍 Search in the left half
   }
```
#### 3️⃣ Return the Result
If the loop ends without finding the target:  
   ```java
      return -1; // ❌ Target not found
   ```

#### 4️⃣ Binary Search Template:  
```java
public class BinarySearchExample {

    // Function to perform Binary Search
    public static int binarySearch(int[] arr, int target) {
        // Step 1: Set the initial boundaries
        int left = 0;
        int right = arr.length - 1;

        // Step 2: Implement the loop
        while (left <= right) {
            // Calculate the middle index (avoid overflow)
            int middle = left + (right - left) / 2;

            // Compare middle element with the target
            if (arr[middle] == target) {
                return middle; // ✅ Found the element
            }

            // If middle element is smaller, ignore left half
            if (arr[middle] < target) {
                left = middle + 1;
            }
            // If middle element is larger, ignore right half
            else {
                right = middle - 1;
            }
        }

        // Step 3: Return result if element not found
        return -1; // ❌ Target not found
    }

    // Main method to test the binary search
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9, 11};
        int target = 7;

        int result = binarySearch(arr, target);

        if (result == -1) {
            System.out.println("Element not found in the array.");
        } else {
            System.out.println("Element found at index: " + result);
        }
    }
}
```

![image](https://github.com/user-attachments/assets/c50594c0-8f3b-45a6-8eba-a7535cb0e54b)


## Prerequisites

To run the code, you need to have the following installed:

- Java Development Kit (JDK) 8 or higher
- Any Java IDE (e.g., IntelliJ IDEA, Eclipse) or a text editor with Java support (e.g., VS Code)
