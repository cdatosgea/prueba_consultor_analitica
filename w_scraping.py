import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape_books() -> pd.DataFrame:
    """
    Esta función realiza scraping de la página web 'http://books.toscrape.com/' para extraer información sobre libros,
    incluyendo el título, el precio y la calificación.

    Parámetros:
    -----------
    No requiere parámetros de entrada.

    Retorna:
    --------
    pd.DataFrame:
        Un DataFrame de pandas que contiene los datos de los libros extraídos.
        El DataFrame tiene tres columnas:
        - 'title': El título del libro.
        - 'price': El precio del libro, como cadena de texto.
        - 'calification': La calificación del libro (número de estrellas), como cadena de texto.
    """
    
    # URL de la página web a la que se hará scraping
    url = "http://books.toscrape.com/"
    
    # Hacer la solicitud HTTP a la página web
    try:
        response = requests.get(url)
        # Parsear el contenido HTML de la página con BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        print(f"La página no carga correctamente: {str(e)}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

    # Lista para almacenar los datos de los libros
    books = []

    # Intentar extraer los datos de cada libro encontrado en la página
    try:
        for item in soup.find_all('article', class_='product_pod'):
            # Extraer el título del libro
            try:
                title = item.h3.a['title']
            except Exception:
                title = "Sin título"
            
            # Extraer el precio del libro
            try:
                price = item.find('p', class_='price_color').text
            except Exception:
                price = "Sin precio"
            
            # Extraer la calificación del libro
            try:
                calificaciones = item.find('p', class_='star-rating')
                calification = calificaciones['class'][1]
            except Exception:
                calification = "Sin calificación"
            
            # Añadir los datos del libro a la lista
            books.append({
                'title': title,
                'price': price,
                'calification': calification
            })
    except Exception as e:
        print(f"No se han encontrado productos: {str(e)}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

    # Convertir la lista de libros a un DataFrame y retornarlo
    return pd.DataFrame(books)


if __name__ == '__main__':
    # Ejecutar la función de scraping y guardar los resultados en un DataFrame
    books_df = scrape_books()
    
    # Guardar el DataFrame en un archivo CSV
    if not books_df.empty:
        books_df.to_csv('books.csv', index=False)
        print('Books saved to books.csv')
    else:
        print('No se guardaron datos ya que no se encontraron libros.')
