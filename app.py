import os
import streamlit as st
from recommender import MovieRecommender

# Page config
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")

# Load recommender
BASE = os.path.dirname(__file__)
MOVIES_CSV = os.path.join(BASE, 'movies.csv')
RATINGS_CSV = os.path.join(BASE, 'ratings.csv')

@st.cache_resource
def load_recommender():
    return MovieRecommender(MOVIES_CSV, RATINGS_CSV)

recommender = load_recommender()

# Sidebar navigation
tab1, tab2 = st.tabs(["👤 Recommend for User", "🎥 Find Similar Movies"])

with tab1:
    st.header("Get Recommendations for a User")
    col1, col2 = st.columns(2)
    
    with col1:
        user_id = st.number_input("Enter User ID (1-610):", min_value=1, max_value=610, value=1)
    
    with col2:
        n_recs = st.slider("Number of recommendations:", 1, 20, 10)
    
    if st.button("Get Recommendations", key="user_btn"):
        recs = recommender.recommend_for_user(user_id, n_recs)
        if recs:
            st.success(f"Top {len(recs)} recommendations for User {user_id}:")
            for i, rec in enumerate(recs, 1):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"{i}. **{rec['title']}**")
                with col2:
                    st.metric("", f"{rec['score']:.3f}")
        else:
            st.warning("No recommendations found for this user.")

with tab2:
    st.header("Find Movies Similar to Your Favorite")
    col1, col2 = st.columns(2)
    
    with col1:
        movie_title = st.text_input("Enter movie title:", placeholder="e.g., Toy Story")
    
    with col2:
        n_similar = st.slider("Number of similar movies:", 1, 20, 10, key="similar_slider")
    
    if st.button("Find Similar Movies", key="movie_btn"):
        if movie_title:
            similar = recommender.similar_movies(movie_title, n_similar)
            if similar:
                st.success(f"Movies similar to **{movie_title}**:")
                for i, sim in enumerate(similar, 1):
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.write(f"{i}. **{sim['title']}**")
                    with col2:
                        st.metric("", f"{sim['score']:.3f}")
            else:
                st.error(f"Movie '{movie_title}' not found. Try another title!")
        else:
            st.warning("Please enter a movie title.")

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **How it works:**\n\n"
    "This system uses **Collaborative Filtering** to:\n\n"
    "- Recommend movies for users based on similar users' ratings\n"
    "- Find similar movies based on who rated them\n\n"
    "Try searching for popular movies like:\n"
    "Toy Story, Matrix, Avatar, Inception, Star Wars"
)
