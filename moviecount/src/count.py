import pandas as pd
from sklearn.ensemble import RandomForestRegressor


# Reading the file
movies = pd.read_csv('https://raw.githubusercontent.com/WittmannF/imdb-tv-ratings/master/top-250-movie-ratings.csv',header=0)

# Selecting relevant columns
movies = movies[['Title', 'Year', 'Rating', 'Rating Count']]

# Translating the rating count to integer
movies['Rating Count'] = movies['Rating Count'].map(lambda x: int(x.replace(',' , '')))

# Setting the title as index, as we won't use it for prediction
movies = movies.set_index('Title')

# Defining some constants given the problem statement 
movies_counted = [
    'Forrest Gump',
    'The Usual Suspects',
    'Rear Window',
    'North by Northwest',
    'The Secret in Their Eyes',
    'Spotlight'
]

counts = [
    10000000,
    7500000,
    6000000,
    4000000,
    3000000,
    1000000
]


X = movies.loc[movies_counted]
y = counts

# Applying a simple Random Forest regressor. Could of course be optimized thru hyperparameters 
reg = RandomForestRegressor().fit(X, y)

# Predict the count
movies['count_prediction'] = reg.predict(movies).round()

# Save to csv file
movies.to_csv('prediction.csv')
