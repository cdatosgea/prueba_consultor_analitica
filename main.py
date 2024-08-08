import streamlit as st
from w_scraping import scrape_books
import pandas as pd

st.title("Libros a la venta")

df = scrape_books()

st.write("Esta es una muestra de los libros disponibles")
st.dataframe(df)

###

# Título de la aplicación
st.title('Filtro de tabla')

title = df['title']

precio_opciones = ['Todos'] + list(df['price'].unique())
calificacion_opciones = ['Todos'] + list(df['calification'].unique())
# Filtro por precio
precio = st.selectbox('Seleccione un precio:', precio_opciones)
# Filtro por calificación
calificacion = st.selectbox('Selecciona una calificación:', calificacion_opciones)

# Aplicar los filtros al DataFrame
if precio == 'Todos':
    df_filtrado = df[df['calification'] == calificacion]
elif calificacion == 'Todos':
    df_filtrado = df[df['price'] == precio]
else:
    df_filtrado = df[(df['price'] == precio) & (df['calification'] == calificacion)]


# Mostrar el DataFrame filtrado
st.write('DataFrame filtrado:')
st.dataframe(df_filtrado)
###
