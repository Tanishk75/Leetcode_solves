class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def time_taken(piles, k):
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k
            return time

        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            mid = (l + r) // 2
            hrs = time_taken(piles, mid)

            if hrs <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans