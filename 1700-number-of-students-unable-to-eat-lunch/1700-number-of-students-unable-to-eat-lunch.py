class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unable_to_eat = 0
        iterations = 0
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                unable_to_eat = 0
            else:
                students.append(students.pop(0))
                unable_to_eat += 1

            iterations += 1
            if unable_to_eat == len(students):
                break

        return len(students)
        
                
        