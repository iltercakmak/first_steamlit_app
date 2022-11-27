import streamlit

streamlit.title("Trying Streamlit")

streamlit.header("This is a header V2")
streamlit.text("This is the first line below the header.")
streamlit.text("🐔And this is the second line. Just trying things out.")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')
