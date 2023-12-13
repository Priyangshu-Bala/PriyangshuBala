import streamlit as st

def find_largest(num1,num2,num3):
  return max(num1, num2, num3)

st.title('Largest Number Finder')

num1 = st.number_input('Enter first number', value=0.0)
num2 = st.number_input('Enter second number', value=0.0)
num3 = st.number_input('Enter third number', value=0.0)

if st.button('Lets Find'):
  largest = find_largest(num1, num2, num3)
  st.success(f'The largest number is: {largest}')
