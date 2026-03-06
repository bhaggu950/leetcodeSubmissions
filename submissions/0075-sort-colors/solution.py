class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min, min_idx = nums[i], i
            for j in range(i, len(nums)):
                if nums[j]<min:
                    min, min_idx = nums[j], j
                
            nums[i],nums[min_idx] = nums[min_idx], nums[i]
