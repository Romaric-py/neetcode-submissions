class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            freq = self.freq(s)
            if freq in groups:
                groups[freq].append(s)
            else:
                groups[freq] = [s]
        return list(groups.values())
    
    def freq(self, s: str) -> str:
        s_count = [0] * 26
        for i in s:
            idx = ord(i) - ord('a')
            s_count[idx] += 1
        return tuple(s_count)