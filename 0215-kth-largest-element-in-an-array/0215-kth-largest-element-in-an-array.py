class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        n=len(nums)

        heap=nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num>heap[0]:
                heapq.heapreplace(heap,num)

        return heap[0]        