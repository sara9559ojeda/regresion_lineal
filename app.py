import streamlit as st
import joblib

st.title("Predicción con Regresión Lineal")

ejercicio = st.selectbox("Selecciona el ejercicio", ["Dólar", "Glucosa", "Energía"])

if ejercicio == "Dólar":
    modelo = joblib.load("modelo_dolar.joblib")
    dia = st.number_input("Día", min_value=1, value=1)
    inflacion = st.number_input("Inflación", value=0.02, format="%.4f")
    tasa_interes = st.number_input("Tasa de interés", value=5.0)
    if st.button("Predecir"):
        pred = modelo.predict([[dia, inflacion, tasa_interes]])[0]
        st.success(f"Precio del dólar predicho: {pred:.2f}")

elif ejercicio == "Glucosa":
    modelo = joblib.load("modelo_glucosa.joblib")
    edad = st.number_input("Edad", min_value=0, value=30)
    imc = st.number_input("IMC", value=24.0)
    actividad = st.number_input("Actividad física (horas/semana)", min_value=0, value=3)
    if st.button("Predecir"):
        pred = modelo.predict([[edad, imc, actividad]])[0]
        st.success(f"Nivel de glucosa predicho: {pred:.2f} mg/dL")

else:
    modelo = joblib.load("modelo_energia.joblib")
    temperatura = st.number_input("Temperatura (°C)", value=25.0)
    hora = st.number_input("Hora del día (1-24)", min_value=1, max_value=24, value=12)
    dia_semana = st.number_input("Día de la semana (1=Lunes, 7=Domingo)", min_value=1, max_value=7, value=1)
    if st.button("Predecir"):
        pred = modelo.predict([[temperatura, hora, dia_semana]])[0]
        st.success(f"Consumo de energía predicho: {pred:.2f} kWh")
