class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)-1):
        #     remaining = target-nums[i]
        #     if remaining in nums[i+1:]:
        #         return [i, nums.index(remaining, i+1)]
                        
        # return [-1,-1]
        
        nums_with_index = [(num,idx) for idx,num in enumerate(nums)]
        nums_with_index.sort(key=lambda x:x[0])
        # nums.sort()
        
        left, right = 0, len(nums)-1
        while left<right:
            total = nums_with_index[left][0]+nums_with_index[right][0]
            if total==target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif total<target:
                left+=1
            else:
                right-=1
                
        return [-1,-1]
        
