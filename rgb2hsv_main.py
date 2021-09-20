import sys
# Импортируем наш интерфейс
from ui_rgb2hsv import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
import os.path
import math


class MyWin():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_RGB_2_HSV_2_RGB()
        self.ui.setupUi(self.main_win)

        # Начало моего кода:
        self.ui.pushButton_selectF.clicked.connect(self.selectF)
        self.ui.pushButton_execute.clicked.connect(self.rgb2hsv2rgb)
        self.ui.sliderS.valueChanged.connect(self.labelsChanged)
        self.ui.sliderV.valueChanged.connect(self.labelsChanged)
        self.ui.valueLabelS.setText('0')
        self.ui.valueLabelV.setText('0')

    def show(self):
        self.main_win.show()

    # функции, которые выполняются при нажатии на кнопку
    def selectF(self):
        path = QFileDialog.getOpenFileName()[0]
        relpath = os.path.relpath(path)
        image = Image.open(relpath)
        image.save("process1_hsv.jpg", "JPEG")
        pixmap = QPixmap("process1_hsv.jpg")
        myScaledPixmap = pixmap.scaled(330, 330, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImageBase.setPixmap(myScaledPixmap)
        self.ui.labelImageBase.repaint()
        QApplication.processEvents()

    def labelsChanged(self):
        valueS = str(self.ui.sliderS.value() - 100)
        self.ui.valueLabelS.setText(valueS)
        valueV = str(self.ui.sliderV.value() - 100)
        self.ui.valueLabelV.setText(valueV)

    def rgb2hsv2rgb(self):
        image = Image.open('process1_hsv.jpg')
        width = image.size[0]  # Определяем ширину
        height = image.size[1]  # Определяем высоту
        imageH = Image.open('process1_hsv.jpg')
        imageS = Image.open('process1_hsv.jpg')
        imageV = Image.open('process1_hsv.jpg')
        imageHSV2RGB = Image.open('process1_hsv.jpg')
        drawH = ImageDraw.Draw(imageH)  # Создаем инструмент для рисования
        drawS = ImageDraw.Draw(imageS)
        drawV = ImageDraw.Draw(imageV)
        drawHSV2RGB = ImageDraw.Draw(imageHSV2RGB)
        pix = image.load()  # Выгружаем значения пикселей

        valueS = self.ui.sliderS.value() / 100
        valueV = self.ui.sliderV.value() / 100

        for y in range(height):
            for x in range(width):
                r_ = pix[x, y][0] / 255  # узнаём значение красного цвета пикселя
                g_ = pix[x, y][1] / 255  # зелёного
                b_ = pix[x, y][2] / 255  # синего

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
                    S = (1 - (mmin / mmax)) * valueS

                if S >= 1:
                    S = 1

                V = mmax * valueV
                if V >= 1:
                    V = 1

                # для отображения H из вики
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

                drawH.point((x, y), (r, g, b))  # отрисовываем пиксели, чтобы потом использовать переменные заново
                Vout = int(V * 255)  # Значения для вывода в rgb
                Sout = int(S * 255)
                drawS.point((x, y), (255, 255 - Sout, 255 - Sout))
                drawV.point((x, y), (Vout, 0, 0))

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

                # рисуем пиксель
                drawHSV2RGB.point((x, y), (Rb, Gb, Bb))

        imageH.save("process2H_hsv.jpg", "JPEG")
        imageS.save("process2S_hsv.jpg", "JPEG")
        imageV.save("process2V_hsv.jpg", "JPEG")
        imageHSV2RGB.save("process2rgb_hsv.jpg", "JPEG")
        pixmapH = QPixmap("process2H_hsv.jpg")
        myScaledPixmapH = pixmapH.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImage_H.setPixmap(myScaledPixmapH)
        self.ui.labelImage_H.repaint()
        pixmapS = QPixmap("process2S_hsv.jpg")
        myScaledPixmapS = pixmapS.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImage_S.setPixmap(myScaledPixmapS)
        self.ui.labelImage_S.repaint()
        pixmapV = QPixmap("process2V_hsv.jpg")
        myScaledPixmapV = pixmapV.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImage_V.setPixmap(myScaledPixmapV)
        self.ui.labelImage_V.repaint()
        pixmapHSV2RGB = QPixmap("process2rgb_hsv.jpg")
        myScaledPixmapHSV2RGB = pixmapHSV2RGB.scaled(330, 330, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImageResult.setPixmap(myScaledPixmapHSV2RGB)
        self.ui.labelImageResult.repaint()
        QApplication.processEvents()
        # Конец моего кода


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())