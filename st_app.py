import streamlit as st

# Display Title
st.markdown('# Current Weather App')

# Set initial settings
initial_settings = [['Jerusalem', 'Asia/Jerusalem', 'Celsius'],
                    ['New York City', 'America/New_York', 'Fahrenheit']
                    ]

# Set temperature options
temp_list = ['Celsius', 'Kelvin', 'Fahrenheit']

# Set cities list
cities_list = [item[0] for item in initial_settings]
cities_list.append('Other')

# Display selection box for cities list
selected_city = st.selectbox('Select a City:', cities_list)

# Extract city settings
city_settings = []
if selected_city != 'Other':
    city_settings = [initial_settings[i] for i, item in enumerate(cities_list) if item == selected_city]

# Determine default temperature
default_temp_index = temp_list.index(city_settings[0][2]) if selected_city != 'Other' else 0

# Display temperature buttons
selected_temp = st.radio('Temperature Units:', temp_list, index=default_temp_index)



