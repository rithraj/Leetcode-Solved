class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num != 0:
                unique.add(num)

        return len(unique)
        


        