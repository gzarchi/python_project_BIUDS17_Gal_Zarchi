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
else:
    pass

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

# Define all 'input states'
selected = selected_city != 'Other'
selected_default = selected_city == initial_list[0]
changed_selection_temp = selected_city != 'Other' and selected_temp != temp_list[initial_temp_index]
typed_empty_input = selected_city == 'Other' and city_input == ''
typed_string_input = selected_city == 'Other' and city_input != ''

# Display fetch button
fetch_button = st.button('Fetch')

# Process fetch button
if fetch_button:

    if typed_empty_input:
        st.write('Enter City Name')

    elif selected:
        st.write(f"fetch_selection({city_settings[0]}, {city_settings[1]}, {selected_temp})  -->  'ow_data'")

    elif typed_string_input:

        # Extract input_settings if selected_city != 'Other'
        input_settings = ['name', 'tz']  # f"extract_input_settings({city_input})  -->  [name, tz] or []"

        if input_settings == []:
            st.markdown(f'Sorry... there is no weather data for `{city_input}`')

        # Fetch typed_string_input
        else:
            city_settings = input_settings
            st.write(f"fetch_selection({city_settings[0]}, {city_settings[1]}, {selected_temp})  -->  'ow_data'")

# Display set_as_default button
button2cond1 = (selected and not selected_default) or changed_selection_temp
button2cond2 = typed_string_input and city_settings != []

if button2cond1 or button2cond2:
    set_as_default_button = st.button('Set as Default')

    # Process set_as_default button
    if set_as_default_button:
        st.write(f"set_as_default({city_settings[0]}, {city_settings[1]}, {selected_temp})  -->  changed input_list")

# Display save_settings button
if (selected and not selected_default and changed_selection_temp) or typed_string_input:
    save_button = st.button('Save City Settings')

    # Process set_settings_as_default button
    if save_button:
        st.write(f"save_city_settings({city_settings[0]}, {city_settings[1]}, {selected_temp})  -->  changed input_list")






# from try4

# state #1: selected_default
if selected_default:

    # Display fetch button
    fetch_button1 = st.button('Fetch')

# state #1.1: selected_default + changed_default_temp
if selected_default and changed_default_temp:

    # Display fetch button
    fetch_button11 = st.button('Fetch')

    # Display save_settings button
    save_button11 = st.button('Save City Settings')

# state #2: selected_not_default
if selected_not_default:

    # Display fetch button
    fetch_button2 = st.button('Fetch')

# state #2.1: selected_not_default + changed_default_temp

    # Display fetch button
    fetch_button21 = st.button('Fetch')

    # Display save_settings button
    save_button21 = st.button('Save City Settings')

# state #3: input_empty_string
if input_empty_string:

    # Display fetch button
    fetch_button3 = st.button('Fetch')

# state #4: input_string
if input_string:

    # Display fetch button
    fetch_button4 = st.button('Fetch')



