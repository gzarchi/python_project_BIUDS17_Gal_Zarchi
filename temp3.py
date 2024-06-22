import streamlit as st

# Display selection box
selection = st.selectbox('select:', [1, 2, 3])

# Initialize selection session state
st.session_state['selection'] = st.session_state['selection'] if 'selection' in st.session_state else None

if selection != st.session_state['selection']:
    st.session_state.clear()
    st.session_state['selection'] = selection

st.write(st.session_state['selection'])





