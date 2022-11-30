import streamlit as st
import mysql.connector
from database import getLogin, signUp

def login():
    signInCol, signUpCol = st.columns(2)
    with signInCol:
        st.text("Log In")
        loginId = st.text_input("Login ID")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            cred=getLogin(loginId, password)
            if cred:
                st.success("Login Successful")
                return cred
            else:
                st.error("Login Failed")

    with signUpCol:
        st.text("Sign Up")
        newLoginId = st.text_input("New Login ID")
        newPassword = st.text_input("New Password", type="password")
        name = st.text_input("Name")
        emailId = st.text_input("Email ID")
        phoneNo= st.text_input("Phone number")
        if st.button("SignUp"):
            signUp(newLoginId, newPassword, name, emailId, phoneNo)
            st.success("Sign Up Successful")
            return newLoginId