class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                if num + 1 in hashmap and num - 1 in hashmap:
                    hashmap[num] = (hashmap[num-1][0], hashmap[num+1][1])
                    hashmap[hashmap[num-1][0]] = hashmap[hashmap[num+1][1]] = hashmap[num]
                elif num + 1 in hashmap:
                    hashmap[num] = (num, hashmap[num+1][1])
                    hashmap[hashmap[num+1][1]] = hashmap[num]
                elif num - 1 in hashmap:
                    hashmap[num] = (hashmap[num-1][0], num)
                    hashmap[hashmap[num-1][0]] = hashmap[num]
                else:
                    hashmap[num] = (num, num)
        return max(b - a + 1 for a, b in hashmap.values())
      