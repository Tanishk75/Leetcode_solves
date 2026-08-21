class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        curr=[]

        def backtrack(idx):
            if idx==len(nums):
                result.append(curr.copy())
                return
            #no
            backtrack(idx+1)

            #yes
            curr.append(nums[idx])
            backtrack(idx+1)

            #backtrack
            curr.pop()
        
        backtrack(0)

        return result


        