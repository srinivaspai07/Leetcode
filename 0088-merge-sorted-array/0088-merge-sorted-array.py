class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1 and nums2
        i, j = m - 1, n - 1
        # Initialize pointer for the end of nums1
        k = m + n - 1
        print(k)

        # Iterate from the end of nums1 and nums2 to merge them
        while i >= 0 and j >= 0:
            print(f"i is {i} and j is {j} and k is {k}")

            # Compare the elements of nums1 and nums2 and place the larger one at the end of nums1
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            # Move the pointer k towards the beginning of nums1
            k -= 1
        
            print(nums1)
        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
