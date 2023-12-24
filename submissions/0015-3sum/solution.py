class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pairs = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            low, high = i+1, len(nums)-1
            while low<high:
                target_sum = nums[i]+nums[low]+nums[high]
                if target_sum<0:
                    low+=1
                elif target_sum>0:
                    high-=1
                else:
                    current_pair = [nums[i],nums[low],nums[high]]
                    pairs.append(current_pair)
                    while low<high and nums[low]==nums[low+1]:
                        low+=1
                    while low<high and nums[high]==nums[high-1]:
                        high-=1
                    low+=1
                    high-=1
        return pairs
