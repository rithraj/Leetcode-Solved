class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        def helperReverse(l, r, nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r - 1
        
        helperReverse(0, len(nums)-1, nums)
        helperReverse(0,k-1,nums)
        helperReverse(k,len(nums) -1, nums)
            