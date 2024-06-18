import streamlit as st

# Set initial settings
initial_settings = [['Jerusalem', 'Asia/Jerusalem', '\U0001F64A Celsius'],
                    ['London', 'Europe/London', '\U0001F64A Celsius'],
                    ['New York City', 'America/New_York', '\U0001F649 Fahrenheit']]

# Extract data by column
settings_names = [initial_setting[0] for initial_setting in initial_settings]
settings_tzs = [initial_setting[1] for initial_setting in initial_settings]
settings_temps = [initial_setting[2] for initial_setting in initial_settings]

# Set initial list of cities
settings_names.append('Other')
initial_list = settings_names

# Set list of temperatures
temp_list = ['\U0001F64A Celsius', '\U0001F648 Kelvin', '\U0001F649 Fahrenheit']

# Display Title
st.markdown('# Current Weather App')

# Display select box for city selection
name_selection = st.selectbox('Select City:', initial_list)

# Display text input if 'Other' is selected
name_input = st.text_input('Type City:') if name_selection == 'Other' else None

# Determine initial temperature selection based on city selection
if name_selection == 'Other':
    initial_temp_selection = 0  # Default to Celsius for 'Other' selection
else:
    initial_temp_selection = 1  # Default to pre-defined selection

# Display radio buttons for temperature selection
temp_selection = st.radio('Temperature in:', temp_list, index=initial_temp_selection)

# Display fetch button
fetch_button = st.button('Fetch')

# Process fetch button click
if fetch_button:
    if name_input:
        # Process with user input city and selected temperature

        # settings = get_settings_for_input(name_input, temp_selection)
        # get_weather_data(settings)
        st.write(name_input.lower().title(), temp_selection)
    else:
        # Process with selected city and temperature based on name_selection
        # settings = get_settings_for_selection(name_selection)
        # get_weather_data(settings)
        st.write(name_selection.lower().title(), temp_selection)

# Display set_settings_as_default button if settings != default
set_default_cond1 = name_selection != initial_list[0]
set_default_cond2 = (name_selection == initial_list[0]) and (temp_selection != settings_temps[0])
if (set_default_cond1 == "True") or (set_default_cond2 == 'True'):
    set_settings_as_default = st.button('Set Settings as Defualt')

    # Process set_settings_as_default button click
    if set_settings_as_default:
        st.write('settings saved as default.')

# Display save_settings button if
if name_input:
    save_settings = st.button('Save Settings')

    # Process save_setting button click
    if save_settings:
        st.write('settings saved in favorites.')

