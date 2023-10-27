import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carga de datos
@st.cache
def load_data():
    return sns.load_dataset('iris')

data = load_data()

# Título de la aplicación
st.title("Visualización del dataset Iris")

# Muestra los primeros registros del dataset
st.write(data.head())

# Gráfico de dispersión
st.subheader("Gráfico de dispersión según especie")
species = st.multiselect("Selecciona especies", data['species'].unique(), default=data['species'].unique())
filtered_data = data[data['species'].isin(species)]
plt.figure(figsize=(8, 6))
sns.scatterplot(data=filtered_data, x="sepal_length", y="sepal_width", hue="species", palette="deep")
st.pyplot(plt)

# Histograma
st.subheader("Histograma de longitud de sépalo")
bin_count = st.slider("Selecciona número de bins", min_value=5, max_value=50, value=20)
plt.figure(figsize=(8, 6))
plt.hist(data['sepal_length'], bins=bin_count, color='skyblue', edgecolor='black')
plt.xlabel("Longitud de sépalo")
plt.ylabel("Número de flores")
plt.title("Histograma de longitud de sépalo")
st.pyplot(plt)
