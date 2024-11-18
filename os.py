import os
import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials


# Función para conectar con Google Sheets
def connect_to_google_sheets():
    # Leer las credenciales desde las variables de entorno
    private_key = os.getenv("PRIVATE_KEY")
    if not private_key:
        raise ValueError("La variable de entorno 'PRIVATE_KEY' no está configurada o es inválida.")

    credentials_dict = {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": private_key.replace("\\n", "\n"),  # Convertir \\n a saltos de línea
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
    }

      # Scopes necesarios para Google Sheets y Google Drive
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",  # Acceso a Google Sheets
        "https://www.googleapis.com/auth/drive.file"    # Acceso a archivos en Google Drive
    ]

    # Crear credenciales
    creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key("17iinnc55WcEUDk86zBwA7_OD_UF_tDx_ORMecj16JFs")  # Reemplaza con el ID de tu Google Sheet
   worksheet = spreadsheet.worksheet("hoja")
        return worksheet
   
# Función para guardar datos en Google Sheets
def save_to_google_sheets(data):
    worksheet = connect_to_google_sheets()
    # Convierte el registro en una lista de valores para añadirlo como una nueva fila
    row = list(data.values())
    worksheet.append_row(row)
    print("Datos guardados en Google Sheets:", row)  # Para depuración
  

# Inicialización de datos en Streamlit
if "data" not in st.session_state:
    st.session_state.data = []

st.title("Reporte de Actividades - Unidad - CAHECOMI SA. DE C.V ")

# Sección 1: Datos Generales
st.header("Datos Generales")
fecha = st.date_input("Fecha", pd.Timestamp.today())
fecha_str = fecha.strftime("%Y-%m-%d")  # Convertir la fecha a una cadena
turno = st.selectbox("Turno", ["Día", "Noche"])
supervisor = st.selectbox("Nombre del Supervisor", ["Nestor Diaz", "Veronica"])

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
    observaciones_desarrollo = st.text_area("Observaciones")

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
    observaciones_fortificacion = st.text_area("Observaciones")

# Botón para guardar la entrada
if st.button("Guardar Datos"):
    data = {"Fecha": fecha_str, "Turno": turno, "Supervisor": supervisor, "Actividad": actividad}

    if actividad == "Desarrollo":
        data.update({
            "Lugar": lugar_desarrollo,
            "Equipo": equipo_desarrollo,
            "Oficial": oficial_desarrollo,
            "Ayudante": ayudante_desarrollo,
            "Barrenos Dados": barrenos_dados,
            "Longitud de Barrenación": longitud_barrenacion,
            "Observaciones": observaciones_desarrollo
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
            "Observaciones": observaciones_fortificacion
        })
    
    # Guardar datos en Google Sheets
    try:
        save_to_google_sheets(data)
        st.success("Datos guardados exitosamente en Google Sheets.")
    except Exception as e:
        st.error("Error al guardar en Google Sheets.")
        st.write(e)
