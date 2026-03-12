class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums_set = sorted(set(nums))
        current = nums_set[0]
        maxLength = 1
        currentLength = 1
        for i in range(1,len(nums_set)):
            element = nums_set[i]
            if element == current+1:
                currentLength+=1
            else:
                maxLength = max(maxLength, currentLength)
                currentLength=1
            current = element
                
        return max(maxLength, currentLength)
            
