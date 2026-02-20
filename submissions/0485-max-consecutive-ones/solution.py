class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxStreak = 0
        count = 0
        for element in nums:
            if element==1:
                count+=1
            else:
                maxStreak=max(maxStreak,count)
                count=0
        maxStreak=max(maxStreak,count)
        return maxStreak
