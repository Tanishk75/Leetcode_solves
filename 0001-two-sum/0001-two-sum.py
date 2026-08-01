class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        
        lookup={}

        for i in range(n):
            comp=target-nums[i]

            if comp in lookup:
                return [lookup[comp],i]
            
            lookup[nums[i]]=i