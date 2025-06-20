# app.py
import streamlit as st
from reco_engine import ContentBasedRecommender

st.set_page_config(page_title="Personalized Reco System", layout="wide")

st.title("🎬 Content-Based Movie Recommendation System")

# Load the model
recommender = ContentBasedRecommender("D:\VS Code\projects\personalized reco system\data\movies.csv")

movie_list = recommender.movies['title'].values.tolist()

selected_movie = st.selectbox("Select a movie you like:", movie_list)

if st.button("Get Recommendations"):
    results = recommender.recommend(selected_movie, top_n=5)
    for _, row in results.iterrows():
        st.subheader(row['title'])
        st.markdown(f"🎭 *Genres*: {row['genres']}")
        st.markdown("---")
