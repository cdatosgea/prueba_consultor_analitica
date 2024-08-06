import streamlit as st
import matplotlib.pyplot as plt
from web_scraping import scrape_books

st.title("Books to Scrape")

# Load data
df = scrape_books()

# Filter books
min_price = st.sidebar.slider('Minimum price', 0, 100, 0)
max_price = st.sidebar.slider('Maximum price', 0, 100, 100)
min_rating = st.sidebar.slider('Minimum rating', 1, 5, 1)

filtered_df = df[(df['price'] >= min_price) & (df['price'] <= max_price) & (df['rating'] >= min_rating)]

# Display data
st.write(f"Books priced between £{min_price} and £{max_price} with rating {min_rating} or higher:")
st.dataframe(filtered_df)

# Plot price distribution
fig, ax = plt.subplots()
ax.hist(filtered_df['price'], bins=20)
st.pyplot(fig)