import argparse
from PIL import Image
import os


def cambiar_dimensiones_imagen(input_path, output_path, new_width, new_height):
    try:
        # Abre la imagen
        imagen = Image.open(input_path)

        # Cambia las dimensiones de la imagen
        imagen = imagen.resize((new_width, new_height))

        # Guarda la imagen con las nuevas dimensiones
        imagen.save(output_path)

        print(
            f"La imagen se ha redimensionado exitosamente a {new_width}x{new_height} y se ha guardado en {output_path}")
    except Exception as e:
        print(f"Hubo un error al redimensionar la imagen: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description="Redimensionar una imagen PNG.")
    parser.add_argument("input_image", help="Ruta de la imagen de entrada (PNG).")
    parser.add_argument("output_image", help="Ruta de la imagen de salida (PNG).")
    parser.add_argument("width", type=int, help="Nueva anchura deseada.")
    parser.add_argument("height", type=int, help="Nueva altura deseada.")

    args = parser.parse_args()

    input_path = args.input_image
    output_path = args.output_image
    new_width = args.width
    new_height = args.height

    if not os.path.exists(input_path):
        print(f"La imagen de entrada '{input_path}' no existe.")
        return

    cambiar_dimensiones_imagen(input_path, output_path, new_width, new_height)


##ejecutar
##>python main.py imagen_entrada imagen_salida ancho alto
##python .\main.py .\LEGO_logo.svg.png .\LEGO_logo2.svg.png 300 400

if __name__ == "__main__":
    main()
