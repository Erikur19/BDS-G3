from PIL import Image, ImageFont, ImageDraw

image = Image.open('Chrollo.jpg')
print (image.size)
print (image.mode)
print (image.format)

# image_blackwhite = image.convert ('L')
# image_blackwhite.show()

#redimensionar imagen
width = image.size [0]
height = image.size [1]
print (f'ancho : {width}')
print (f'alto: {height}')

factor = int (input("Ingrese el factor de redimensionamiento % que desea aplicar "))
print(factor/100)

new_width = round(width*factor/100)
new_height = round(height*factor/100)
print (f'nuevo ancho : {new_width}')
print (f'nuevo alto: {new_height}')

new_size = (new_width, new_height)

image_resized = image.resize (new_size)
# image_resized.show()
# image.show()

#incrustar textos en la imagen
font = ImageFont.truetype ('wind.ttf',40) #acá debo incluir tamaño de fuente
draw = ImageDraw.Draw (image_resized)
draw.text (
    (round(new_width*0.25),round(new_height*0.5)), #posición (coordenadas) iniciales del texto
    "CHROLLO HXH", #texto a insertar
    (19,81,119),  #este es el color
    font
)
image_resized.show ()

