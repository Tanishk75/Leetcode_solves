class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):

            currentWeight = 0
            daysNeeded = 1

            for weight in weights:

                if currentWeight + weight > capacity:
                    daysNeeded += 1
                    currentWeight = 0

                currentWeight += weight

            return daysNeeded <= days

        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = (left + right) // 2

            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left