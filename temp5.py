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

if 'typed_selection_settings' not in st.session_state:
    st.session_state['typed_selection_settings'] = None

# Display selection box for cities list
selection = st.selectbox('Select a City: ', cities_list)

# check if user selected already
if selection != st.session_state['selection']:
    st.session_state['selection'] = selection  # save value in st.session_state

# Extract selection settings
selection_settings = None
for settings in initial_settings:
    if settings[0] == selection:
        selection_settings = settings
        break

# Display typing field
typed_selection = st.text_input('City:') if selection == 'Other' else None

if typed_selection != st.session_state['typed_selection']:
    st.session_state['typed_selection'] = typed_selection # save value in st.session_state
    st.session_state['typed_selection_settings'] = None  # Reset typed_selection_settings

# Determine default temperature
default_temp_index = temp_list.index(selection_settings[2]) if selection_settings else 0

# Display temperature buttons
selected_temp = st.radio('Temperature Units: ', temp_list, index=default_temp_index)

# End of user initial input
# ----------------------------------------------------------------------------------------------------

# Display fetch button
fetch_button = st.button('Fetch')
if fetch_button:
    if selection != 'Other':
        st.write(f'fetch_data({selection_settings[0]}, {selection_settings[1]}, {selected_temp})')
    elif typed_selection == '':
        st.write(f'Enter a City')
    else:
        st.write(f'typed_selection_settings = get_typed_selection_settings({typed_selection})')

        # Simulate get_typed_selection_settings output
        typed_selection_settings = ['name', 'tz']

        # Save value in st.session_state
        if typed_selection_settings != st.session_state['typed_selection_settings']:
            st.session_state['typed_selection_settings'] = typed_selection_settings

        st.write(f'fetch_data({typed_selection_settings[0]}, {typed_selection_settings[1]}, {selected_temp})')

# Check
st.write(st.session_state['selection'])
st.write(st.session_state['typed_selection'])
st.write(st.session_state['typed_selection_settings'])

