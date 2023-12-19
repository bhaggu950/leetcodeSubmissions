class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        minLength = min(len(word1),len(word2))
        for a,b in zip(word1,word2):
            merged+=f'{a}{b}'
        merged+=f'{word1[minLength:]}{word2[minLength:]}'
        return merged
