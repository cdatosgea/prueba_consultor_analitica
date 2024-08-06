import streamlit as st
from w_scraping import scrape_books

st.title("Books to Scrape")

df = scrape_books()

st.write("Here are some books:")
st.dataframe(df)
