# Last updated: 5/14/2025, 7:11:53 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(A) + len(B)
        if len(A) > len(B):
            A, B = B, A
            
        half = total / 2
        l, r = 0, len(A) - 1
        while True:
            i = l + r
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if i+1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if j+1 < len(B) else float('infinity')
            
            if(Aleft <= Bright and Bleft <= Aright):
                if total % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / float(2)
            
            elif Aleft > Bright:
                r -= 1
            else:
                l += 1
        return None
