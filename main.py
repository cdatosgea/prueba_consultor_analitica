import streamlit as st
from w_scraping import scrape_books

st.title("Libros a la venta")

df = scrape_books()

st.write("Esta es una muestra de los libros disponibles")
st.dataframe(df)
