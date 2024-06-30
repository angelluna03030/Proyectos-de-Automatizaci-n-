from PIL import Image
import os

downloads_folder = "C:/Users/angel/OneDrive/Escritorio/proyectos/automatizacion/Comprimir/CompimirImagenes"

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(filename)

        if extension.lower() in [".png", ".jpg", ".jpeg"]:
            file_path = os.path.join(downloads_folder, filename)
            picture = Image.open(file_path)
            compressed_file_path = os.path.join(downloads_folder, "comprimidi_" + filename)
            picture.save(compressed_file_path, optimize=True, quality=60)
