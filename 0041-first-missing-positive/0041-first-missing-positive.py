class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        n=len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=1
        
        for i in range(n):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        for  i in range(n):
            if nums[i]>0:
                return i+1
        return n+1