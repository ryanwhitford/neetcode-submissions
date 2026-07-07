class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxf = 0
        res = 0
        for r, c in enumerate(s):
            freq[c] = 1 + freq.get(c,0)
            maxf = max(maxf, freq[c])
            while r-l+1 - maxf > k:
                freq[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res