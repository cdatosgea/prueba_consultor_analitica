import streamlit as st
from w_scraping import scrape_books
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

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

# Título de la aplicación
st.title('distribución de calificaciones')

categorias = df['calification']
contador = Counter(categorias)
labels = list(contador.keys())
cantidades = list(contador.values())

# Calcular porcentajes
total = sum(cantidades)
porcentajes = [(cantidad / total) * 100 for cantidad in cantidades]

# Crear gráfico circular
fig, ax = plt.subplots()
ax.pie(porcentajes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Para asegurar que el gráfico sea un círculo

# Mostrar gráfico en Streamlit
st.pyplot(fig)