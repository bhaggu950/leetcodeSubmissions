class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count_dict = {}
        n = len(nums)
        for element in nums:
            count_dict[element] = count_dict.get(element, 0)+1
        
        result = []
        for key,value in count_dict.items():
            if value>(n/3):
                result.append(key)
        
        return result
