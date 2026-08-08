class Solution:
    def get_start(self, interval):
        return interval[0]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=self.get_start)

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged