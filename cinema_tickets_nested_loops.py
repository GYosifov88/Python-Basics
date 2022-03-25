total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

command = input()
while command != 'Finish':
    free_spaces = int(input())
    total_spaces = free_spaces
    sold_tickets = 0
    ticket_type = input()
    while ticket_type != 'End':
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
        total_tickets+=1
        sold_tickets+=1
        free_spaces -= 1
        if free_spaces <=0:
            break
        ticket_type = input()
    percent_hall_per_movie = sold_tickets / total_spaces * 100
    print (f'{command} - {percent_hall_per_movie:.2f}% full.')


    command = input()

percent_student_tickets = student_tickets / total_tickets * 100
percent_standard_tickets = standard_tickets / total_tickets * 100
percent_kid_tickets = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")
