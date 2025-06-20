class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = i

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in hashmap and hashmap[remainder] != i:
                return [i, hashmap[remainder]]

        return []
        