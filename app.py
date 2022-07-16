import bz2
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f17017cf9ab19e407243ae287d90f746&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distnaces = similarity[movie_index]
    movies_list = sorted(list(enumerate(distnaces)), reverse=True, key=lambda x: x[1])[1:17]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters, 

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
ifile = bz2.BZ2File("similarity.pkl",'rb')
similarity = pickle.load(ifile)
ifile.close()


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select One Movie',
    movies['title'].values
)
    


if st.button('Recommend'):
    names, posters  = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 , col6 , col7 ,col8 = st.columns(8)
    with col1:
        st.text(names[0])   
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col1:
        st.text(names[8])   
        st.image(posters[8])
    with col2:
        st.text(names[9])
        st.image(posters[9])
    with col3:
        st.text(names[10])
        st.image(posters[10])
    with col4:
        st.text(names[11])
        st.image(posters[11])
    with col5:
        st.text(names[12])
        st.image(posters[12])
    with col6:
        st.text(names[13])
        st.image(posters[13])
    with col7:
        st.text(names[14])
        st.image(posters[14])
    with col8:
        st.text(names[15])
        st.image(posters[15])
