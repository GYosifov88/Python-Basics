number_of_groups = int(input())
mountain = ''
total_people = 0
total_per_musala = 0
total_per_monblan = 0
total_per_kilimandjaro = 0
total_per_k2 = 0
total_per_everest = 0
for i in range (number_of_groups):
    number_of_people_in_group = int(input())
    total_people += number_of_people_in_group
    if number_of_people_in_group <= 5:
        mountain == 'Musala'
        total_per_musala += number_of_people_in_group
    elif 6 <= number_of_people_in_group <= 12:
        mountain == 'Monblan'
        total_per_monblan += number_of_people_in_group
    elif 13 <= number_of_people_in_group <= 25:
        mountain == 'Kilimandjaro'
        total_per_kilimandjaro += number_of_people_in_group
    elif 26 <= number_of_people_in_group <= 40:
        mountain == 'K2'
        total_per_k2 += number_of_people_in_group
    elif  number_of_people_in_group >= 41:
        mountain == 'Everest'
        total_per_everest += number_of_people_in_group

total_per_musala_percent = total_per_musala / total_people * 100
total_per_monblan_percent = total_per_monblan / total_people * 100
total_per_kilimandjaro_percent = total_per_kilimandjaro / total_people * 100
total_per_k2_percent = total_per_k2 / total_people * 100
total_per_everest_percent = total_per_everest / total_people * 100

print (f'{total_per_musala_percent:.2f}%')
print (f'{total_per_monblan_percent:.2f}%')
print (f'{total_per_kilimandjaro_percent:.2f}%')
print (f'{total_per_k2_percent:.2f}%')
print (f'{total_per_everest_percent:.2f}%')