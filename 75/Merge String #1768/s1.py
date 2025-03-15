class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n, m = len(word1), len(word2)
        min_len = min(n, m)  # Length of the shorter string
        max_len = max(n, m)  # Length of the longer string
        
        # Merge alternately up to the length of the shorter string
        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])
        
        # Append remaining characters from both strings
        res.append(word1[min_len:])  # Remaining part of word1 (if any)
        res.append(word2[min_len:])  # Remaining part of word2 (if any)
        
        return ''.join(res)
