# For loops in Python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#   print(fruit + " pie")

student_grades = [85, 90, 78, 92, 88]

total_exam_score = sum(student_grades)
print(total_exam_score)

sum = 0
for grade in student_grades:
    sum += grade
print(sum)

# Pick out the top grade
print(max(student_grades))

top_grade = 0
for grade in student_grades:
    if grade > top_grade:
        top_grade = grade
print(top_grade)

top_grade = 0
for grade in student_grades:
    top_grade = max(grade, top_grade)
print(top_grade)