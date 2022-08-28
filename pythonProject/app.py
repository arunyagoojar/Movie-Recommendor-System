import pickle
import streamlit as st
import requests
import base64

st.set_page_config(layout="wide")
page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://assets.nflxext.com/ffe/siteui/vlv3/3a073c5f-0160-4d85-9a42-6f59aa4b64b9/ce862595-09a3-4fbf-b41c-76386c05f759/IN-en-20220718-popsignuptwoweeks-perspective_alpha_website_large.jpg");
  background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
streamlit_style = """
			<style>
			@import url('https://fonts.google.com/specimen/Oswald');
https://fonts.google.com/specimen/Oswald
			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:13]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.markdown("<h1 style='text-align: center; '>Movie Recommender System</h1>", unsafe_allow_html=True)
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.subheader(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.subheader(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.subheader(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.subheader(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

    with col6:
        st.subheader(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.subheader(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])

    with col8:
        st.subheader(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])

    col9, col10, col11, col12 = st.columns(4)
    with col9:
        st.subheader(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col10:
        st.subheader(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
    with col11:
        st.subheader(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])
    with col12:
        st.subheader(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])
