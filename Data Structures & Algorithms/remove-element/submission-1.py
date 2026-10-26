class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        offset = 0
        count = 0
        for i in range(len(nums)):
            if nums[i+offset] == val:
                del nums[i+offset]
                offset -= 1
            else:
                count += 1
        return count