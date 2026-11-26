class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        best = 0
        for num in hashset:
            if num - 1 not in hashset:
                i = num
                while i in hashset:
                    i += 1
                if  (i - num) > best:
                    best = i - num
        return best
      