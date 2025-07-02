import streamlit as st
from movies import movies, fig


st.write("""
Average Movie Budget, Grouped by Genre
""")

st.pyplot(fig)

score_rating = movies['score'].unique().tolist()
genre_list = movies['genre'].unique().tolist()
year_list = movies['year'].unique().tolist()


with st.sidebar:
    st.write("Select a range on the slider (it represents movie score) to view the total number of movies in a genre that falls within that range ")

    new_score_rating = st.slider(label = "Choose a value:",min_value = 1.0,max_value = 10.0,value = (3.0,5.0))

    new_genre_list = st.multiselect('Choose Genre:', genre_list, default = ['Animation','Horror',  'Fantasy', 'Romance'])

    year = st.selectbox('Choose a Year', year_list, len(year_list) -1)

print(new_score_rating," ============= ", new_genre_list,"=============", year)

score_info = (movies['score'].between(*new_score_rating))

new_genre_year = (movies['genre'].isin(new_genre_list)) & (movies['year'] == year)


col1, col2 = st.columns([2,3])
with col1:
    st.write("""#### Lists of movies filtered by year and Genre """)
    dataframe_genre_year = movies[new_genre_year].groupby(['name',  'genre'])['year'].sum()
    dataframe_genre_year = dataframe_genre_year.reset_index()
    st.dataframe(dataframe_genre_year, width = 400)

with col2:
    st.write("""#### User score of movies and their genre """)
    rating_count_year = movies[score_info].groupby('genre')['score'].count()
    rating_count_year = rating_count_year.reset_index()
    figpx = px.line(rating_count_year, x = 'genre', y = 'score')
    st.plotly_chart(figpx)