
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🔥 ComparAuto Max | Comparador de Autos", page_icon="🚘", layout="centered")

st.markdown("""<style>
    .main { background-color: #f8f9fa; }
    .stApp { font-family: 'Segoe UI', sans-serif; }
</style>""", unsafe_allow_html=True)

# ------------------ Base de datos de autos con marca y fotos ------------------
autos = pd.DataFrame({
    'Modelo': ['Nissan Versa', 'Toyota Prius', 'Tesla Model 3', 'Chevrolet Spark', 'BMW i3',
               'Mazda 3', 'Kia Rio', 'Ford Mustang Mach-E', 'Hyundai Elantra', 'Volkswagen Golf'],
    'Marca': ['Nissan', 'Toyota', 'Tesla', 'Chevrolet', 'BMW',
              'Mazda', 'Kia', 'Ford', 'Hyundai', 'Volkswagen'],
    'Imagen': [
        'nissan_versa.jpg', 'toyota_prius.jpg', 'tesla_model3.jpg', 'chevy_spark.jpg', 'bmw_i3.jpg',
        'mazda_3.jpg', 'kia_rio.jpg', 'mustang_mach_e.jpg', 'hyundai_elantra.jpg', 'vw_golf.jpg'
    ],
    'Tipo': ['Gasolina', 'Híbrido', 'Eléctrico', 'Gasolina', 'Eléctrico',
             'Gasolina', 'Gasolina', 'Eléctrico', 'Gasolina', 'Gasolina'],
    'Motor': ['1.6L I4', '1.8L Híbrido', 'Eléctrico', '1.4L I4', 'Eléctrico',
              '2.5L I4', '1.6L I4', 'Eléctrico', '2.0L I4', '1.4L Turbo'],
    'HP': [118, 121, 283, 98, 170, 186, 121, 346, 147, 150],
    'Torque (Nm)': [149, 142, 450, 127, 250, 252, 151, 580, 179, 250],
    'Cilindros': [4, 4, 0, 4, 0, 4, 4, 0, 4, 4],
    'Tracción': ['FWD', 'FWD', 'RWD', 'FWD', 'RWD', 'FWD', 'FWD', 'AWD', 'FWD', 'FWD'],
    'Transmisión': ['CVT', 'Automática', 'Automática', 'Manual', 'Automática',
                    'Automática', 'Manual', 'Automática', 'CVT', 'Automática'],
    'Rendimiento (km/L o km/kWh)': [16, 26, 6, 17, 7, 14, 16, 5, 15, 14],
    'Emisiones CO2 (g/km)': [140, 90, 0, 150, 0, 160, 145, 0, 155, 150],
    'Costo mantenimiento anual (MXN)': [8000, 7000, 5000, 7500, 5200, 8500, 7800, 6000, 8000, 7700],
    'Autonomía (km)': [750, 1000, 450, 700, 300, 650, 730, 490, 700, 720],
    'Costo promedio (MXN)': [300000, 450000, 900000, 250000, 700000, 420000, 290000, 980000, 350000, 370000]
})

# ------------------ Interfaz ------------------
st.title("🔥 ComparAuto Max")
st.subheader("Explora y compara vehículos con estilo y precisión")

autos_disp = autos['Modelo'].tolist()
auto1 = st.selectbox("Selecciona el primer auto", autos_disp, index=0)
auto2 = st.selectbox("Selecciona el segundo auto", autos_disp, index=1)

info1 = autos[autos['Modelo'] == auto1].reset_index(drop=True)
info2 = autos[autos['Modelo'] == auto2].reset_index(drop=True)
comparacion = pd.concat([info1, info2], ignore_index=True)

# Mostrar imágenes (solo si están en la carpeta img/)
st.write("### Vista previa de los vehículos")
col1, col2 = st.columns(2)
with col1:
    st.image(f"img/{info1['Imagen'][0]}", caption=f"{auto1}", width=300)
with col2:
    st.image(f"img/{info2['Imagen'][0]}", caption=f"{auto2}", width=300)

# Tabla detallada
st.write("### Comparación Detallada")
st.dataframe(comparacion.drop(columns=['Imagen']).set_index("Modelo"))

# Gráficas
atributos = ['HP', 'Torque (Nm)', 'Rendimiento (km/L o km/kWh)', 'Emisiones CO2 (g/km)',
             'Costo mantenimiento anual (MXN)', 'Autonomía (km)', 'Costo promedio (MXN)']

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = range(len(atributos))

bar1 = [info1[atributo][0] for atributo in atributos]
bar2 = [info2[atributo][0] for atributo in atributos]

ax.bar(index, bar1, bar_width, label=auto1)
ax.bar([i + bar_width for i in index], bar2, bar_width, label=auto2)

ax.set_xlabel('Atributos')
ax.set_ylabel('Valores')
ax.set_title('Comparación Visual Avanzada')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(atributos, rotation=45)
ax.legend()

st.pyplot(fig)
