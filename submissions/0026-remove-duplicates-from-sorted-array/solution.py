class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        key = nums[0]
        j=1
        for i in range(1,len(nums)):
            if nums[i]==key:
                continue
            else:
                key = nums[i]
                nums[j] = nums[i]
                j+=1
        return j
