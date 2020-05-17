class Solution:
    def searchInsert(self, nums, target):
        if(target > nums[len(nums)-1]):
            return len(nums)
        upperBound = len(nums) - 1
        lowerBound = 0
        while(upperBound >= lowerBound):
            middleIndex = (upperBound + lowerBound) // 2
            if(nums[middleIndex] > target):
                upperBound = middleIndex - 1
            elif (nums[middleIndex] < target):
                lowerBound = middleIndex + 1
            else:
                return middleIndex
        return lowerBound


