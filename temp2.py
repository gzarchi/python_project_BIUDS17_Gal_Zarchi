import streamlit as st

st.session_state['fetch'] = st.session_state['fetch'] if 'fetch' in st.session_state else 'default'
st.session_state['save'] = st.session_state['save'] if 'save' in st.session_state else 'default'
st.session_state['set as default'] = st.session_state['set as default'] if 'set as default' in st.session_state else 'default'

selected = st.selectbox('select:', [1, 2])

# Reset session state values to 'default' when user changes selection
if selected != st.session_state.get('selected', None):
    st.session_state['fetch'] = 'default'
    st.session_state['save'] = 'default'
    st.session_state['set as default'] = 'default'

# Update selected value in session state
st.session_state['selected'] = selected


fetch = st.button('fetch')
if fetch and st.session_state['fetch'] == 'default':
    st.write('fetching')
    st.session_state['fetch'] = f'fetched data'

if st.session_state['fetch'] != 'default':
    save = st.button('save')
    if save:
        st.write('saving')
        st.session_state['save'] = 'saved'

if st.session_state['save'] != 'default':
    set_as_default = st.button('set as default')
    if set_as_default:
        st.write('setting')
        st.session_state['set as default'] = 'set'

st.write(st.session_state['fetch'])
st.write(st.session_state['save'])
st.write(st.session_state['set as default'])











