import streamlit as st
import mysql.connector
from database import getCast, updateRating

def main():
    if st.session_state.user:
        if st.session_state.movie:
            # st.info(st.session_state.movie)
            st.header(st.session_state.movie[1] + " (" + str(st.session_state.movie[4]) + ")")
            st.subheader("Genre - "+st.session_state.movie[5])
            st.write(st.session_state.movie[2])
            st.subheader('[Watch here](https://www.netflix.com/)')
            casts = getCast(st.session_state.movie[0])
            st.subheader("Cast")
            for cast in casts:
                # st.info(cast)
                st.write(cast[0])
            st.subheader("Rating")
            st.write(st.session_state.movie[3])
            rating = st.number_input("Rate this movie")
            if st.button("Submit"):
                updateRating(st.session_state.movie[0], rating)
        else:
            st.header("Please select a movie")
    else:
        st.header("Please Login to continue")

if __name__ == '__main__':
	main()
