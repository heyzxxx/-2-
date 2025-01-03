from PIL import Image, ImageDraw, ImageFont
import os
from utils.helpers import center_text, split_text
from exceptions import FileNotFoundException, InvalidInputException
from decorators import validate_input


class MemeGenerator:
    # класс для обработки изображения с добавлением текста.

    @validate_input
    def __init__(self, font_path="arial/ARIAL.ttf"):
        # импортируем собственные шрифты потому что встроенный в библиотеку не изменяется
        if not os.path.exists(font_path):
            raise FileNotFoundException(f"Шрифт {font_path} не найден.")
        self.font_path = font_path

    def process_image(self):
        # метод для обработки изображения
        try:
            filename = input("Введите название файла изображения (с расширением): ").strip()
            if not os.path.exists(filename):
                raise FileNotFoundException(f"Файл {filename} не найден.")

            top_text = input("Введите текст для верхней части изображения: ")
            bottom_text = input("Введите текст для нижней части изображения: ")

            font_size = int(input("Введите размер шрифта (64/128/192): ") or 128)
            output_filename = input("Введите имя выходного файла (с расширением): ") or f"output_{filename}"


            # https://pillow.readthedocs.io/en/stable/reference/Image.html
            image = Image.open(filename)

            # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
            draw = ImageDraw.Draw(image)

            # https://pillow.readthedocs.io/en/stable/reference/ImageFont.html
            font = ImageFont.truetype(self.font_path, size=font_size)

            self._add_text(draw, image, top_text, font, "top")
            self._add_text(draw, image, bottom_text, font, "bottom")

            image.save(output_filename)
            print(f"Сохранено как {output_filename}")

        except InvalidInputException as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def _add_text(self, draw, image, text, font, position):
        # добавляем текст на изображение
        image_width, image_height = image.size
        max_width = image_width - 20
        lines = split_text(text, font, max_width)

        if position == "top":
            y_position = 10
        elif position == "bottom":
            total_height = len(lines) * font.size + (len(lines) - 1) * 10
            y_position = image_height - total_height - 10

        for line in lines:
            x_position = center_text(line, font, image_width, draw)
            draw.text((x_position, y_position), line, font=font, fill="white", stroke_fill="black", stroke_width=2)
            y_position += font.size + 10
