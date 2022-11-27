import streamlit as st

st.write("""
# Multiplication of 2 given numbers

This app multiplies the 2 given numbers
""")
#Get Input

st.header('Please enter numbers you want to multiply')

def user_input():
    num_1 = st.number_input("Enter 1st number")
    num_2 = st.number_input("Enter 2nd number")
    
    return num_1, num_2, num_1*num_2

num1, num2, multiplication = user_input()

st.subheader('Your answer is')
st.write(f"{num1} * {num2} = {multiplication}")
