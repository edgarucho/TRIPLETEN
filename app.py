# ==============================
# IMPORTACIONES
# ==============================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# ==============================
# CONFIGURACIÓN DE LA APP
# ==============================

st.set_page_config(
    page_title="TRIPLETEN - Análisis de Vehículos",
    layout="wide"
)

st.title("📊 Análisis de Vehículos - TRIPLETEN")
st.write("Aplicación interactiva para visualizar datos del dataset vehicles_us.csv")


# ==============================
# CARGA DE DATOS
# ==============================

@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

car_data = load_data()


# ==============================
# MOSTRAR DATOS
# ==============================

if st.checkbox("Mostrar tabla de datos"):
    st.write(car_data.head())


# ==============================
# BOTÓN HISTOGRAMA
# ==============================

st.subheader("Histograma del Odómetro")

hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Distribución del odómetro de los vehículos")

    fig = go.Figure(
        data=[go.Histogram(x=car_data["odometer"])]
    )

    fig.update_layout(
        title="Distribución del Odómetro",
        xaxis_title="Kilometraje",
        yaxis_title="Frecuencia"
    )

    st.plotly_chart(fig, use_container_width=True)


# ==============================
# BOTÓN DISPERSIÓN (extra)
# ==============================

st.subheader("Gráfico de Dispersión Precio vs Odómetro")

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Relación entre precio y kilometraje")

    fig_scatter = go.Figure(
        data=[go.Scatter(
            x=car_data["odometer"],
            y=car_data["price"],
            mode="markers"
        )]
    )

    fig_scatter.update_layout(
        title="Precio vs Odómetro",
        xaxis_title="Kilometraje",
        yaxis_title="Precio"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

