import streamlit as st
import langchain_helper

st.title("Restuarant Name Generator")

cuisine = st.sidebar.selectbox("Cuisine" , ("Indian" , "Chinese" , "Mexican" , "Italian" , "American" ))

if cuisine:
    response = langchain_helper.generate_resturant_name_and_items(cuisine)
    st.header(response['resturant_name'])
    menu_items = response['menu_items'].split(',')

    st.write("Menu Items")

    for item in  menu_items:
        st.write("-" , item)