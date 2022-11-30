import streamlit as st
import mysql.connector
from database import getLogin, signUp, getMovies, getMovieCount, getAvgRating, getMovieGenre
import plotly.express as px
import pandas as pd

def main():
        if st.session_state.user: 
                st.header("Home")
                st.write("Welcome", st.session_state.user[3])
                movies = getMovies()
                col1,col2 = st.columns(2)
                with col1:
                        for movie in movies:
                                if st.button(movie[1]):
                                        st.session_state.movie = movie
                with col2:
                        st.write("Total movies available: ", getMovieCount())
                        st.write("Average people's liking: ", getAvgRating())
                        movieList = getMovieGenre()
                        movieList = pd.DataFrame(movieList, columns=['genre','numberOfMovies'])
                        with st.expander('Genre: '):
                                pieChart = px.pie(movieList, names='genre',values='numberOfMovies')
                                st.plotly_chart(pieChart)
        else:
                st.header("Please Login to continue")


if __name__ == '__main__':
	main()


