class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_list = []
        maximum = 0
        for character in s:
            if character in char_list:
                maximum = max(maximum,len(char_list))
                char_list = char_list[char_list.index(character)+1:]
                char_list.append(character)
            else:
                char_list.append(character)

        return max(maximum, len(char_list))
