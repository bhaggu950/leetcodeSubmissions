class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        input_length = len(nums)
        sums = [sum(nums[idx:idx+k]) for idx in range(input_length-k+1)]
        left = [0] * len(sums)
        right = [0] * len(sums)
        best = 0
        for idx in range(input_length-k+1):
            if sums[idx]>sums[best]:
                best = idx
            left[idx] = best
        
        best = len(sums)-1
        for i in range(len(sums)-1, -1, -1):
            if sums[i]>=sums[best]:
                best=i
            right[i] = best
        
        max_sum = 0
        result = []
        for j in range(k, len(sums)-k):
            i, l = left[j-k], right[j+k]
            curr_sum = sums[i] + sums[j] + sums[l]
            if curr_sum > max_sum:
                max_sum = curr_sum
                result = [i, j, l]
        return result
