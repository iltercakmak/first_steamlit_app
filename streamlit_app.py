import streamlit

streamlit.title("Trying Streamlit")

streamlit.header("This is a header V2")
streamlit.text("This is the first line below the header.")
streamlit.text("🐔And this is the second line. Just trying things out.")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
