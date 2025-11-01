# 🧠 Java Algorithms

This repository contains Java implementations of essential algorithms, focusing on sorting and searching techniques. The current algorithms included are:

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

Original Array:
38 27 43 3 9 82 10 

Sorted Array:
3 9 10 27 38 43 82
```
![image](https://github.com/user-attachments/assets/542f7e1c-b49b-4304-abb4-3a9a0a737189)

---

## ⚡ Binary Search
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
Array: [1, 3, 5, 7, 9, 11]
Target: 7

Step 1: middle = 2 → arr[2] = 5 → target > 5 → move right
Step 2: middle = 4 → arr[4] = 9 → target < 9 → move left
Step 3: middle = 3 → arr[3] = 7 → ✅ found!

```

![image](https://github.com/user-attachments/assets/c50594c0-8f3b-45a6-8eba-a7535cb0e54b)

---

## ⚡ Two Pointers
The **Two Pointers** technique is a powerful approach commonly used to solve array and string problems efficiently.  
It involves using **two indices (pointers)** to iterate through data from either the same direction or opposite directions, reducing the need for nested loops.

### 🧩 Key Features
| Property | Description |
|-----------|--------------|
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) |
| **Approach Type** | Iterative (uses two moving pointers) |
| **Common Use Cases** | Pair sum, reverse array, remove duplicates, palindrome check |

### 🧠 Implementation Steps
#### 1️⃣ Initialize Two Pointers
Decide how your pointers will move:
   - **Opposite direction:** Start with one pointer at the beginning and one at the end.  
   - **Same direction:** Start both pointers at the beginning and move the second pointer ahead to form a sliding window.

Example initialization:
```java
   int left = 0;
   int right = arr.length - 1;
```
#### 2️⃣ Iterate While Condition Holds
   - Move the pointers based on the problem condition.
```java
   while (left < right) {
       int sum = arr[left] + arr[right];
   
       if (sum == target) {
           System.out.println("Pair found: (" + arr[left] + ", " + arr[right] + ")");
           break;
       } else if (sum < target) {
           left++;   // Increase sum
       } else {
           right--;  // Decrease sum
       }
   }
```
#### 3️⃣ Stop Condition
Stop when:
   - Pointers cross each other ``(left >= right)``, or
   - The required condition `(like sum == target)` is satisfied.

#### 4️⃣ Two Pointer Template:  
```java
public class TwoPointersExample {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 6};
        int target = 6;

        int left = 0, right = arr.length - 1;

        while (left < right) {
            int sum = arr[left] + arr[right];

            if (sum == target) {
                System.out.println("Pair found: (" + arr[left] + ", " + arr[right] + ")");
                return;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        System.out.println("No pair found.");
    }
}
Array: [1, 2, 3, 4, 6], Target = 6

Step 1: left=0 (1), right=4 (6) → sum=7 → too high → move right--
Step 2: left=0 (1), right=3 (4) → sum=5 → too low → move left++
Step 3: left=1 (2), right=3 (4) → sum=6 ✅ Found!

```
<img width="205" height="246" alt="image" src="https://github.com/user-attachments/assets/7bda6f7d-e388-427c-aabd-ba1ba4792072" />

---

## ⚡ Prefix Sum
The **Prefix Sum Algorithm** is a simple yet powerful technique used to efficiently calculate **the sum of elements in a subarray**.  
It precomputes cumulative sums so that each range sum query can be answered in **O(1)** time instead of recalculating from scratch every time.

> 📘 **Tip:** Prefix Sum is extremely useful in problems involving **range queries**, **subarray sums**, and **cumulative data analysis**.

### 🧩 Key Features

| Property | Description |
|-----------|--------------|
| **Time Complexity (Preprocessing)** | O(n) |
| **Time Complexity (Query)** | O(1) |
| **Space Complexity** | O(n) |
| **Approach Type** | Precomputation / Cumulative Sum |
| **Common Use Cases** | Range sum queries, subarray calculations, 2D matrix sums |

### 🧠 Implementation Steps
#### 1️⃣ Compute Prefix Sum Array
Given an array `arr[]`, create a new array `prefix[]` where:


```java
   prefix[i] = prefix[i - 1] + arr[i];

   //example:
   arr    = [2, 4, 6, 8, 10]
   prefix = [2, 6, 12, 20, 30]
```
#### 2️⃣ Use Prefix Sum to Calculate Range Sum
The sum of elements from index l to r can be found using:
```java
   sum(l, r) = prefix[r] - prefix[l - 1]
```

