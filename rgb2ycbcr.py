import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

image = Image.open('image.jpg')
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
imageY = Image.open('image.jpg')
imageCb = Image.open('image.jpg')
imageCr = Image.open('image.jpg')
drawY = ImageDraw.Draw(imageY)
drawCb = ImageDraw.Draw(imageCb)
drawCr = ImageDraw.Draw(imageCr)
pix = image.load()  # Выгружаем значения пикселей



for y in range(height):
   for x in range(width):
      r = pix[x, y][0]   # узнаём значение красного цвета пикселя
      g = pix[x, y][1]   # зелёного
      b = pix[x, y][2]   # синего
      Y = int((0.299 * r + 0.587 * g + 0.114 * b))
      Cb = int(((-0.169 * r) + (-0.331 * g) + (0.5 * b) + 128))
      Cr = int(((0.5 * r) + (-0.419 * g) + (-0.081 * b) + 128))
      draw.point((x, y), (Y, Cb, Cr))  # рисуем пиксель
      drawY.point((x, y), (Y, 0, 0))
      drawCb.point((x, y), (0, Cb, 0))
      drawCr.point((x, y), (0, 0, Cr))

plt.imshow(image)
plt.show()
plt.imshow(imageY)
plt.show()
plt.imshow(imageCb)
plt.show()
plt.imshow(imageCr)
plt.show()
#image.save("result.jpg", "JPEG")  # не забываем сохранить изображение
