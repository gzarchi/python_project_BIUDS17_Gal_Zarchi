import streamlit as st

# Display Title
st.markdown('# Current Weather Data App')

# Set initial settings
initial_settings = [['Jerusalem', 'Asia/Jerusalem', 'Celsius'],
                    ['New York City', 'America/New_York', 'Fahrenheit']]

# Set temperature list
temp_list = ['Celsius', 'Fahrenheit', 'Kelvin']

# Set cities list
cities_list = [item[0] for item in initial_settings]
cities_list.append('Other')

# Display selection box for cities list
selected_city = st.selectbox('Select a City: ', cities_list)

# Initialize 'selected_city' in st.session_state
st.session_state['selected_city'] = None

# Extract city settings
city_settings = []
for settings in initial_settings:
    if settings[0] == selected_city:
        city_settings = settings

# Display text input if 'Other' is selected
typed_city = st.text_input('City: ') if selected_city == 'Other' else None

# Initialize 'typed_city' in st.session_state
st.session_state['typed_city'] = None

# Clear st.session_state if selection is changed and set the new selection in st.session_state
if selected_city != st.session_state['selected_city'] or typed_city != st.session_state['typed_city']:
    st.session_state.clear()
    st.session_state['selected_city'] = selected_city
    st.session_state['typed_city'] = typed_city

# Determine default temperature
default_temp_index = temp_list.index(city_settings[2]) if city_settings else 0

# Display temperature buttons
selected_temp = st.radio('Temperature Units: ', temp_list, index=default_temp_index)


# End of user initial input
# ----------------------------------------------------------------------------------------------------

# check session states
fetch = st.button('fetch')
if fetch:
    st.session_state['fetch'] = f'fetched data for {selected_city}'

st.write(st.session_state['fetch'] if 'fetch' in st.session_state else None)

st.write(st.session_state['selected_city'])
st.write(st.session_state['typed_city'])