class Solution:
    def removeDuplicates(self, s: str) -> str:
        check_stack = []
        check_stack = []
        for element in s:
            check_stack.pop() if (len(check_stack)!=0 and element == check_stack[-1]) else check_stack.append(element)
        return ''.join(check_stack)
