from collections import deque
class Solution:
    def countStudents(self, students, sandwiches):
        students = deque(students)
        while students:
            top = sandwiches[0]
            if students[0]==top:
                sandwiches.pop(0)
                students.popleft()
            else:
                student = students.popleft()
                students.append(student)
                if top not in students:
                    break 
        return len(students)
    
# class Solution:
#     def countStudents(self, students, sandwiches):

#         count0 = students.count(0)
#         count1 = students.count(1)

#         for sandwich in sandwiches:

#             if sandwich == 0:
#                 if count0 == 0:
#                     return count1
#                 count0 -= 1

#             else:
#                 if count1 == 0:
#                     return count0
#                 count1 -= 1

#         return 0

obj = Solution()
result = obj.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])
print(result)
            