class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_cnt = 0
        prefix_sum = 0
        prefix_occurence = {0:1}
        
        for num in nums:
            prefix_sum+=num
            
            if prefix_sum-k in prefix_occurence.keys():
                subarray_cnt+=prefix_occurence[prefix_sum-k]
            
            if prefix_sum in prefix_occurence.keys():
                prefix_occurence[prefix_sum] = prefix_occurence[prefix_sum] + 1
            else:
                prefix_occurence[prefix_sum] = 1
                
        return subarray_cnt
