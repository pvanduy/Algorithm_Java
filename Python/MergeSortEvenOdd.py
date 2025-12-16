class MergeSortEvenOdd:

    # Merge two subarrays of arr[]
    # First subarray is arr[l..m]
    # Second subarray is arr[m+1..r]
    def merge(self, arr, l, m, r):
        # Find the sizes of two subarrays to be merged
        n1 = m - l + 1
        n2 = r - m

        # Create temporary arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temporary arrays L[] and R[]
        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        # Merge the temporary arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray
        while i < n1 and j < n2:
            # Check if both elements are even or both are odd
            if (L[i] % 2 == 0) and (R[j] % 2 == 0):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            elif (L[i] % 2 != 0) and (R[j] % 2 != 0):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            elif (L[i] % 2 == 0) and (R[j] % 2 != 0):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L[] if any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R[] if any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    # MergeSort function
    def sort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2  # Find the middle point

            # Recursively divide the array
            self.sort(arr, l, m)
            self.sort(arr, m + 1, r)

            # Merge the sorted halves
            self.merge(arr, l, m, r)

    # Function to print the array
    @staticmethod
    def print_array(arr):
        for i in arr:
            print(i, end=" ")
        print()

# Driver code to test the MergeSortEvenOdd
if __name__ == "__main__":
    arr = [3, 1, 2, 4]

    print("Original array:")
    MergeSortEvenOdd.print_array(arr)

    # Create an instance of MergeSortEvenOdd and call sort()
    ob = MergeSortEvenOdd()
    ob.sort(arr, 0, len(arr) - 1)

    print("Sorted array:")
    MergeSortEvenOdd.print_array(arr)
