# 🧮 Median of Two Sorted Arrays

### 📘 Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

---

### 💡 Intuition
Since both arrays are sorted, the simple way is to **merge** them and then **sort** the combined array.  
Once sorted, the median can easily be found using the middle index.

---

### 🚀 Approach: Merge and Sort
1. Merge both arrays into a single array.  
2. Sort the merged array.  
3. Find the middle element(s).  
4. If total elements are odd → return the middle one.  
5. If even → return the average of the two middle values.  

---

### ⏱️ Complexity
- **Time Complexity:** O((m + n) × log(m + n))  
- **Space Complexity:** O(m + n)

---

### 🧠 Code (Python3)
```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the arrays into a single sorted array.
        nums3 = nums1 + nums2

        # Sort the merged array.
        nums3.sort()

        # Calculate the total number of elements in the merged array.
        total = len(nums3)

        if total % 2 == 1:
            # If the total number of elements is odd, return the middle element as the median.
            return float(nums3[total // 2])
        else:
            # If the total number of elements is even, calculate the average of the two middle elements as the median.
            return (nums3[total // 2 - 1] + nums3[total // 2]) / 2.0

