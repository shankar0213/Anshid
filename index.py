import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from navigation import make_sidebar
from navigation import make_sidebar1
#from db import db1

#from navigation import hide_sidebar

import pandas as pd
import numpy as np
#
users_df = pd.read_csv("pages/db.csv")

#

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True) # To hide pages in sidebar

#
make_sidebar()
#hide_sidebar()

st.subheader('Customer Login')

        
#st.page_link("pages/page2.py", label="Secret Company Stuff", icon="🔒")
#
col1, col2 = st.columns(2)
with col1:
    with st.form("Form"): 
        email = st.text_input("Email Id",type="default")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Submit",type="primary")
        if submit:  
            if email in users_df['email'].values:
                user_data = users_df[users_df['email'] == email]
                if user_data['password'].iloc[0] == password:
                    st.success("Login successful!")

                    result = email.title()
                    st.session_state.logged_in = True
                    result= "Welcome "+result
                    st.success(result)
                    sleep(1)
                    st.switch_page("pages/page1.py")
                else:
                    st.error("Incorrect password!")
            else:
                st.error("Email not found!")
      