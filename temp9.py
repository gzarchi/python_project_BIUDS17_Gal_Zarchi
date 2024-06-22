# check temp5 using selection_settings instead of typed_input_settings

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

# Initialize session state
if 'selection' not in st.session_state:
    st.session_state['selection'] = None

if 'typed_selection' not in st.session_state:
    st.session_state['typed_selection'] = None

if 'selection_settings' not in st.session_state:
    st.session_state['selection_settings'] = None

if 'save_settings clicked' not in st.session_state:
    st.session_state['save_settings clicked'] = False

# Display selection box for cities list
selection = st.selectbox('Select a City: ', cities_list)

# check if user selected already
if selection != st.session_state['selection']:
    st.session_state['selection'] = selection  # save value in st.session_state

# Extract selection settings
selection_settings = None if selection != 'Other' else st.session_state['selection_settings']
for settings in initial_settings:
    if settings[0] == selection:
        selection_settings = settings
        break

# Check if selection_settings has changed and update session_state
if selection_settings != st.session_state['selection_settings']:
    st.session_state['selection_settings'] = selection_settings

# Display typing field
typed_selection = st.text_input('City:') if selection == 'Other' else None

if typed_selection != st.session_state['typed_selection']:
    st.session_state['typed_selection'] = typed_selection  # save value in st.session_state
    st.session_state['selection_settings'] = None

# Determine default temperature
default_temp_index = temp_list.index(selection_settings[2]) if st.session_state['selection_settings'] is not None else 0

# Display temperature buttons
selected_temp = st.radio('Temperature Units: ', temp_list, index=default_temp_index)

# End of user initial input
# ----------------------------------------------------------------------------------------------------

# Display fetch button
fetch_button = st.button('Fetch Data')
if fetch_button:

    # Process fetch_data() for an existing settings
    if selection != 'Other':
        st.write(f'fetch_data({selection_settings[0]}, {selection_settings[1]}, {selected_temp})')

    # Ask for user typed_input
    elif typed_selection == '':
        st.markdown(f'Enter ` City `')

    # Process get_typed_selection_settings() for a new typed_input
    else:
        st.write(f'typed_selection_settings = get_typed_selection_settings({typed_selection}) -->  [name, tz] or []')

        # Simulate get_typed_selection_settings output
        typed_selection_settings = ['name', 'tz']
        typed_selection_settings.append(selected_temp)

        # Set selection_settings as typed_selection_settings
        selection_settings = typed_selection_settings

        # Save value in st.session_state
        if selection_settings != st.session_state['selection_settings']:
            st.session_state['selection_settings'] = typed_selection_settings

        if not typed_selection_settings:
            st.write(f'Sorry, we have no data for `{typed_selection}`...')
        else:
            st.write(f'fetch_data({selection_settings[0]}, {selection_settings[1]}, {selected_temp})')

# Define terms to display buttons
selected = selection != 'Other'
empty_typed_selection = typed_selection == ''
found_typed_selection_settings = not selected and not empty_typed_selection and st.session_state['selection_settings'] is not None
changed_default_temp = selected and selected_temp != temp_list[default_temp_index]
selected_default = selection == cities_list[0]
save_settings_button_clicked = st.session_state['save_settings clicked']

# Display 'Save to Favorites' button
if changed_default_temp or found_typed_selection_settings:
    save_settings_button = st.button('Save Settings')

    # Process save_to_favorites_button
    if save_settings_button:
        st.session_state['save_settings clicked'] = True
        st.write(f'save_settings({selection_settings[0]}, {selection_settings[1]}, {selected_temp})  -->  check if exists already and saves/updates to favorites')

# Display 'Set as Default' button
if (selected and not selected_default and not changed_default_temp and not save_settings_button_clicked) or (not selected_default and save_settings_button_clicked):
    set_as_default_button = st.button('Set as Default')

    # Process set_as_default_button
    if set_as_default_button:
        st.write(f'set_as_default({selection_settings[0]}, {selection_settings[1]}, {selected_temp})  -->  replace saved settings with initial_settings[0]')
        st.session_state['save_settings clicked'] = False
