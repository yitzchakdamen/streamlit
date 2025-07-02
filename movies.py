import pandas as pd
import matplotlib.pyplot as plt



url = "https://raw.githubusercontent.com/danielgrijalva/movie-stats/refs/heads/master/movies.csv"
movies = pd.read_csv(url)

movies = movies.dropna()

avg_budget  = movies.groupby("genre")["budget"].mean().round()
avg_budget  = avg_budget.reset_index()

fig = plt.figure(figsize = (19, 10))
plt.style.use("classic")

plt.bar(avg_budget['genre'], avg_budget['budget'], color = "#f03c36", width=0.5)
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing the Average Budget of Movies in Each Genre')

