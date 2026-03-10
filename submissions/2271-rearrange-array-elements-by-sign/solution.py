class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0]*n
        posi = 0
        nega = 1
        for element in nums:
            if element>0:
                result[posi] = element
                posi+=2
            else:
                result[nega] = element
                nega+=2
            
        return result
