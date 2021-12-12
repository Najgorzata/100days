
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


max = student_scores[0]
for score in student_scores:
    for n in range(1, len(student_scores)):
        if student_scores[n]>=max:
            max=student_scores[n]
    
        

print(f"The highest score in the class is: {max}")   