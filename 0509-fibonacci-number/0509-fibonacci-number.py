class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        prev1 = self.fib(n - 1)
        prev2 = self.fib(n - 2)

        return prev1 + prev2