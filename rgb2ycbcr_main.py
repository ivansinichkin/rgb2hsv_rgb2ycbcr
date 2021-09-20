import sys
# Импортируем наш интерфейс
from ui_rgb2ycbcr import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
import os.path


class MyWin():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_RGB_2_YCbCr_2_RGB()
        self.ui.setupUi(self.main_win)

        # Начало моего кода:
        self.ui.pushButton_selectF.clicked.connect(self.selectF)
        self.ui.pushButton_rgb2ycbcr.clicked.connect(self.rgb2ycbcr)
        self.ui.pushButton_ycbcr2rgb.clicked.connect(self.ycbcr2rgb)
        self.ui.sliderY.valueChanged.connect(self.labelsChanged)
        self.ui.sliderCb.valueChanged.connect(self.labelsChanged)
        self.ui.sliderCr.valueChanged.connect(self.labelsChanged)
        self.ui.valueLabelY.setText('0')
        self.ui.valueLabelCb.setText('0')
        self.ui.valueLabelCr.setText('0')

    def show(self):
        self.main_win.show()

    # функции, которые выполняются при нажатии на кнопку
    def selectF(self):
        path = QFileDialog.getOpenFileName()[0]
        relpath = os.path.relpath(path)
        image = Image.open(relpath)
        image.save("process1.jpg", "JPEG")
        pixmap = QPixmap("process1.jpg")
        myScaledPixmap = pixmap.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImageBase.setPixmap(myScaledPixmap)
        self.ui.labelImageBase.repaint()
        QApplication.processEvents()

    def labelsChanged(self):
        valueY = str(self.ui.sliderY.value() - 100)
        self.ui.valueLabelY.setText(valueY)
        valueCb = str(self.ui.sliderCb.value() - 100)
        self.ui.valueLabelCb.setText(valueCb)
        valueCr = str(self.ui.sliderCr.value() - 100)
        self.ui.valueLabelCr.setText(valueCr)

    def rgb2ycbcr(self):
        image = Image.open("process1.jpg")
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
        width = image.size[0]  # Определяем ширину
        height = image.size[1]  # Определяем высоту
        pix = image.load()  # Выгружаем значения пикселей
        imageY = Image.open('process1.jpg')
        imageCb = Image.open('process1.jpg')
        imageCr = Image.open('process1.jpg')
        drawY = ImageDraw.Draw(imageY)
        drawCb = ImageDraw.Draw(imageCb)
        drawCr = ImageDraw.Draw(imageCr)
        valueY = self.ui.sliderY.value() / 100
        valueCb = self.ui.sliderCb.value() / 100
        valueCr = self.ui.sliderCr.value() / 100
        for y in range(height):
            for x in range(width):
                r = pix[x, y][0]  # узнаём значение красного цвета пикселя
                g = pix[x, y][1]  # зелёного
                b = pix[x, y][2]  # синего
                Y = int((0.299 * r + 0.587 * g + 0.114 * b) * valueY)
                Cb = int(((-0.169 * r) + (-0.331 * g) + (0.5 * b) + 128) * valueCb)
                Cr = int(((0.5 * r) + (-0.419 * g) + (-0.081 * b) + 128) * valueCr)
                if Y >= 255:
                    Y = 255
                if Cb >= 255:
                    Cb = 255
                if Cr >= 255:
                    Cr = 255
                draw.point((x, y), (Y, Cb, Cr))  # рисуем пиксель
                drawY.point((x, y), (Y, Y, Y))
                drawCb.point((x, y), (255 - Cb, 255 - Cb, Cb))
                drawCr.point((x, y), (Cr, 255 - Cr, 255 - Cr))
        image.save("process2.jpg", "JPEG")
        imageY.save("process2Y.jpg", "JPEG")
        imageCb.save("process2Cb.jpg", "JPEG")
        imageCr.save("process2Cr.jpg", "JPEG")
        pixmap = QPixmap("process2.jpg")
        myScaledPixmap = pixmap.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImage_YCbCr.setPixmap(myScaledPixmap)
        self.ui.labelImage_YCbCr.repaint()
        pixmapY = QPixmap("process2Y.jpg")
        myScaledPixmapY = pixmapY.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImage_Y.setPixmap(myScaledPixmapY)
        self.ui.labelImage_Y.repaint()
        pixmapCb = QPixmap("process2Cb.jpg")
        myScaledPixmapCb = pixmapCb.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImage_Cb.setPixmap(myScaledPixmapCb)
        self.ui.labelImage_Cb.repaint()
        pixmapCr = QPixmap("process2Cr.jpg")
        myScaledPixmapCr = pixmapCr.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImage_Cr.setPixmap(myScaledPixmapCr)
        self.ui.labelImage_Cr.repaint()
        QApplication.processEvents()

    def ycbcr2rgb(self):
        image = Image.open('process2.jpg')
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
        width = image.size[0]  # Определяем ширину
        height = image.size[1]  # Определяем высоту
        pix = image.load()  # Выгружаем значения пикселей
        for y in range(height):
            for x in range(width):
                Y = pix[x, y][0]  # узнаём значения компонент
                Cb = pix[x, y][1]
                Cr = pix[x, y][2]
                R = int(Y + 1.402 * (Cr - 128))
                G = int(Y - 0.344 * (Cb - 128) - 0.714 * (Cr - 128))
                B = int(Y + 1.772 * (Cb - 128))
                draw.point((x, y), (R, G, B))  # рисуем пиксель
        image.save("process3.jpg", "JPEG")  # не забываем сохранить изображение
        pixmap = QPixmap("process3.jpg")
        myScaledPixmap = pixmap.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.ui.labelImageResult.setPixmap(myScaledPixmap)
        self.ui.labelImageResult.repaint()
        QApplication.processEvents()
        # Конец моего кода


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
