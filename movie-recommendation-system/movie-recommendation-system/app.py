"""
Streamlit UI for the Movie Recommendation System.

Run with:
    streamlit run app.py
"""

import streamlit as st
from recommender import MovieRecommender

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")


@st.cache_resource
def load_engine():
    return MovieRecommender()


engine = load_engine()

st.title("🎬 Movie Recommendation System")
st.write(
    "A content-based recommender that suggests similar movies using "
    "genres, cast, director, and plot overview (TF-IDF + Cosine Similarity)."
)

movie_titles = engine.get_all_titles()
selected_movie = st.selectbox("Pick a movie you like:", movie_titles)

top_n = st.slider("How many recommendations?", min_value=3, max_value=10, value=5)

if st.button("Get Recommendations", type="primary"):
    results = engine.recommend(selected_movie, top_n=top_n)

    if not results:
        st.error("Sorry, couldn't find recommendations for that movie.")
    else:
        st.subheader(f"Because you liked '{selected_movie}':")
        for r in results:
            with st.container(border=True):
                st.markdown(f"**{r['title']}**  ·  similarity: `{r['similarity']}`")
                st.caption(r["genres"])
                st.write(r["overview"])

st.divider()
st.caption("Built with Python, pandas, scikit-learn, and Streamlit.")
