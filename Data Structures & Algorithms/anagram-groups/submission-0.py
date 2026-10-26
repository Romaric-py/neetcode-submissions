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
        s_count = {}
        for i in s:
            s_count[i] = s_count.get(i, 0) + 1
        return "".join([f"{k}{v}" for k, v in sorted(s_count.items())])