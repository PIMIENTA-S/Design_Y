from pydrive. auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autenticación y creación del cliente de PyDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Esto abrirá una ventana del navegador para autenticarse
drive = GoogleDrive(gauth)

# ID de la carpeta de Google Drive
folder_id = '10SvO2yulC2OG_x0RzeqwurJ4ey0Y7FyQ'

# Consulta para listar los archivos en la carpeta especificada
query = f"'{folder_id}' in parents and trashed=false"
file_list = drive.ListFile({'q': query}).GetList()

# Obtener los nombres de los archivos
tallaL = [file['title'] for file in file_list]

tallaM = [file['title'] for file in file_list]
