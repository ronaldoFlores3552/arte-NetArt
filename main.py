from PIL import Image, ImageDraw, ImageFont, ExifTags

def correct_image_orientation(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())

        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)

    except (AttributeError, KeyError, IndexError):
        pass

    return image

def scale_image(image, new_width=200):  # Aumenta el ancho para más detalle
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=10):  # Reduce el rango para más detalle
    ascii_str = ''
    ascii_chars = '@%#*+=-:. '  # Puedes experimentar con diferentes caracteres
    for pixel_value in image.getdata():
        ascii_str += ascii_chars[(pixel_value//range_width) % len(ascii_chars)]
    return ascii_str

def convert_image_to_ascii(image_path):
    try:
        image = Image.open(image_path)
        image = correct_image_orientation(image)
    except Exception as e:
        print(e)
        return
    image = scale_image(image)
    image = grayscale_image(image)
    ascii_str = map_pixels_to_ascii(image)
    return "\n".join(ascii_str[i:(i+image.width)] for i in range(0, len(ascii_str), image.width))

def save_ascii_to_image(ascii_str, font_path='arial.ttf', font_size=5):  # Reduce el tamaño de la fuente para más detalle
    ascii_lines = ascii_str.split("\n")
    image = Image.new('RGB', (len(ascii_lines[0])*font_size, len(ascii_lines)*font_size), 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    for i, line in enumerate(ascii_lines):
        draw.text((0, i*font_size), line, fill='black', font=font)
    image.save('ascii_art2.png')

ascii_str = convert_image_to_ascii('./img/caballos.jpg')
print(ascii_str)
save_ascii_to_image(ascii_str)