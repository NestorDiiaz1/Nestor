import streamlit as st
import pandas as pd
from datetime import datetime

# Inicialización de datos
if "data" not in st.session_state:
    st.session_state.data = []

st.title("Reporte de Actividades - Unidad - CAHECOMI SA. DE C.V ")

# Sección 1: Datos Generales
st.header("Datos Generales")
fecha = st.date_input("Fecha", datetime.today())
turno = st.selectbox("Turno", ["Día", "Noche"])
supervisor = st.selectbox("Nombre del Supervisor", ["Nestor Diaz", " veronica"])


# Sección 2: Registro de Actividades
st.header("Registro de Actividades")

# Selección de Actividad
actividad = st.selectbox("Selecciona la Actividad", [
    "Desarrollo", "Voladura", "Fortificación"
])

# Campos específicos por actividad seleccionada
if actividad == "Desarrollo":
    st.subheader("Desarrollo")
    lugar_desarrollo = st.selectbox("Lugar", ["Zona A", "Zona B", "Zona C"])
    equipo_desarrollo = st.selectbox("Equipo", ["Equipo 1", "Equipo 2", "Equipo 3"])
    oficial_desarrollo = st.selectbox("Oficial", ["Oficial 1", "Oficial 2", "Oficial 3"])
    ayudante_desarrollo = st.selectbox("Ayudante", ["Ayudante 1", "Ayudante 2", "Ayudante 3"])
    barrenos_dados = st.number_input("Barrenos Dados", min_value=0, step=1)
    longitud_barrenacion = st.number_input("Longitud de Barrenación", min_value=0.0, step=0.1)
    hi_motor_diesel = st.number_input("Inicio Motor Diesel", min_value=0.0, step=0.1)
    hf_motor_diesel = st.number_input("Fin Motor Diesel", min_value=0.0, step=0.1)
    hi_electrico = st.number_input("Hi Eléctrico", min_value=0.0, step=0.1)
    hf_electrico = st.number_input("Hf Eléctrico", min_value=0.0, step=0.1)
    hi_perf = st.number_input("Hi Perf", min_value=0.0, step=0.1)
    hf_perf = st.number_input("Hf Perf", min_value=0.0, step=0.1)
    observaciones_desarrollo = st.text_area("Observaciones")
    demoras_fallas_desarrollo = st.text_area("Demoras o Fallas")

elif actividad == "Voladura":
    st.subheader("Voladura")
    lugar_voladura = st.selectbox("Lugar", ["Zona A", "Zona B", "Zona C"])
    oficial_voladura = st.selectbox("Oficial", ["Oficial 1", "Oficial 2", "Oficial 3"])
    ayudante_voladura = st.selectbox("Ayudante", ["Ayudante 1", "Ayudante 2", "Ayudante 3"])
    barrenos_cargados = st.number_input("Barrenos Cargados", min_value=0, step=1)
    longitud_real_disparo = st.number_input("Longitud Real de Disparo", min_value=0.0, step=0.1)
    observaciones_voladura = st.text_area("Observaciones")

elif actividad == "Fortificación":
    st.subheader("Fortificación")
    lugar_fortificacion = st.selectbox("Lugar", ["Zona A", "Zona B", "Zona C"])
    equipo_fortificacion = st.selectbox("Equipo", ["Equipo 1", "Equipo 2", "Equipo 3"])
    oficial_fortificacion = st.selectbox("Oficial", ["Oficial 1", "Oficial 2", "Oficial 3"])
    ayudante_fortificacion = st.selectbox("Ayudante", ["Ayudante 1", "Ayudante 2", "Ayudante 3"])
    barrenos_dados_fortificacion = st.number_input("Barrenos Dados", min_value=0, step=1)
    longitud_barrenacion_fortificacion = st.number_input("Longitud de Barrenación", min_value=0.0, step=0.1)
    anclas_colocadas = st.number_input("Anclas Colocadas", min_value=0, step=1)
    mallas_colocadas = st.number_input("Mallas Colocadas", min_value=0, step=1)
    hi_motor_diesel_fortificacion = st.number_input("Hi Motor Diesel", min_value=0.0, step=0.1)
    hf_motor_diesel_fortificacion = st.number_input("Hf Motor Diesel", min_value=0.0, step=0.1)
    hi_electrico_fortificacion = st.number_input("Hi Eléctrico", min_value=0.0, step=0.1)
    hf_electrico_fortificacion = st.number_input("Hf Eléctrico", min_value=0.0, step=0.1)
    hi_perf_fortificacion = st.number_input("Hi Perf", min_value=0.0, step=0.1)
    hf_perf_fortificacion = st.number_input("Hf Perf", min_value=0.0, step=0.1)
    observaciones_fortificacion = st.text_area("Observaciones")
    demoras_fallas_fortificacion = st.text_area("Demoras o Fallas")

# Botón para guardar la entrada
if st.button("Guardar Datos"):
    # Captura de datos según la actividad seleccionada
    data = {
        "Fecha": fecha,
        "Turno": turno,
        "Supervisor": supervisor,
    }
    
    if actividad == "Desarrollo":
        data.update({
            "Lugar": lugar_desarrollo,
            "Equipo": equipo_desarrollo,
            "Oficial": oficial_desarrollo,
            "Ayudante": ayudante_desarrollo,
            "Barrenos Dados": barrenos_dados,
            "Longitud de Barrenación": longitud_barrenacion,
            "Hi Motor Diesel": hi_motor_diesel,
            "Hf Motor Diesel": hf_motor_diesel,
            "Hi Eléctrico": hi_electrico,
            "Hf Eléctrico": hf_electrico,
            "Hi Perf": hi_perf,
            "Hf Perf": hf_perf,
            "Observaciones": observaciones_desarrollo,
            "Demoras o Fallas": demoras_fallas_desarrollo
        })
    elif actividad == "Voladura":
        data.update({
            "Lugar": lugar_voladura,
            "Oficial": oficial_voladura,
            "Ayudante": ayudante_voladura,
            "Barrenos Cargados": barrenos_cargados,
            "Longitud Real de Disparo": longitud_real_disparo,
            "Observaciones": observaciones_voladura
        })
    elif actividad == "Fortificación":
        data.update({
            "Lugar": lugar_fortificacion,
            "Equipo": equipo_fortificacion,
            "Oficial": oficial_fortificacion,
            "Ayudante": ayudante_fortificacion,
            "Barrenos Dados": barrenos_dados_fortificacion,
            "Longitud de Barrenación": longitud_barrenacion_fortificacion,
            "Anclas Colocadas": anclas_colocadas,
            "Mallas Colocadas": mallas_colocadas,
            "Hi Motor Diesel": hi_motor_diesel_fortificacion,
            "Hf Motor Diesel": hf_motor_diesel_fortificacion,
            "Hi Eléctrico": hi_electrico_fortificacion,
            "Hf Eléctrico": hf_electrico_fortificacion,
            "Hi Perf": hi_perf_fortificacion,
            "Hf Perf": hf_perf_fortificacion,
            "Observaciones": observaciones_fortificacion,
            "Demoras o Fallas": demoras_fallas_fortificacion
        })
    
    # Guardar datos en la sesión
    st.session_state.data.append(data)
    st.success("Datos guardados exitosamente")

# Visualización de datos
st.header("Datos Recopilados")
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.write(df)
    st.download_button("Descargar datos en CSV", data=df.to_csv(index=False), file_name="datos_operativos.csv",)
