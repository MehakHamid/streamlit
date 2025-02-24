import streamlit as st
st.title("my first app")
st.write("Hello, i'm mehak. its my first streamlit web")
st.header("Its a Header")
st.subheader("Its a Subheader")

name = st.text_input("Enter Your Name:")
age = st.number_input("Enter your Age:", min_value=1, max_value=100)
button = st.button("Submit")

if button:
    st.write(f"Hello {name}, Your age is {age} years.")


agree = st.checkbox("I love streamlit")

if agree:
    st.write("Thank you! 😊")

choice = st.selectbox("Choose your Fav Pet:", ["Dog", "Cat", "Rabbit"])
st.write(f"you choose {choice} !")


