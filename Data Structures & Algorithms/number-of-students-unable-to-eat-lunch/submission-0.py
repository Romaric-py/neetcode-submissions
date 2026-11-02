class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        i = 0 # sandwich index
        n = len(students)

        while any(students[j] == sandwiches[i] for j in range(len(students))):
            if students[0] == sandwiches[i]:
                i += 1
                students = students[1:]
                n -= 1
            else:
                students = students[1:] + [students[0]]

        return n
        