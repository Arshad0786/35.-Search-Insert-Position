class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if(nums[i] == target):
                return i
            if(nums[i] > target):
                return i
            if(i == len(nums) - 1):
                return i + 1
