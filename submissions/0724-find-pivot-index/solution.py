class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        pre_sum = 0
        post_sum = 0
        idx = -1
        for i in range(1, len(nums)):
            pre[i] = pre_sum+nums[i-1]
            pre_sum+=nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            post[i] = post_sum+nums[i+1]
            post_sum+=nums[i+1]
            
        for i in range(len(nums)):
            if pre[i]==post[i]:
                return i
        
        return idx
