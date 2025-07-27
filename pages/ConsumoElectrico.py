
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Consumo Eléctrico", page_icon="⚡")

st.title("⚡ Análisis de Consumo Eléctrico")
st.markdown("Sube una matriz de consumo por horas (formato CSV) y calcula el consumo base y coste.")

uploaded_file = st.file_uploader("Sube un archivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=None)
    st.write("📊 Matriz de consumo (kWh):")
    st.dataframe(df)

    precio_por_hora = np.linspace(0.1, 0.3, df.shape[1])
    consumo_total = df.sum(axis=0)
    coste_total = consumo_total * precio_por_hora

    st.write("💰 Precio horario simulado:")
    st.write(precio_por_hora)

    st.write("🔌 Consumo por hora:")
    st.bar_chart(consumo_total)

    st.write("💸 Coste total por hora:")
    st.bar_chart(coste_total)

    st.success(f"⚙️ Coste total estimado: **{coste_total.sum():.2f} €**")
