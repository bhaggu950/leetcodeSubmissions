class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for index,current_number in enumerate(nums):
            complement = target-current_number
            if complement in indices.keys():
                return [index,indices[complement]]
            indices[current_number] = index
        
        return None
