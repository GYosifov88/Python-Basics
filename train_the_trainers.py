number_of_jury = int(input())
average_grade = 0
total_grade = 0
overall_grade = 0
presentation = 0
final_grade = 0
command = input()
while command != 'Finish':
    presentation += 1
    for num in range (number_of_jury):
        current_grade = float(input())
        total_grade += current_grade
        average_grade = total_grade / number_of_jury
    print(f"{command} - {average_grade:.2f}.")
    total_grade = 0
    overall_grade += average_grade

    command = input()
final_grade = overall_grade / presentation
print (f"Student's final assessment is {final_grade:.2f}.")




