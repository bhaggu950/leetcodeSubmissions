class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_set = set(nums)
        
        for element in nums_set:
            if nums.count(element) > int(len(nums)/2):
                return element
        
