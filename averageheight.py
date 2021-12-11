student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


sum = 0
for n in student_heights:
    sum = sum + n


number_of_students = 0
for n in student_heights:
    number_of_students += 1


average = sum / number_of_students
print(round(average))
