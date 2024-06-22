import streamlit as st

# Set 'selection' in st.session_state
st.session_state['selection'] = None

# Get user input
selection = st.selectbox('select:', [1,2])

# Clear st.session_state if selection is changed and set the new selection in st.session_state
if selection != st.session_state['selection']:
    st.session_state.clear()
    st.session_state['selection'] = selection

fetch = st.button('fetch')
if fetch:
    st.session_state['fetch'] = f'fetched data for {selection}'

st.write(st.session_state['fetch'] if 'fetch' in st.session_state else None)
