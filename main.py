import streamlit as st

import requests

name = st.text_input('Enter your name: ')

st.title(f'Welcome {name} to AP\'s Currency converter')

amount = st.number_input('Enter the amount in INR: ',min_value=1)

target_currency = st.selectbox('Select the currency to convert to:', ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD' ])

bt = st.button(f'Convert {amount} INR to {target_currency}')

if bt: 
    url = f'https://api.exchangerate-api.com/v4/latest/INR'

    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        conversion = amount * rate
        st.success(f'{amount} INR is equal to {conversion:.2f} {target_currency}')
    else:
        st.error('Error fetching exchange rates. Please try again later.')

      
