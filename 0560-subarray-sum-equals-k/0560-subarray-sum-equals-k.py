class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        curr = 0
        count = 0

        for i in range(len(nums)):
            curr += nums[i]
            complement = curr - k

            if complement in hashmap:
                count += hashmap[complement]

            hashmap[curr] = hashmap.get(curr, 0) + 1

        return count