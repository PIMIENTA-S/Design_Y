from pydrive. auth import GoogleAuth
from pydrive.drive import GoogleDrive


# Autenticación y creación del cliente de PyDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Esto abrirá una ventana del navegador para autenticarse
drive = GoogleDrive(gauth)

# ID de la carpeta de Google Drive
folder_xl = '108bFWuqqtyxkoq0RTU3MQDeEpcP7rVnB'

# Consulta para listar los archivos en la carpeta especificada
query = f"'{folder_xl}' in parents and trashed=false"
file_list = drive.ListFile({'q': query}).GetList()

# Obtener los nombres de los archivos
tallaXL = [file['title'] for file in file_list]

print(tallaXL)