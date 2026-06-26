class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        res=1
        for f in range(1,n):
            if nums[f]!=nums[s]:
                s+=1
                res+=1
                nums[s]=nums[f]
        return res
        