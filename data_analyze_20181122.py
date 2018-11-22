import pandas as pd
unames = ['user_id','gender', 'age','occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id','movie_id', 'rating','timstamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames, engine='python')

print(users[:5])
print(users[-5:])
print(ratings[:5])
print(ratings[-5:])
print(movies[:5])
print(moviess[-5:])

data = pd.merge( pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')

agegen_ratings = data.pivot_table(values='rating', index='title', columns=['gender', 'age'], aggfunc='mean')

gender_min = data.pivot_table(values='rating', index='title', columns='gender', aggfunc='min')

age_sum = data.pivot_table(values='rating', index='title', columns='age', aggfunc='sum')

zip_ave = data.pivot_table(values='rating', index='title', columns='zip', aggfunc='ave')


