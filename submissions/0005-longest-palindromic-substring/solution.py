class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_list = []
        len_list = []
        ps = ''
        maximum = 0
        for si in range(len(s)):
            for ei in range(si, len(s)):
                ps = s[si:ei+1]
                if ps == ps[::-1]:
                    str_list.append(ps)
                    len_list.append(len(ps))
        if len(len_list) == 0:
            return s
        else:
            return (str_list[len_list.index(max(len_list))])
