class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # count_dict = {}
        # for element in nums:
        #     if element in list(count_dict.keys()):
        #         count_dict[element] = count_dict[element]+1
        #     else:
        #         count_dict[element]=1
        
        # for key,value in count_dict.items():
        #     if value==1:
        #         return key
        xoor = 0
        for element in nums:
            xoor^=element
            
        return xoor
