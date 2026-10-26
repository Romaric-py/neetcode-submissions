class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_nb_ones = 0
        current_nb = 0
        for num in nums:
            if num == 1:
                current_nb += 1
            else:
                max_nb_ones = max(current_nb, max_nb_ones)
                current_nb = 0
        return max(current_nb, max_nb_ones)