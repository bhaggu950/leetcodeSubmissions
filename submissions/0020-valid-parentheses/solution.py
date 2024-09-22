class Solution:
    def isValid(self, s: str) -> bool:
        check_stack = []
        parantheses_dict =  {')':'(', '}':'{', ']':'['}
        for element in s:
            if element in parantheses_dict.values():
                check_stack.append(element)
            else:
                if len(check_stack) == 0:
                    return False
                popped_element = check_stack.pop()
                if popped_element == parantheses_dict.get(element):
                    continue
                else:
                    return False
        return True if len(check_stack)==0 else False
