import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from streamlit_option_menu import option_menu
 


def hide_sidebar():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
 
def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")
 
    pages = get_pages("")
 
    return pages[ctx.page_script_hash]["page_name"]
 
 
 
def make_sidebar():
    msb=st.session_state.get('logged_in')
    #st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        section[data-testid="stSidebar"] ul li {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
    if msb:
        with st.sidebar:
            st.title("💎 LALINA WORLD")
            st.write("")
            st.header("= Navigation")
            if st.button("Log out"):
                    logout()


    else:    
        with st.sidebar:
            st.title("💎 LALINA WORLD")
            st.write("")
            st.header("= Navigation")
            #st.write("-"*10)
            temp=get_current_page_name()
            
            st.page_link("pages/page1.py", label="Customer Login", icon="🔒")
            st.page_link("pages/reg.py", label="Create Account", icon="🔒")
            st.page_link("pages/forgot.py", label="Forgot Password", icon="🔒")
            st.page_link("pages/admin.py", label="Admin", icon="🔒")
        
            temp=get_current_page_name()
            print('--->',temp)
            
        
            if st.session_state.get("logged_in", False):
                st.page_link("pages/page1.py", label="Secret Company Stuff", icon="🔒")
                #st.page_link("pages/page2.py", label="More Secret Stuff", icon="🕵️")
    
                st.write("")
                st.write("")
    
                if st.button("Log out"):
                    logout()
    
        
            elif temp not in ["index", "page2","reg","forgot","admin"]:
                # If anyone tries to access a secret page without being logged in,
                # redirect them to the login page
                #pass
                print('--')
                st.switch_page("index.py")
 
def make_sidebar1():
    msb=st.session_state.get('logged_in')
    #st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        section[data-testid="stSidebar"] ul li {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

    if msb:
        with st.sidebar:
            st.title("💎 LALINA WORLD")
            st.write("")
            
            if st.button("Log out"):
                    logout()

    else:                
        with st.sidebar:
            st.title("💎 LALINA WORLD")
            st.write("")
            selected = option_menu(
            menu_title="Main Menu",
            options = ["Customer Login"
            ,"Create Account",
            "Forgot Password",
            "Admin Login"],

            icons=["person-bounding-box","person-plus-fill","key","hammer"],
            menu_icon="cast",
            default_index=0,
            
                    )
                 
                   
            if selected=="Customer Login":
                st.page_link("index.py")
            elif selected=="Create Account":
                st.page_link("pages/reg.py") 
            elif selected=="Forgot Password":
                st.page_link("pages/forgot.py")         
            elif selected=="Admin Login":
                st.page_link("pages/admin.py")            

            temp=get_current_page_name()
            
                   


            print(temp)
            if st.session_state.get("logged_in", False):
                print('-------->')
                st.page_link("pages/page1.py", label="Secret Company Stuff", icon="🔒")
                        #st.page_link("pages/page2.py", label="More Secret Stuff", icon="🕵️")
            
                st.write("")
                st.write("")
            
                if st.button("Log out"):
                    logout()

            elif temp not in ["index", "page2","reg","forgot","admin"]:
                        # If anyone tries to access a secret page without being logged in,
                        # redirect them to the login page
                        #pass
                print('--')
                st.switch_page("index.py")  
         
                   
         

        


 
def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("index.py")