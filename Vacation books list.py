pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())
total_time = pages / pages_per_hour
needed_hours_per_day = total_time / days_per_book
print(round(needed_hours_per_day))
