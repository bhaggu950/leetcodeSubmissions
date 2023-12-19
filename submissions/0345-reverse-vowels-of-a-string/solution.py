class Solution:
    def is_vowel(self,any_list:list):
        res = []
        for c in any_list:
            if c.lower() in ['a','e','i','o','u']:
                res.append(c)
        return res
        
    def reverseVowels(self, s: str) -> str:
        reverse = self.is_vowel(list(s))
        normal = list(s)
        for idx,char in enumerate(normal):
            if char.lower() in ['a','e','i','o','u']:
                normal[idx] = reverse.pop()
        return ''.join(normal)
