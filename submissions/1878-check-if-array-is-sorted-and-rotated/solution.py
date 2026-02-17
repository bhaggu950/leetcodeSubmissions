class Solution:
    def check(self, nums: List[int]) -> bool:
        al = len(nums)
        if al in [0,1]:
            return True
        
        original_array = nums.copy()
        nums.sort()
        if original_array == nums:
            return True
        
        for i in range(0, al):
            # print(i)
            # print(nums)
            if (nums[al-i:al+1]+nums[0:al-i]) == original_array:
                return True
                
        return False
        # return sorted_array == nums
