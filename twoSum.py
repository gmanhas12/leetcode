class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for x in range(i + 1, len(nums)):
                if target - nums[i] == nums[x]: 
                    return [i, x]
        return None 
