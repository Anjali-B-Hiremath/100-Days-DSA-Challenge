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
            return (nums3[total // 2 - 1]+nums3[total // 2])/2.0
