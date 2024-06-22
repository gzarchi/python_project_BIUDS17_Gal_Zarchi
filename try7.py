import streamlit as st

# Display a button in Streamlit
if st.button('Refresh App'):

    # Use JavaScript to redirect to a URL
    st.write('<script>window.location.href = "https://www.google.com";</script>', unsafe_allow_html=True)

