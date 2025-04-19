class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        current_ptr = m+n-1
        m-=1
        n-=1
        while n>-1 and m>-1:
            if nums2[n]>nums1[m]:
                nums1[current_ptr]=nums2[n]
                n-=1
            else:
                nums1[current_ptr]=nums1[m]
                m-=1
            current_ptr-=1
        
        if m==-1:
            for idx in range(n+1):
                nums1[idx]=nums2[idx]