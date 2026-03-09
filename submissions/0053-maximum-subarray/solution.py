class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = float('-inf')
        n = len(nums)
        total = 0
        for element in nums:
            total+=element
            if total>maximum:
                maximum = total
            if total<0:
                total = 0
                    
        return maximum
        
