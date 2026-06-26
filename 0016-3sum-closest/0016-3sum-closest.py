class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        t=target
        close=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                curr=nums[i]+nums[l]+nums[r]
                if abs(curr-t)<abs(close-t):
                    close=curr
                if curr==t:
                    break
                elif curr<t:
                    l+=1
                else:
                    r-=1
        
        return close

