import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# --load assets --
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_2znxgjyt.json")
img_1 = Image.open("images/python_Data_Science.png")
img_2 = Image.open("images/python_Web_Development.png")

# --header section ----
with st.container():
    st.subheader("Hi, Python :wave:")
    st.title("Programming Language")
    st.write("Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.")
    st.write("[Learn More >](https://www.python.org/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Features of Python")
        st.write("##")
        st.write(
            """
            Python is a very developer-friendly language which means that anyone and everyone can learn to code it in a couple of hours or days, 
            - Open Source and Free
            - Support for GUI 
            - Object-Oriented Approach
            - High-Level Language
            - Integrated by Nature
            - Highly Portable
            - Highly Dynamic
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/watch?v=kqtD5dpn9C8)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Python Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_1)
    with text_column:
        st.subheader("Python Data Science Project")
        st.write(
            """
            Python is the preferred language among analytics professionals 
            to build pipelines, models, and dashboards. It's simplistic in nature 
            and provides a wide range of functionalities which makes it 
            the choice of programming language for a Data Scientist.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=9QNRhSAxPjY)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.subheader("Python Web Development Project")
        st.write(
            """
            Python is a popular programming language that is widely used
             in the development of web applications. It is easy to learn, 
             as a large and active community, and is supported by a wealth 
             of libraries and frameworks.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=9QNRhSAxPjY)")

# --contact ----
with st.container():
    st.write("---")
    st.header("To Learn More:")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/sabbavarapulahari27@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Text here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()