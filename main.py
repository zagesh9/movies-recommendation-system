import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movie_posters

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col1:
        st.image(posters[4])
        st.text(names[4])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col2:
        st.image(posters[5])
        st.text(names[5])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col3:
        st.image(posters[6])
        st.text(names[6])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col4:
        st.image(posters[7])
        st.text(names[7])