import streamlit as st
st.header('Money Converter')
# Choose the conversion direction
choose_currency = st.selectbox('Choose the currency to convert:', ["USD to MMK", "MMK to USD"])
# Input the amount to convert
currency_input = st.number_input('Enter the amount:')
# Exchange rates
MMK_rate = 4500
# Conversion functions
def change_currency_to_MMK(amount):
    return amount * MMK_rate
def change_currency_to_USD(amount):
    return amount / MMK_rate
# Button to perform the conversion
if st.button('Convert'):
    if choose_currency == 'USD to MMK':
        result = change_currency_to_MMK(currency_input)
        st.write(f"{currency_input} USD is equal to {result} MMK")
    else:
        result = change_currency_to_USD(currency_input)
        st.write(f"{currency_input} MMK is equal to {result} USD")
st.text('Thank you')