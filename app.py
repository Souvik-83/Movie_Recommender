import streamlit as st
import pickle
import pandas as pd
import numpy
import requests
def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=fc2bb868724c04a345d5df266faa806f".format(movie_id)
    data=requests.get(url)
    data=data.json()
    #st.text(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_sorted=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movie_posters=[]
    for i in movies_sorted:
        movie_id=movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
        #print(recommended_movie_posters)
    return recommended_movies,recommended_movie_posters

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie recommender system')
movies=pickle.load(open('movies.pkl','rb'))
movies_list=movies['title'].values
selected_movie_name = st.selectbox(
    'Please enter the name of the movie.',
    movies_list)
names=[]
posters=[]
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    #st.write(selected_movie_name)


    col1, col2, col3, col4, col5 = st.columns(5)
    #st.text(len(names))
    #st.text(len(posters))
    with col1:
        st.image(posters[0])
        st.write(names[0])

    with col2:
        st.image(posters[1])
        st.write(names[1])

    with col3:
        st.image(posters[2])
        st.write(names[2])

    with col4:
        st.image(posters[3])
        st.write(names[3])

    with col5:
        st.image(posters[4])
        st.write(names[4])

