import streamlit
streamlit.title('My Mom\'s New Healthy Diner')


streamlit.header('Breakfast Favorites')
streamlit.text('🥣omega 3 & bluberry oatmeal')
streamlit.text('🥗Kale, Spinach and Rocket smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruit_to_show)
