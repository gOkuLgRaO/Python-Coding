import heapq


def find_kth_largest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # Turn the first k elements into a heap

    # iterate over the remaining elements in the array
    for num in nums[k:]:
        if num > min_heap[0]:  # compare with the smallest element in the array
            heapq.heapreplace(min_heap, num)  # replace the smallest

    return min_heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))

"""
You are given an array of integers nums and an integer k. Your task is to find the kth largest element in the array.

Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Explanation: The 2nd largest element is 5.

A more efficient solution is to use a min-heap of size k. This approach doesn't require sorting the entire array and works well with large datasets.

Build a Min-Heap:

We maintain a heap of size k such that the smallest element in the heap is always at the root.
If we find a new number larger than the smallest in the heap, we replace the smallest element with the new number.
Final Result:

After processing the entire array, the root of the min-heap will be the k-th largest element.

Heapify: We take the first k elements from the array and turn them into a min-heap.
Iteration: We iterate through the remaining elements in the array, and for each element, we check if it is larger than the smallest element in the heap (i.e., the root). If it is, we replace the root with the new element using heapreplace() which maintains the heap property.
Result: After processing the entire array, the smallest element in the heap will be the k-th largest element in the original array.
Time Complexity for Min-Heap:
O(n log k): We maintain a heap of size k. Inserting or removing an element from the heap takes O(log k) time, and we do this for n elements.
"""