#### 3️⃣ Prefix Sum Template
```java
public class PrefixSumExample {
    public static void main(String[] args) {
        //Given an array. what is sum of range 1 to 3
        int[] arr = {2, 4, 6, 8, 10};
        int n = arr.length;

        int[] prefix = new int[n];
        prefix[0] = arr[0];

        // Step 1️⃣: Compute prefix sums
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + arr[i];
        }

        // Step 2️⃣: Answer range sum queries
        int l = 1, r = 3; // Example: sum of elements from index 1 to 3
        int rangeSum = prefix[r] - (l > 0 ? prefix[l - 1] : 0);

        System.out.println("Prefix Array: " + java.util.Arrays.toString(prefix));
        System.out.println("Sum from index " + l + " to " + r + " = " + rangeSum);
    }
}

Index:    0   1   2   3   4
Array:    2   4   6   8   10
Prefix:   2   6  12  20   30

Sum(1,3) = prefix[3] - prefix[0]
         = 20 - 2 = 18 ✅

```
<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/5479f706-f3d7-47ec-a366-459bf6648323" />

---

## ⚡ Linked List
A **Linked List** is a linear data structure in which elements (called **nodes**) are connected using **pointers** instead of being stored in contiguous memory like arrays.  
Each node contains **data** and a **reference (link)** to the next node in the sequence.

> 📘 **Tip:** Linked Lists are great for **dynamic memory allocation** and when you need **frequent insertions or deletions**.

---

### 🧩 Key Features

| Property | Description |
|-----------|--------------|
| **Structure Type** | Linear data structure (non-contiguous memory) |
| **Components** | `Node` (data + next pointer) |
| **Insertion/Deletion** | O(1) at head or tail (with reference) |
| **Access Time** | O(n) (must traverse from head) |
| **Variants** | Singly, Doubly, and Circular Linked Lists |
| **Memory Usage** | Extra memory for pointer(s) |

---
### 🧠 Implementation Steps

#### 1️⃣ Define a Node Class
Each node stores:
- The **data value**
- A reference to the **next node**

```java
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
```

#### 2️⃣ Linked List Template

```java
public class LinkedList {
    Node head;

    // Add a new node at the end
    public void append(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            return;
        }

        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    // Print all elements
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.append(10);
        list.append(20);
        list.append(30);

        System.out.println("Linked List:");
        list.printList();
    }
}
```
<img width="2768" height="1238" alt="image" src="https://github.com/user-attachments/assets/a848484e-9f66-4d84-a142-0817bd96b2fd" />

---

## ⚡ Stack
A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.  
This means the **last element added** to the stack will be the **first one removed**.  

> 📘 **Tip:** Think of a stack as a stack of plates — you can only take the top one off first.

---

### 🧩 Key Features

| Property | Description |
|-----------|--------------|
| **Structure Type** | Linear |
| **Access Order** | LIFO (Last In, First Out) |
| **Insertion / Deletion** | At the top only |
| **Time Complexity** | O(1) for `push()` and `pop()` |
| **Common Operations** | `push()`, `pop()`, `peek()`, `isEmpty()` |
| **Typical Use Cases** | Undo operations, expression evaluation, DFS, parentheses validation |

---

### 🧠 Implementation Steps

#### 1️⃣ Define a Stack Structure
You can use either:
- **Built-in Java Stack** (`java.util.Stack`), or  
- **Custom implementation** using an array or `LinkedList`.

Example using Java’s built-in class:
```java
import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        // Create a stack
        Stack<Integer> stack = new Stack<>();

        // Push elements
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Peek top element
        System.out.println("Top element: " + stack.peek());

        // Pop elements
        System.out.println("Popped: " + stack.pop());
        System.out.println("Popped: " + stack.pop());

        // Check if stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty());
    }
}
Step 1️⃣: push(10) → Stack: [10]
Step 2️⃣: push(20) → Stack: [10, 20]
Step 3️⃣: push(30) → Stack: [10, 20, 30]
Step 4️⃣: peek() → Top element: 30
Step 5️⃣: pop() → Popped 30 → Stack: [10, 20]
Step 6️⃣: pop() → Popped 20 → Stack: [10]
Step 7️⃣: isEmpty() → ❌ false (still has [10])

✅ Final Stack: [10]
```

<img width="545" height="361" alt="image" src="https://github.com/user-attachments/assets/5e61a1c6-6f97-40b5-be9f-7a8b5534eb88" />

---

## ⚡ Queue

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.  
It works just like a real-life queue — the first person to enter the line is the first to leave.

> 📘 **Tip:** Queue is ideal for managing tasks in order — such as processing requests, scheduling jobs, or buffering data.

---

### 🧩 Key Features

| Property | Description |
|-----------|--------------|
| **Order** | First In, First Out (FIFO) |
| **Insertion (Enqueue)** | Adds an element at the **rear (end)** |
| **Deletion (Dequeue)** | Removes an element from the **front** |
| **Time Complexity** | O(1) for enqueue/dequeue operations |
| **Common Implementations** | Array, Linked List, Priority Queue, Deque |
| **Applications** | Task scheduling, BFS traversal, caching, buffering |

---

### 🧠 Implementation Steps

#### 1️⃣ Define a Queue Structure
We can implement a queue using an array or a linked list.  
Below is a simple **array-based queue** implementation:

