import streamlit as st
import joblib

st.set_page_config(page_title="Regresión Lineal", page_icon="📊", layout="centered")

st.markdown("""
<style>
:root {
    --bg: #f5f5f7;
    --card: #ffffff;
    --text: #1d1d1f;
    --muted: #6e6e73;
    --accent: #0071e3;
    --accent-2: #34aadc;
    --border: #d2d2d7;
}
@media (prefers-color-scheme: dark) {
    :root {
        --bg: #000000;
        --card: #1c1c1e;
        --text: #f5f5f7;
        --muted: #98989d;
        --accent: #0a84ff;
        --accent-2: #64d2ff;
        --border: #3a3a3c;
    }
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background: var(--bg) !important;
}

.block-container { max-width: 600px; padding-top: 3.5rem; }

* { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Helvetica Neue", sans-serif; }

.header h1 {
    font-weight: 700;
    letter-spacing: -0.03em;
    font-size: 2.3rem;
    color: var(--text);
    margin-bottom: 0.2rem;
}
.header p {
    color: var(--muted);
    font-size: 1.02rem;
    margin-bottom: 2rem;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--card);
    border: 1px solid var(--border) !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 40px rgba(0,0,0,0.08);
}

label { color: var(--muted) !important; font-size: 0.82rem !important; font-weight: 500 !important; }

[data-baseweb="select"] > div, input[type="number"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    border-radius: 10px !important;
    border: 1px solid var(--border) !important;
}

.stButton > button {
    background: linear-gradient(135deg, var(--accent), var(--accent-2));
    color: #fff;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    padding: 0.55rem 0;
    transition: opacity 0.15s ease;
}
.stButton > button:hover { opacity: 0.88; color: #fff; }

.result {
    margin-top: 1.2rem;
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1rem 1.25rem;
    text-align: center;
    font-size: 1.05rem;
    color: var(--text);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>Predicción con Regresión Lineal</h1>
    <p>Selecciona un escenario e ingresa los valores para obtener una predicción.</p>
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    ejercicio = st.selectbox("Ejercicio", ["Dólar", "Glucosa", "Energía"])
    resultado = None

    if ejercicio == "Dólar":
        modelo = joblib.load("modelo_dolar.joblib")
        c1, c2, c3 = st.columns(3)
        dia = c1.number_input("Día", min_value=1, value=1)
        inflacion = c2.number_input("Inflación", value=0.02, format="%.4f")
        tasa_interes = c3.number_input("Tasa interés", value=5.0)
        if st.button("Predecir", use_container_width=True):
            pred = modelo.predict([[dia, inflacion, tasa_interes]])[0]
            resultado = f"Precio del dólar predicho: <b>{pred:,.2f}</b>"

    elif ejercicio == "Glucosa":
        modelo = joblib.load("modelo_glucosa.joblib")
        c1, c2, c3 = st.columns(3)
        edad = c1.number_input("Edad", min_value=0, value=30)
        imc = c2.number_input("IMC", value=24.0)
        actividad = c3.number_input("Actividad física", min_value=0, value=3)
        if st.button("Predecir", use_container_width=True):
            pred = modelo.predict([[edad, imc, actividad]])[0]
            resultado = f"Nivel de glucosa predicho: <b>{pred:.2f} mg/dL</b>"

    else:
        modelo = joblib.load("modelo_energia.joblib")
        c1, c2, c3 = st.columns(3)
        temperatura = c1.number_input("Temperatura (°C)", value=25.0)
        hora = c2.number_input("Hora (1-24)", min_value=1, max_value=24, value=12)
        dia_semana = c3.number_input("Día semana (1-7)", min_value=1, max_value=7, value=1)
        if st.button("Predecir", use_container_width=True):
            pred = modelo.predict([[temperatura, hora, dia_semana]])[0]
            resultado = f"Consumo de energía predicho: <b>{pred:.2f} kWh</b>"

    if resultado:
        st.markdown(f'<div class="result">{resultado}</div>', unsafe_allow_html=True)
