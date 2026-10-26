class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count, t_count = {}, {}

        for i, j in zip(s, t):
            s_count[i] = 1 + s_count.get(i, 0)
            t_count[j] = 1 + t_count.get(j, 0)
        return s_count == t_count