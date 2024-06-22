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

# Define changed_input_settings states
changed_input_settings_state1 = selected_city != st.session_state['selected_city']
changed_input_settings_state2 = selected_city == st.session_state['selected_city'] and typed_city != st.session_state['typed_city']

# Clear st.session_state if selection is changed and set the new selection in st.session_state
if changed_input_settings_state1 or changed_input_settings_state2:
    st.session_state.clear()
    st.session_state['selected_city'] = selected_city

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





# Define terms to display buttons
selected = selected_city != 'Other'
empty_typed_city = not selected and typed_city == ''
changed_default_temp = selected and selected_temp != temp_list[default_temp_index]
found_typed_city_settings = not selected and 'typed_city_settings' in st.session_state
selected_default = selected_city == cities_list[0]

# Display 'Fetch Weather Data' button
if selected or not empty_typed_city:
    fetch_weather_data_button = st.button('Fetch Weather Data')

    # Process fetch_weather_data_button
    if fetch_weather_data_button:
        if selected:
            st.write(f'fetch_weather_data({city_settings[0]}, {city_settings[1]}, {selected_temp})  -->  df')
        elif not empty_typed_city:
            st.write(f'typed_city_settings = find_typed_city_settings({typed_city})  -->  [name, tz] or []')

            # Simulate output for typed_city_settings
            typed_city_settings = ['name', 'tz']

            if not typed_city_settings:
                st.write(f'Sorry, we have no data for `{typed_city}`...')
            else:
                st.session_state['typed_city_settings'] = typed_city_settings
                st.write(f'fetch_weather_data({typed_city_settings[0]}, {typed_city_settings[1]}, {selected_temp})  -->  df')

# Display 'Save to Favorites' button
if changed_default_temp or found_typed_city_settings:
    save_to_favorites_button = st.button('Save Settings')

    # Process save_to_favorites_button
    if save_to_favorites_button:
        st.write(f'save_to_favorites({city_settings[0]}, {city_settings[1]}, {selected_temp})')
        st.session_state['saved'] = True

# Display 'Set as Default' button
if 'saved' in st.session_state and not selected_default:
    set_as_default_button = st.button('Set as Default')

    # Process set_as_default_button
    if set_as_default_button:
        st.write(f'set_as_default({city_settings[0]}, {city_settings[1]}, {selected_temp})')
