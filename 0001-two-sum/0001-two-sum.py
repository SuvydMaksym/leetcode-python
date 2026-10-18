class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return seen[needed],index
            else:
                seen[num] = index
        return []
        