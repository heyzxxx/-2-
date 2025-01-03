import textwrap


def center_text(text, font, image_width, draw):
    """
    возвращаем координату X для центрирования текста
    вычисляем ширину текста
    """
    text_width = draw.textbbox((0, 0), text, font=font)[2]
    return (image_width - text_width) // 2


def split_text(text, font, max_width):
    """
    разбиваем текст на строки
    используем среднюю ширину одного пробела для расчёта допустимого количества символов
    """
    space_width = font.getbbox(" ")[2]  # Ширина пробела
    return textwrap.wrap(text, width=int(max_width / space_width))
