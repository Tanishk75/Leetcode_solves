class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        longest=0

        for num in hashset:
            if num-1 not in hashset:
                curr=num
                length=1
                while curr+1 in hashset:
                    curr+=1
                    length+=1
                
                longest=max(longest,length)


        return longest