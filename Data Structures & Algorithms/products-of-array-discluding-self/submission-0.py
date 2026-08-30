import math 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            new_nums = nums.copy()
            new_nums.pop(i)
            output.append(math.prod(new_nums))
        return output



        