class Solution:
    def longestOnes(self, nums, k):
        zc=0
        l=0
        ml=float('-inf')
        for r in range(len(nums)):
            if nums[r]==0:
                zc+=1
            
            while zc>k:
                if nums[l]==0:
                    zc-=1
                l+=1
            ml=max(ml,r-l+1)
        return ml


            
