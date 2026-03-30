class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        subarray_cnt = 0
        total = 0
        sum_dict = {}
        sum_dict[0]=1
        for element in nums:
            total+=element
            if total-k in sum_dict:
                subarray_cnt+=sum_dict[total-k]
            if total in sum_dict:
                sum_dict[total]+=1
            else:
                sum_dict[total]=1
        
        return subarray_cnt

                
