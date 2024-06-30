from PIL import Image
import os
import shutil

# Definición de carpetas
paths = {
    #carpeta donde se darcargan los Archivos
    "downloads_folder": "C:/Users/angel/Downloads",
    #carpetas donde quieres guardar los archivos  
    "Carpetas_Archivos": "C:/Users/angel/OneDrive/Escritorio/Archivos",
    "Carpetas_Fotos": "C:/Users/angel/OneDrive/Escritorio/Fotos",
    "Carpetas_Software": "C:/Users/angel/OneDrive/Escritorio/Software",
    "downloads_video": "C:/Users/angel/OneDrive/Escritorio/video",
    "downloads_carpeta": "C:/Users/angel/OneDrive/Escritorio/carpetas",
    "downloads_random": "C:/Users/angel/OneDrive/Escritorio/random"
}

# Función para comprimir imágenes
def compress_image(file_path, save_path):
    picture = Image.open(file_path)
    picture.save(save_path, optimize=True, quality=60)
    print(f"Imagen comprimida y guardada en: {save_path}")

# Función para mover archivos
def move_file(src_path, dest_path):
    try:
        shutil.move(src_path, dest_path)
        print(f"Archivo movido a: {dest_path}")
    except Exception as e:
        print(f"Error al mover el archivo {src_path}: {e}")

if __name__ == "__main__":
    for filename in os.listdir(paths["downloads_folder"]):
        name, extension = os.path.splitext(filename)
        extension = extension.lower()
        src_path = os.path.join(paths["downloads_folder"], filename)

        # Manejo de imágenes
        if extension in  ['.png', '.jpeg', '.jpg', '.gif', '.bmp', '.tiff', '.svg', '.webp' , '.jpg']:
            dest_path = os.path.join(paths["Carpetas_Fotos"], "comprimido_" + filename)
            compress_image(src_path, dest_path)
        
        # Manejo de videos
        elif extension in ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg']:
            dest_path = os.path.join(paths["downloads_video"], filename)
            move_file(src_path, dest_path)
        
        # Manejo de archivos de software
        elif extension in ['.exe', '.msi', '.bat', '.sh', '.dmg', '.apk', '.bin', '.iso', '.jar', '.deb', '.rpm']:
            dest_path = os.path.join(paths["Carpetas_Software"], filename)
            move_file(src_path, dest_path)
        
        # Manejo de archivos de documentos
        elif extension in [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"]:
            dest_path = os.path.join(paths["Carpetas_Archivos"], filename)
            move_file(src_path, dest_path)
        
        # Manejo de carpetas y archivos comprimidos
        elif os.path.isdir(src_path) or extension in ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.bz2', '.tar.xz']:
            dest_path = os.path.join(paths["downloads_carpeta"], filename)
            move_file(src_path, dest_path)
        
        # Manejo de otros archivos
        else:
            dest_path = os.path.join(paths["downloads_random"], filename)
            move_file(src_path, dest_path)
