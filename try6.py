import streamlit as st

def selection(options):
    user_input = st.radio('select:', options)
    if user_input != st.session_state['user_input']:
        st.session_state['user_input'] = user_input
    return user_input


if 'user_input' not in st.session_state:
    st.session_state['user_input'] = None

button = st.button('go')

if button or st.session_state['user_input'] is not None:
    user_input = selection([1, 2, 3])
    st.write(user_input)