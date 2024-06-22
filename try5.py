import streamlit as st

def set_value(key, value):
    st.session_state[key] = value


def get_value(key):
    if key not in st.session_state:
        return None
    else:
        return st.session_state[key]

print('Hello World!')

# Display Title
st.markdown('# Current Weather App')

# Set initial settings
list_input = [['Jerusalem', 'Asia/Jerusalem', '\U0001F64A Celsius'],
              ['New York City', 'America/New_York', '\U0001F649 Fahrenheit']
              ]

# Copy list_input to set initial_settings
initial_settings = list_input

# Set list of temperatures
temp_list = ['\U0001F64A Celsius', '\U0001F648 Kelvin', '\U0001F649 Fahrenheit']

# Set selection_list
selection_list = [item[0] for item in initial_settings]
selection_list.append('Other')

# Display select box for city selection
selected_city = st.selectbox('Select a City:', selection_list)

# Extract selection_settings if 'Other' is not selected
selection_settings = []
if selected_city != 'Other':
    for i, item in enumerate(selection_list):
        if item == selected_city:
            selection_settings.append(initial_settings[i][0])
            selection_settings.append(initial_settings[i][1])
            selection_settings.append(initial_settings[i][2])
else:
    pass

# Display text input if 'Other' is selected
typed_input = st.text_input('City Name:') if selected_city == 'Other' else None

# Initialize input_settings
input_settings = []
if get_value('input_settings'):
    input_settings = get_value('input_settings')


# Determine initial temperature selection
if selected_city != 'Other':
    initial_temp_index = temp_list.index(selection_settings[2])
else:
    initial_temp_index = 0  # Default to Celsius for 'Other' selection

# Display radio buttons for temperature selection
selected_temp = st.radio('Temperature Units:', temp_list, index=initial_temp_index)

# Define changed_default_temp to capture if the default temperature selection has changed
changed_default_temp = selected_temp != temp_list[initial_temp_index]

# Define all possible 'input states'
selected_default = selected_city == selection_list[0]
selected_not_default = selected_city != 'Other' and not selected_default
input_empty_string = selected_city == 'Other' and typed_input == ''
input_string = selected_city == 'Other' and typed_input != ''

# Display fetch button
fetch_button = st.button('Fetch')



print(get_value('input_settings'))

# Process fetch button
if fetch_button:

    if input_empty_string:
        st.write('Enter City Name')

    elif selected_default or selected_not_default:
        st.write(f"fetch_selection({selection_settings[0]}, {selection_settings[1]}, {selected_temp})")

    elif input_string:
        # Simulate fetching input settings based on typed input
        set_value('input_settings', ['name', 'tz'])
        input_settings = ['name', 'tz']

        if not input_settings:
            st.markdown(f'Sorry... there is no weather data for `{typed_input}`')

        else:
            selection_settings = input_settings
            st.write(f"fetch_selection({selection_settings[0]}, {selection_settings[1]}, {selected_temp}) --> 'ow_data'")

# Display set_as_default button
# print(selected_not_default, input_string, input_settings)

if selected_not_default or (input_string and input_settings):
    set_as_default_button = st.button('Set as Default')

    # Process set_as_default_button
    if set_as_default_button:
        if input_string and not input_settings:
            st.markdown(f'Sorry... there is no weather data for `{typed_input}`')
        else:
            st.write(f"set_as_default({input_settings[0]}, {input_settings[1]}, {selected_temp})")

# Display save_settings button
cond_s1 = (selected_default or selected_not_default) and changed_default_temp
cond_s2 = not input_empty_string and input_string and input_settings
if cond_s1 or cond_s2:
    save_settings_button = st.button('Save Settings')

    # Process save_settings_button
    if save_settings_button:
        if input_string and not input_settings:
            st.markdown(f'Sorry... there is no weather data for `{typed_input}`')
        else:
            st.write(f"save_settings({selection_settings[0]}, {selection_settings[1]}, {selected_temp})")
