import sys
number_of_movies = int(input())
higher_rating = -sys.maxsize
lower_rating = sys.maxsize
total_rating = 0
top_movie_rating = ''
low_movie_rating = ''
for i in range (number_of_movies):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > higher_rating:
        higher_rating = movie_rating
        top_movie_rating = movie_name
    if movie_rating < lower_rating:
        lower_rating = movie_rating
        low_movie_rating = movie_name

average_rating = total_rating / number_of_movies

print (f'{top_movie_rating} is with highest rating: {higher_rating:.1f}')
print (f'{low_movie_rating} is with lowest rating: {lower_rating:.1f}')
print (f'Average rating: {average_rating:.1f}')

