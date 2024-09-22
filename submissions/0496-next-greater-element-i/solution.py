class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for number1 in nums1:
            higher = -1
            if nums2.index(number1)==len(nums2)-1:
                result.append(-1)
                continue
            for element in nums2[nums2.index(number1):]:
                if element>number1:
                   higher=element
                   break
            result.append(higher)
        return result
