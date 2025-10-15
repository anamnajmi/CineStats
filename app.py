#app.py
import streamlit as st
import pandas as pd

# Loading Dataset
df = pd.read_csv("Raw Data/movies.csv")
# Title
st.title("CineStats - Movie Recommendation")

# User Input
movie_title = st.text_input("Enter a movie title:")
if st.button("Search"):
    if movie_title in df['title'].values:
        # Get the selected movie
        movie = df[df['title'] == movie_title].iloc[0]
        st.markdown("---")

        # Display movie details
        st.markdown(f"[![poster]({movie['link']})]({movie['link']})")
        st.subheader(movie['title'])
        rating = movie['rating']
        stars = int(round(rating / 2))
        star_display = "★" * stars + "☆" * (5 - stars)
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown(f"**Genre**\n{movie['genre']}")
        col2.markdown(f"**Director**\n{movie['director']}")
        col3.markdown(f"**Year**\n{movie['year']}")
        col4.markdown(f"**IMDB Rating**\n{star_display}")
        st.markdown(f"**Description:** {movie['description']}")

        st.markdown("---")

        # Review
        st.markdown("### 💬 Reviews")
        for r in movie['reviews'].split(";"):
            st.markdown(f"- {r.strip()}")

        # Genre-Director based Recommendation
        st.markdown("---")
        st.markdown("### 🎥 Anam's Recommendation")
        similar = df[
            ((df['genre'] == movie['genre']) | (df['director'] == movie['director'])) &
            (df['title'] != movie_title)
            ].head(5)

        if not similar.empty:
            for s in similar['title']:
                st.markdown(f"- {s}")
        else:
            st.info("No similar movies found.")
    else:
        st.error("Movie not found in dataset.")