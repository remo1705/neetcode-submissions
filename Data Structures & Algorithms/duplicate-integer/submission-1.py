class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)): 
            new_nums = nums[i+1:]
            if nums[i] in new_nums:
                return True
        return False