```java
public class Queue {
    private int[] arr;
    private int front, rear, size, capacity;

    // Constructor
    public Queue(int capacity) {
        this.capacity = capacity;
        arr = new int[capacity];
        front = 0;
        rear = -1;
        size = 0;
    }

    // Check if queue is full
    public boolean isFull() {
        return size == capacity;
    }

    // Check if queue is empty
    public boolean isEmpty() {
        return size == 0;
    }

    // Step 2️⃣: Enqueue - Add element to the rear
    public void enqueue(int item) {
        if (isFull()) {
            System.out.println("Queue is full!");
            return;
        }
        rear = (rear + 1) % capacity; // circular increment
        arr[rear] = item;
        size++;
        System.out.println(item + " enqueued to queue.");
    }

    // Step 3️⃣: Dequeue - Remove element from the front
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return -1;
        }
        int item = arr[front];
        front = (front + 1) % capacity; // circular increment
        size--;
        System.out.println(item + " dequeued from queue.");
        return item;
    }

    // Peek the front element
    public int peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return -1;
        }
        return arr[front];
    }

    // Display all elements
    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return;
        }
        System.out.print("Queue elements: ");
        for (int i = 0; i < size; i++) {
            System.out.print(arr[(front + i) % capacity] + " ");
        }
        System.out.println();
    }

    // Main method to test
    public static void main(String[] args) {
        Queue queue = new Queue(5);

        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        queue.display();

        queue.dequeue();
        queue.display();

        System.out.println("Front element: " + queue.peek());
    }
}
Queue capacity = 5

Step 1️⃣: enqueue(10) → Queue: [10]
Step 2️⃣: enqueue(20) → Queue: [10, 20]
Step 3️⃣: enqueue(30) → Queue: [10, 20, 30]
Step 4️⃣: display() → Output: Queue elements: 10 20 30
Step 5️⃣: dequeue() → Removed 10 → Queue: [20, 30]
Step 6️⃣: display() → Output: Queue elements: 20 30
Step 7️⃣: peek() → Front element = 20

✅ Final Queue State: [20, 30]
📍 Front = 20, Rear = 30, Size = 2
```

<img width="1082" height="384" alt="image" src="https://github.com/user-attachments/assets/34160dbe-440c-4f8a-821d-45853c9d2d31" />

---

## ⚡ Sliding Window

The **Sliding Window** technique is a powerful approach used to solve problems that involve **contiguous subarrays or substrings**.  

> 📘 **Tip:** Sliding Window is most effective when the problem involves **subsets of consecutive elements** (like subarrays or substrings).

---

### 🧩 Key Features

| Property | Description |
|-----------|--------------|
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) or O(k), depending on the problem |
| **Approach Type** | Iterative (dynamic window adjustment) |
| **Common Use Cases** | Maximum/Minimum sum subarray, longest substring, counting elements within range |

---

### 🧠 Implementation Steps

#### 1️⃣ Define the Window
Decide what your window represents (for example: **a fixed-length subarray** or **a variable-length substring**).  
Set two pointers:
```java
int left = 0;
int right = 0;
```
   - The window covers all elements between left and right.  
   - You’ll move right to expand the window and left to shrink it.

     
#### 2️⃣ Expand the Window
Increase right to include new elements into the current window:
```java
   currentSum += arr[right];
```

If the window size or condition exceeds the requirement (for example, window size > k), shrink it by moving left:
```java
   currentSum -= arr[left];
   left++;
```
#### 3️⃣ Update the Result

After each adjustment, update your desired result (e.g., maximum sum, count, or length):
```java
   maxSum = Math.max(maxSum, currentSum);
```

#### Sliding Window Template
```java
public class SlidingWindowExample {
    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 1, 3, 2};
        int k = 3;
        System.out.println("Maximum sum of subarray of size " + k + ": " + maxSumSubarray(arr, k));
    }

    public static int maxSumSubarray(int[] arr, int k) {
        int windowSum = 0, maxSum = 0;

        // Compute sum of first window
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }
        maxSum = windowSum;

        // Slide the window
        for (int right = k; right < arr.length; right++) {
            windowSum += arr[right] - arr[right - k]; // add new, remove old
            maxSum = Math.max(maxSum, windowSum);
        }

        return maxSum;
    }
Array: [2, 1, 5, 1, 3, 2]
k = 3

Step 1: Window [2, 1, 5] → sum = 8
Step 2: Window [1, 5, 1] → sum = 7
Step 3: Window [5, 1, 3] → sum = 9 ✅
Step 4: Window [1, 3, 2] → sum = 6

Maximum sum = 9

}
```

<img width="785" height="400" alt="image" src="https://github.com/user-attachments/assets/66aa8b98-d823-4ee3-9976-b539aae6b5f0" />

---

## 🧰 Prerequisites

To run the code, you need to have the following installed:

- Java Development Kit (JDK) 8 or higher
- Any Java IDE (e.g., IntelliJ IDEA, Eclipse) or a text editor with Java support (e.g., VS Code)
- [Road MAP](https://neetcode.io/roadmap)
