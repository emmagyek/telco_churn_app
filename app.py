import streamlit as st
from home import home_page
from data import data_page
from predict import predict_page
from dashboard import dashboard_page
from auth import authenticate



# Link sidebar to the pages 
def main():
    authenticate()

    if st.session_state.authenticated:
        # creating a sidebar
        st.sidebar.title('Navigator')
        st.sidebar.title('Use the dropbox below to select between pages')
        page = st.sidebar.selectbox('Navigate',['Home', 'Data', 'Predict', 'Dashboard'])


        if page == 'Home':
            home_page()
        elif page == 'Data':
            data_page()
        elif page == 'Predict':
            predict_page()
        elif page == 'Dashboard':
            dashboard_page()
        

if __name__ == '__main__':
    main()