import os
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Configuración para acceder a Google Sheets usando variables de entorno
def connect_to_google_sheets():
    # Crear el diccionario de credenciales desde las variables de entorno
    credentials_dict = {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
    }

    creds = Credentials.from_service_account_info(credentials_dict)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key("your_google_sheet_id")  # Reemplaza con el ID de tu Google Sheet
    worksheet = spreadsheet.sheet1
    return worksheet

# Función para guardar datos en Google Sheets
def save_to_google_sheets(data):
    worksheet = connect_to_google_sheets()
    # Convierte el registro en una lista de valores para añadirlo como una nueva fila
    row = list(data.values())
    worksheet.append_row(row)

# Ejemplo de datos a guardar
data = {
    "Fecha": "2024-11-05",
    "Turno": "Día",
    "Supervisor": "Nestor Diaz",
    "Actividad": "Desarrollo",
    "Lugar": "Zona A",
    "Equipo": "Equipo 1",
    "Observaciones": "Operación sin fallas"
}

# Guardar en Google Sheets
save_to_google_sheets(data)
