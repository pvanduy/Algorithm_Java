# DC4 Codefights 2024 Solutions

## Table of Contents
1. [Challenge 1](#challenge-1)
2. [Challenge 2](#challenge-2)
3. [Challenge 3](#challenge-3)

---

## Challenge 1

### Problem Statement
Challenge 1: Card Collection
An is a big fan of collecting trading cards. He has a collection of `n` unique cards, each with a distinct ID. These cards are placed in numbered slots from 1 to n.

One day, An woke up to find that some of his cards had been swapped with duplicates of cards he already had. To identify the exact cards that were switched, An wants to find two indices, left and right, such that when he removes all cards between these indices (inclusive), the remaining cards will all have unique IDs.

Your task is to help An find the smallest possible size of the subarray from left to right that needs to be removed to ensure all remaining cards have unique IDs.

Simplified Explanation
Imagine An has a row of numbered cards. Some cards are in the wrong place, causing duplicates. An wants to find the shortest section of cards he can remove so that all the remaining cards are unique.

Example:

If An has cards with IDs [1, 2, 3, 2, 1, 4], he could remove the subarray [2, 3, 2], leaving [1, 1, 4]. This is not the smallest possible subarray. The smallest subarray to remove would be [2, 3], leaving [1, 1, 4].

Goal: Find the smallest subarray to remove so that all remaining cards have unique IDs.

Key points:

Each card has a unique ID.
Some cards might be in the wrong place (duplicates).
The goal is to find the shortest section of cards to remove to eliminate duplicates.
### Approach and Solution
The task can be solved using the **two-pointer technique** combined with a `Set` for efficient duplicate checking.

1. Use a pointer `right` to iterate from the end of the array backward, adding elements to a `Set` until a duplicate is found.
2. Use another pointer `left` to iterate from the start, stopping when a duplicate is found.
3. Depending on the overlap of duplicates between the segments defined by `left` and `right`, adjust the removal segment.

**Time Complexity**: `O(n)`  
**Space Complexity**: `O(n)`

### Java Implementation
```java
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n + 1];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
        int r = n - 1;
        int ans = Integer.MAX_VALUE;
        Set<Integer> s = new HashSet<>();
        while (r > 0 && !s.contains(a[r])) {
            s.add(a[r]);
            r--;
        }
        int l = 0;
        while (r < n) {
            r++;
            while (l < r && !s.contains(a[l])) {
                s.add(a[l]);
                l++;
            }
            ans = Math.min(ans, r - l);
            s.remove(a[r]);
        }
        System.out.println(ans);
    }
}
```
## Challenge 2
Problem Statement
Given a string s, find the minimum number of adjacent swaps required to reverse the string. For instance, to reverse "abbcda" to "adcbba", you can only swap adjacent characters.

Approach and Solution
The solution involves iterating through the string from left to right and processing characters based on their last occurrence.

Character Processing: For each character, find the rightmost index of that character that hasn't been processed yet.
Swap Calculation: Calculate the number of swaps needed to move the current character to its correct position in the reversed string. This is equal to the number of characters already processed that should appear after the current character in the reversed string.
Updating Count Array: After moving the character, update a count array to indicate that one more character has been processed for all subsequent indices.
Key Points
Inverse Pairs: The problem can be viewed as counting the number of inverse pairs in the string. An inverse pair occurs when a character a appears before another character b in the original string but should appear after b in the reversed string.
Fenwick Tree: To efficiently calculate the number of characters processed before a given index, a Fenwick Tree (Binary Indexed Tree) can be used. This data structure allows for both efficient updates and queries.
Time Complexity: Using a Fenwick Tree, the time complexity of the solution can be improved from O(n^2) to O(n log n).
Detailed Example
Consider the string "abbcda".

- 'a' at index 0: The last 'a' is at index 5. No swaps are needed, and we update the count for index 5.
- 'b' at index 1: The last 'b' is at index 2. No swaps needed. Update count for indices 2, 3, 4, and 5.
- 'b' at index 2: The last 'b' is at index 1. No swaps needed. Update count for indices 1, 2, 3, 4, and 5.
- 'c' at index 3: The last 'c' is at index 3. Two swaps are needed (as 2 characters before it have been processed). Update count for indices 3, 4, and 5.
- 'd' at index 4: The last 'd' is at index 4. Three swaps are needed. Update count for index 5.
- 'a' at index 5: No swaps needed. Update count for index 5.
The total number of swaps is 2 + 3 = 5.

Key Concepts:
Binary Indexed Tree (Fenwick Tree) for efficient updates and queries.
LIFO (Last In First Out) stack for tracking character indices.
**Time Complexity**: `O(n log n)`  
**Space Complexity**: `O(n)`
### Java Implementation
```java
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        char[] from = br.readLine().trim().toCharArray();
        Stack<Integer>[] stack = new Stack[26];

        for (int i = 0; i < 26; i++) {
            stack[i] = new Stack<>();
        }

        for (int i = 0; i < n; i++) {
            stack[from[i] - 'a'].push(i);
        }

        long ans = 0;
        BIT bit = new BIT(n);

        for (int i = 0; i < n; ++i) {
            int x = stack[from[i] - 'a'].pop();
            ans += bit.preSum(x);
            bit.update(x, 1);
        }

        System.out.println(ans);
    }

    // 1-indexed fenwick tree
    static class BIT {
        int n;
        int[] tree;

        BIT(int n) {
            this.n = n;
            tree = new int[n + 1];
        }

        void update(int idx, int val) {
            ++idx;
            while (idx <= n) {
                tree[idx] += val;
                idx += (idx & -idx);
            }
        }

        int preSum(int idx) {
            int ret = 0;
            ++idx;
            while (idx > 0) {
                ret += tree[idx];
                idx -= (idx & -idx);
            }
            return ret;
        }
    }
}
```

## Challenge 3
Problem Statement
In a video game, Mariomo needs to jump over stairs to score as many points as possible. The stairs have heights from 1 to n (all heights are unique) and are arranged in a random order.

To move and score points, in each turn, Mariomo needs to select a range of stairs from position left to position right (including both left and right), temporarily called the range [l,r]. Among these stairs, let max_pos[l,r] be the position of the highest stair in the range [l,r], similarly min_pos[l,r] is the position of the lowest stair in the range [l,r]. Then Mariomo will jump from the lowest stair to the highest in order from left to right, which means max_pos[l,r] must be greater than min_pos[l,r].

Help Mariomo count the number of feasible stair subsets [l, r] such that max_pos[l,r] > min_pos[l,r]. Note that only count the number of feasible intervals [l,r] even if the intervals can overlap partially, as long as it is uniquely identified by the corresponding pair l and r.

### Approach and Solution
Precompute the nearest smaller/larger values for each element on the left (lmi, lma) and right (rmi, rma) using monotonic stacks.

Traverse each index i:
Identify subarrays where the maximum position is after the minimum position.
Handle left- and right-dominant ranges separately to avoid overlap.
**Time Complexity**: `O(n)`  
**Space Complexity**: `O(n)`

Java Implementation
```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        solve();
    }

    static long ans = 0;

    public static void solve() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in), 32768);
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());

        int[] a = new int[n];
        int[] lmi = new int[n];
        int[] rmi = new int[n];
        int[] lma = new int[n];
        int[] rma = new int[n];

        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < n; ++i) {
            a[i] = Integer.parseInt(tokenizer.nextToken());
        }

        // push -1 to the stack for left bound, and push n for right bound
        // calculate lmi (nearest left minimum index)
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for (int i = 0; i < n; ++i) {
            while (stack.size() > 1 && a[i] < a[stack.peek()]) {
                stack.pop();
            }
            lmi[i] = stack.peek();
            stack.push(i);
        }

        // calculate lma (nearest left maximum index)
        stack.clear();
        stack.push(-1);
        for (int i = 0; i < n; ++i) {
            while (stack.size() > 1 && a[i] > a[stack.peek()]) {
                stack.pop();
            }
            lma[i] = stack.peek();
            stack.push(i);
        }

        // calculate rmi (nearest right minimum index)
        stack.clear();
        stack.push(n);
        for (int i = n - 1; i >= 0; --i) {
            while (stack.size() > 1 && a[i] < a[stack.peek()]) {
                stack.pop();
            }
            rmi[i] = stack.peek();
            stack.push(i);
        }

        // calculate rma (nearest right maximum index)
        stack.clear();
        stack.push(n);
        for (int i = n - 1; i >= 0; --i) {
            while (stack.size() > 1 && a[i] > a[stack.peek()]) {
                stack.pop();
            }
            rma[i] = stack.peek();
            stack.push(i);
        }

        // Main calculation
        for (int i = 0; i < n; ++i) {
            int lm = lma[i];
            int rm = rma[i];
            // left range dominant
            if (i - lm >= rm - i) {
                int cur = n;
                for (int j = i; j < rm; ++j) {
                    cur = Math.min(cur, lmi[j]);
                    ans += Math.max(0, cur - lm);
                }
            } else { // right range dominant
                int cur = i;
                for (int j = i; j > lm; --j) {
                    if (a[j] < a[cur]) {
                        cur = j;
                    }

                    if (cur != i) {
                        ans += Math.max(0, Math.min(rmi[cur], rm) - i);
                    }
                }
            }
        }
        System.out.println(ans);
    }
}

```
