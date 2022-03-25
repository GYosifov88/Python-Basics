movie_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
tickets_price = float(input())
percent_for_theater = int(input())

total_tickets_sold = number_of_tickets * number_of_days
income = total_tickets_sold * tickets_price
theater_commision = income * percent_for_theater / 100

gain = income - theater_commision

print(f'The profit from the movie {movie_name} is {gain:.2f} lv.')