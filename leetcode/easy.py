"""Problem no1: Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target."""

class Solution:
    def twoSum(self, nums, target):
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i


s = Solution()          # create an object of the class
result = s.twoSum([2,7,11,15], 18)
print(result)           


# Problem no2: 