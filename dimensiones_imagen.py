from tkinter import Tk, filedialog
from PIL import Image, ImageFilter
import os

def resize_and_save(input_path, output_path, new_size):
    try:
        image = Image.open(input_path)
        resized_image = image.resize(new_size, Image.LANCZOS)  # Usar un filtro adecuado
        resized_image.save(output_path)
        print("Imagen redimensionada y guardada con éxito.")
    except Exception as e:
        print("Error al redimensionar y guardar la imagen:", str(e))

def main():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    file_paths = filedialog.askopenfilenames(filetypes=[("Imágenes", "*.jpg *.jpeg *.png")])

    if file_paths:
        new_size = (800, 800)

        for file_path in file_paths:
            folder_path, file_name = os.path.split(file_path)
            output_folder = os.path.join(folder_path, "ediciones")
            os.makedirs(output_folder, exist_ok=True)  # Crear la carpeta si no existe

            file_name_without_extension, extension = os.path.splitext(file_name)
            output_path = os.path.join(output_folder, f"{file_name_without_extension}_nueva{extension}")

            resize_and_save(file_path, output_path, new_size)

if __name__ == "__main__":
    main()