class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1): return False
        k = len(s1)
        l=0
        count1 = Counter(s1)
        count2 = Counter(s2[:k-1])
        for l in range(len(s2)-len(s1)+1):
            r = l + k - 1
            count2[s2[r]] = 1 + count2.get(s2[r],0)
            if count1 == count2:
                return True
            count2[s2[l]]-=1
            l+=1
        return False


            