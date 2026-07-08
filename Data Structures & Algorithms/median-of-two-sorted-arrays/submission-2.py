class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            #i+j+2 = (len(A)+len(B))//2
            j = (len(A)+len(B))//2 - i - 2
            AL = A[i] if i>=0 else float('-infinity')
            AR = A[i+1] if i<len(A)-1 else float('infinity')
            BL = B[j] if j>=0 else float('-infinity')
            BR = B[j+1] if j<len(B)-1 else float('infinity')
            if AL > BR:
                r=i-1
            elif AR < BL:
                l=i+1
            else:
                if (len(A)+len(B))%2:
                    return min(AR, BR)
                else:
                    return (max(AL, BL) + min(AR, BR))/2



