class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        # Base case
        if n < 0:
            return 0
        if n == 0:
            return 1

        count = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = count
        return count
        
        