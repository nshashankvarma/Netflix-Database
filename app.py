import streamlit as st
import mysql.connector

from login import login
from database import getUserDetails

mydb = mysql.connector.connect(host='localhost',user='root',password='')
cur = mydb.cursor()

st.session_state.page="login"
st.session_state.user=''
st.session_state.movie=''

def main():
    st.title("Netflix DB")
    if st.session_state.page=="login":
        user=login()
        if user:
            st.session_state.page="home"
            st.session_state.user=user



if __name__ == '__main__':
    main()