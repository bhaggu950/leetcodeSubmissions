class Solution:
    def countSubstrings(self, s: str) -> int:
        i=1
        palindrome_cnt = 0
        while i<=len(s):
            start = 0
            while start+i<=len(s):
                substr = s[start:start+i]
                if substr==substr[::-1]:
                    palindrome_cnt+=1
                start+=1
            i+=1
        return palindrome_cnt
