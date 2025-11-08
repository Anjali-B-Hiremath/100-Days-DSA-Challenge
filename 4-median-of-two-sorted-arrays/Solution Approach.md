## 📘 Problem Understanding
Given two sorted arrays `nums1` and `nums2`, the task is to return the median of the two sorted arrays combined.

If the total length is odd, return the middle element.  
If even, return the average of the two middle elements.

---

## 💡 Intuition
Since both arrays are sorted, the simplest way is to merge and sort them, then find the middle element(s).

---

## 🧠 Approach - Merge and Sort
1. Merge both arrays into one.
2. Sort the combined array.
3. If the total count is odd → return the middle element.  
   If even → return the average of the two middle elements.

