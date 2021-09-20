import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import math

image = Image.open('house2.jpg')
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
imageH = Image.open('house2.jpg')
imageS = Image.open('house2.jpg')
imageV = Image.open('house2.jpg')
imageHSV2RGB = Image.open('house2.jpg')
drawH = ImageDraw.Draw(imageH)
drawS = ImageDraw.Draw(imageS)
drawV = ImageDraw.Draw(imageV)
drawHSV2RGB = ImageDraw.Draw(imageHSV2RGB)
pix = image.load()  # Выгружаем значения пикселей
plt.imshow(image)
plt.show()


for y in range(height):
   for x in range(width):
      r_ = pix[x, y][0] / 255   # узнаём значение красного цвета пикселя
      g_ = pix[x, y][1] / 255   # зелёного
      b_ = pix[x, y][2] / 255   # синего

      mmax = max(r_, g_, b_)
      mmin = min(r_, g_, b_)
      if mmax == mmin:
         H = 0
      elif mmax == r_ and g_ >= b_:
         H = 60 * ((g_ - b_) / (mmax - mmin))
      elif mmax == r_ and g_ < b_:
         H = 60 * ((g_ - b_) / (mmax - mmin)) + 360
      elif mmax == g_:
         H = 60 * ((b_ - r_) / (mmax - mmin)) + 120
      elif mmax == b_:
         H = 60 * ((r_ - g_) / (mmax - mmin)) + 240

      if mmax == 0:
         S = 0
      else:
         S = 1 - (mmin / mmax)

      V = mmax



      # для отображения H
      Hi = int(math.fmod(abs(H / 60), 6))
      if Hi == 6:
         Hi = 0
      v = 100
      s = 100
      Vmin = 0
      a = 100 * (math.fmod(H, 60) / 60)
      Vinc = a
      Vdec = v - a
      if Hi == 0:
         r, g, b = v, Vinc, Vmin
      elif Hi == 1:
         r, g, b = Vdec, v, Vmin
      elif Hi == 2:
         r, g, b = Vmin, v, Vinc
      elif Hi == 3:
         r, g, b = Vmin, Vdec, v
      elif Hi == 4:
         r, g, b = Vinc, Vmin, v
      elif Hi == 5:
         r, g, b = v, Vmin, Vdec
      r, g, b = int(r * 255 / 100), int(g * 255 / 100), int(b * 255 / 100)
      #print(Hi, a, Vinc, Vdec)
      #print(r, g, b)
      drawH.point((x, y), (r, g, b))  # отрисовываем пиксели, чтобы потом использовать переменные заново
      Vout = int(V * 255)  # Значения для вывода в rgb
      Sout = int(S * 255)
      drawS.point((x, y), (255, 255 - Sout, 255 - Sout))
      drawV.point((x, y), (Vout, 0, 0))



      # обратное перобразование HSV 2 RGB
      # Топ, результат без артефактов

      V *= 100
      S *= 100
      Hi_ = int(math.fmod(abs(H / 60), 6))
      if Hi_ == 6:
         Hi_ = 0
      Vmin = ((100 - S) * V) / 100
      a = (V - Vmin) * (math.fmod(H, 60) / 60)
      Vinc = Vmin + a
      Vdec = V - a
      if Hi_ == 0:
         Rb, Gb, Bb = V, Vinc, Vmin
      elif Hi_ == 1:
         Rb, Gb, Bb = Vdec, V, Vmin
      elif Hi_ == 2:
         Rb, Gb, Bb = Vmin, V, Vinc
      elif Hi_ == 3:
         Rb, Gb, Bb = Vmin, Vdec, V
      elif Hi_ == 4:
         Rb, Gb, Bb = Vinc, Vmin, V
      elif Hi_ == 5:
         Rb, Gb, Bb = V, Vmin, Vdec
      Rb, Gb, Bb = int(Rb * 255 / 100), int(Gb * 255 / 100), int(Bb * 255 / 100)
      #print(Hi, a, Vinc, Vdec)
      #print(Rb, Gb, Bb)

      # рисуем пиксель
      drawHSV2RGB.point((x, y), (Rb, Gb, Bb))



#print(mmax, mmin)
#plt.imshow(image)
#plt.show()
plt.imshow(imageH)
plt.show()
plt.imshow(imageS)
plt.show()
plt.imshow(imageV)
plt.show()
plt.imshow(imageHSV2RGB)
plt.show()
#image.save("result.jpg", "JPEG")  # не забываем сохранить изображение
