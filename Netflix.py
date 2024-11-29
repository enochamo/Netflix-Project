# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filtering Data
netflix_subset = netflix_df[netflix_df['type'] == "Movie"]

# Checking for Release Year b/n 1990 & 2000
movies_1990s = netflix_subset[(netflix_subset['release_year'] >= 1990) & (netflix_subset['release_year'] < 2000)]

# Plotting The Data
plt.hist(movies_1990s['duration']) 
plt.title('1990 Decade Movies')
plt.xlabel('Duration')
plt.ylabel('Number of Movies')
plt.show()

duration = 100
# Subsetting movies_1990s into Action Movies
action = movies_1990s[movies_1990s['genre'] == 'Action']

# Creating a For Loop
short_movie_count = 0
for label, row in action.iterrows():
    if row['duration'] < 90:
        short_movie_count = short_movie_count + 1
    else :
        short_movie_count = short_movie_count

print(short_movie_count)