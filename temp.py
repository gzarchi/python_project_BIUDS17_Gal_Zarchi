import streamlit as st

if 'lst' in st.session_state:
    lst = st.session_state['lst']
else:
    lst = []

fetch = st.button('fetch')
if fetch:
    lst = [1, 2]
    st.write(lst)
    st.session_state['lst'] = lst

if 'lst' in st.session_state:
    save = st.button('save')
    if save:
        st.write(lst)

