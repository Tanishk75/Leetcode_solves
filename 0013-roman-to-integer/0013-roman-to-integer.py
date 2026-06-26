class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        values = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }
        total=0
        for x in range(n):
            curr=values[s[x]]
            if x+1<n and curr< values[s[x+1]]:
                total-=curr
            else:
                total+=curr
        return total       