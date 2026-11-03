class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq_students = self.get_freq(students)
        freq_sandwiches = self.get_freq(sandwiches)

        for s in sandwiches:
            if freq_students[s] > 0:
                freq_students[s] -= 1
            else:
                break
        
        return freq_students[0] + freq_students[1]


    def get_freq(self, li):
        freq = [0, 0]
        for k in li:
            freq[k] += 1
        return freq