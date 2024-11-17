import streamlit as st
from PIL import Image

# add an image as the title
# install pillow -- from PIL import Image
my_image = Image.open(r"E:\Azubi\Phase 2\Week 5-7 StreamLit\banner title.png")
st.image(my_image, width=300)

# create home page
def home_page():
    #st.write('Classification Project')
    st.title(body="Embedding ML Models in GUI's using Streamlit")

    st.markdown(''' This app uses machine learning to predict whether a customer is likely to churn or not. ''')

    st.subheader('Instructions')
    st.markdown('''
        - Upload a csv file
        - Select the features you want for classification
        - Choose a machine learning model from the dropdown
        - Click on 'Classify' to get the predicted results
        - The app will give you a report on the performance of the model
        - Expect it to give you metrics like f1_score, recall, precision, and accuracy
                ''')

    st.header('App Features')
    st.markdown('''
    - **Data view**: Provides access to the customer's data
    - **Prediction Page**: shows the various models and the predictionsyou will make
    - **Dashboard**: Shows data visualizations for your data
            ''')
    
    st.subheader(body='User Benefits')
    st.markdown('''
    + **Data driven decisions**: Make informed decisions from your data
    + **Access machine learning**: Utilize machine learning algorithms to draw insights from your data
                ''')
    
    st.write('#### How to run the application')
    with st.container(border=True):
        st.code('''
        # Activate the virtual environment
        env/scripts/activate
                
        # Run the App
        streamlit run telco_churn_app.py
        ''')

    # adding a video
    st.video(data='https://www.youtube.com/watch?v=QsPDfIh12Hg&pp=ygUJc3RyZW1hbGl0', autoplay=False)

    
    # add a clickable link
    st.write('Click the link below to read more in streamlit documentation')
    st.markdown('[Streamlit Documentation](https://docs.streamlit.io/)')
  

    # add an image
    st.image(image=r"E:\Azubi\Phase 2\Week 5-7 StreamLit\image.classificaiton.png", caption='The Classification Process')



    st.divider()
    st.write('Need help?')
    st.write('Contact me on')
    st.markdown('''
    - emmagyek@gmail.com
    - +233 245232364
    ''')
