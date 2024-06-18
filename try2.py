# inputs: list_input(admin), selected_city/city_input(user), selected_temp(user)

# import functions:
# get_input_settings_for_city_input({city_input})
# get_data_for_city_input(input_settings[0], input_settings[1], {selected_temp})
# get_data_for_selected_city({city_settings[0]}, {city_settings[1]}, {selected_temp})
# Save_for_city_input(input_settings[0], input_settings[1], {selected_temp})
# Save_for_selected_city({city_settings[0]}, {city_settings[1]}, {selected_temp})
# set_default_for_city_input(input_settings[0], input_settings[1], {selected_temp})
# set_default_for_selected_city({city_settings[0]}, {city_settings[1]}, {selected_temp})

import streamlit as st

# Set initial settings
list_input = [['Jerusalem', 'Asia/Jerusalem', '\U0001F64A Celsius'],
                    ['New York City', 'America/New_York', '\U0001F649 Fahrenheit']
              ]

# Display Title
st.markdown('# Current Weather App')

# Copy list_input to set initial_settings
initial_settings = list_input

# Set list of temperatures
temp_list = ['\U0001F64A Celsius', '\U0001F648 Kelvin', '\U0001F649 Fahrenheit']

# Set initial_list
initial_names = [item[0] for item in initial_settings]
initial_names.append('Other')
initial_list = initial_names

# Display select box for city selection
selected_city = st.selectbox('Select a City:', initial_list)

# Extract city_settings if 'Other' is not selected
city_settings = []
if selected_city != 'Other':
    for i, item in enumerate(initial_list):
        if item == selected_city:
            city_settings.append(initial_settings[i][0])
            city_settings.append(initial_settings[i][1])
            city_settings.append(initial_settings[i][2])

# Display text input if 'Other' is selected
city_input = st.text_input('City Name:') if selected_city == 'Other' else None

# Determine initial temperature selection based on city selection
if selected_city == 'Other':
    initial_temp_index = 0  # Default to Celsius for 'Other' selection
else:
    initial_temp_index = temp_list.index(city_settings[2])  # Default to pre-defined selection

# Display radio buttons for temperature selection
selected_temp = st.radio('Temperature Units:', temp_list, index=initial_temp_index)


# ----------------------


# Extract input_settings if 'Other' is selected
input_settings = []
if city_input and city_input != '':
    st.write(f"append name and tz to input_settings[] with: get_input_settings_for_city_input({city_input})")

# Display fetch button
fetch_button = st.button('Fetch')

# Process fetch button click
if fetch_button:
    if city_input and city_input != '':
        # Process with city_input and selected_temp
        st.write(f"get_data_for_city_input(input_settings[0], input_settings[1], {selected_temp})")
    elif city_input == '':
        st.write("Enter 'City Name'")
    else:
        # Process with selected_city and temperature based on selected_city
        st.write(f"get_data_for_selected_city({city_settings[0]}, {city_settings[1]}, {selected_temp})")

# Display save_settings button
button2_cond1 = selected_city != 'Other' and selected_temp != temp_list[initial_temp_index]
button2_cond2 = selected_city == 'Other' and city_input != ''

if button2_cond1 or button2_cond2:
    save_settings = st.button('Save Settings')

    # Process save_setting button click
    if save_settings:
        if city_input and city_input != '':
            # Process with city_input and selected_temp
            st.write(f"Save_for_city_input(input_settings[0], input_settings[1], {selected_temp})")
        else:
            # Process with selected_city and temperature based on selected_city
            st.write(f"Save_for_selected_city({city_settings[0]}, {city_settings[1]}, {selected_temp})")

# Display set_settings_as_default button
button3_cond1 = button2_cond1
button3_cond2 = button2_cond2
button3_cond3 = (selected_city != initial_list[0] and selected_city != 'Other') or (selected_city == 'Other' and city_input != '')

if button3_cond1 or button3_cond2 or button3_cond3:
    set_settings_as_default = st.button('Set Settings as Default')

    # Process set_settings_as_default button click
    if set_settings_as_default:
        if city_input and city_input != '':
            # Process with city_input and selected_temp
            st.write(f"set_default_for_city_input(input_settings[0], input_settings[1], {selected_temp})")
        else:
            # Process with selected_city and temperature based on selected_city
            st.write(f"set_default_for_selected_city({city_settings[0]}, {city_settings[1]}, {selected_temp})")




