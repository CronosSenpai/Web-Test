
import streamlit as st
from pulp import LpProblem, LpVariable, LpMaximize, value

st.set_page_config(page_title="Optimización en Videojuego", page_icon="📦")

st.title("📦 Optimización de Producción en Videojuego")
st.markdown("Este módulo calcula la cantidad óptima a producir para maximizar beneficio.")

precio_venta = st.number_input("Precio de venta del insumo (abido)", min_value=0.0, value=100.0)
costo_material1 = st.number_input("Costo de material 1 (por unidad)", min_value=0.0, value=10.0)
costo_material2 = st.number_input("Costo de material 2 (por unidad)", min_value=0.0, value=20.0)

disp_material1 = st.number_input("Cantidad disponible de material 1", min_value=0.0, value=50.0)
disp_material2 = st.number_input("Cantidad disponible de material 2", min_value=0.0, value=80.0)

uso_material1 = st.number_input("Material 1 necesario por unidad producida", min_value=0.1, value=2.0)
uso_material2 = st.number_input("Material 2 necesario por unidad producida", min_value=0.1, value=1.0)

if st.button("Calcular producción óptima"):
    prob = LpProblem("Maximizar_Beneficio", LpMaximize)
    x = LpVariable("unidades_a_producir", lowBound=0)

    beneficio_unitario = precio_venta - (uso_material1 * costo_material1 + uso_material2 * costo_material2)
    prob += beneficio_unitario * x, "BeneficioTotal"
    prob += uso_material1 * x <= disp_material1, "RestriccionMaterial1"
    prob += uso_material2 * x <= disp_material2, "RestriccionMaterial2"

    prob.solve()

    st.success("✅ Optimización completada")
    st.write(f"🔧 Unidades óptimas a producir: **{x.varValue:.2f}**")
    st.write(f"💰 Beneficio total: **{value(prob.objective):.2f}**")
