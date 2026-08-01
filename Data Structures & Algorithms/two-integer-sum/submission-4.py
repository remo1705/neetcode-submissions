class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = target - nums[i]; 
            if num not in hashmap.values():
                hashmap[i] = nums[i]
            else:
                return [nums.index(num), i]

