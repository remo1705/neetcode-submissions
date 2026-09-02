class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff, output = [], [], []
        for i in range(len(nums)):
            pref = nums[0: i]
            suff = nums[i+1:len(nums)]
            output.append(math.prod(pref) * math.prod(suff))
        return output