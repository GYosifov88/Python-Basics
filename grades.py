number_of_students = int(input())
average_grades = 0
top_grade_above_5 = 0
between_3_and_3_99 = 0
between_4_and_4_99 = 0
fails_between_2_and_2_99 = 0
for i in range (number_of_students):
    student_grade = float(input())
    average_grades +=student_grade
    if 2 <= student_grade <= 2.99:
        fails_between_2_and_2_99 += 1
    elif 3 <= student_grade <= 3.99:
        between_3_and_3_99 += 1
    elif 4 <= student_grade <= 4.99:
        between_4_and_4_99 += 1
    elif student_grade >= 5:
        top_grade_above_5 += 1

percent_top_students = top_grade_above_5 / number_of_students * 100
percent_between_4_and_4_99 = between_4_and_4_99 / number_of_students * 100
percent_between_3_and_3_99 = between_3_and_3_99 / number_of_students * 100
percent_fails_between_2_and_2_99 = fails_between_2_and_2_99 / number_of_students * 100
average_percent = average_grades / number_of_students




print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between_4_and_4_99:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between_3_and_3_99:.2f}%")
print(f"Fail: {percent_fails_between_2_and_2_99:.2f}%")
print(f"Average: {average_percent:.2f}")
