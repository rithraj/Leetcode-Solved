class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2 + l

        while l < r:
            mid = (r - l) // 2 + l
            print(l, r, mid)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]
