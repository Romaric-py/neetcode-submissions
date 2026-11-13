class Solution:

    def climbStairs(self, n: int) -> int:
        u0, u1 = 1, 1
        for i in range(1, n):
            u0, u1 = u1, u0 + u1
        return u1
        
        