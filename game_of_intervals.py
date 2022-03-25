number_of_moves = int(input())
final_result = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for i in range (number_of_moves):
    number = int(input())
    if 0 <= number <= 9:
        from_0_to_9 += 1
        final_result += number * 0.2
    elif 10 <= number <= 19:
            from_10_to_19 += 1
            final_result += number * 0.3
    elif 20 <= number <= 29:
            from_20_to_29 += 1
            final_result += number * 0.4
    elif 30 <= number <= 39:
            from_30_to_39 += 1
            final_result += 50
    elif 40 <= number <= 50:
            from_40_to_50 += 1
            final_result += 100
    elif number < 0 or number > 50:
        invalid_numbers += 1
        final_result = final_result / 2

percent_from_0_to_9 = from_0_to_9 / number_of_moves * 100
percent_from_10_to_19 = from_10_to_19 / number_of_moves * 100
percent_from_20_to_29 = from_20_to_29 / number_of_moves * 100
percent_from_30_to_39 = from_30_to_39 / number_of_moves * 100
percent_from_40_to_50 = from_40_to_50 / number_of_moves * 100
percent_invalid_numbers = invalid_numbers / number_of_moves * 100

print(f"{final_result:.2f}")
print(f"From 0 to 9: {percent_from_0_to_9:.2f}%")
print(f"From 10 to 19: {percent_from_10_to_19:.2f}%")
print(f"From 20 to 29: {percent_from_20_to_29:.2f}%")
print(f"From 30 to 39: {percent_from_30_to_39:.2f}%")
print(f"From 40 to 50: {percent_from_40_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")



