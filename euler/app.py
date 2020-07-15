import PyQt5, window, graphics
import pyqtgraph as pg
from PyQt5.QtWidgets import QMessageBox


class MainApp(PyQt5.QtWidgets.QMainWindow, window.Ui_MainWindow):
    acc, app = graphics.Accurate(), graphics.Approach(10)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.segments.setText('10')
        self.graphic_holder.setBackground('w')
        self.graphic_holder.showGrid(x = True, y = True)
        self.graphic_holder.setLabel('left', 'Y')
        self.graphic_holder.setLabel('bottom', 'X')
        self.initGraphics()
        self.refresh_graphic.clicked.connect(self.refreshGraphics)
        self.auto_approach.clicked.connect(self.autoSequence)

    def initGraphics(self):
        self.graphic_holder.clear()
        self.max_difference.setText("Максимальная невязка: %.4f" % self.difference(graphics.Accurate(self.app.n)))
        self.graphic_holder.addLegend()
        self.graphic_holder.plot(list(self.acc.dots.keys()), list(self.acc.dots.values()), pen = pg.mkPen(color='#568259', width = 2, style = PyQt5.QtCore.Qt.SolidLine), name = "Точное решение")
        self.graphic_holder.plot(list(self.app.dots.keys()), list(self.app.dots.values()), pen = pg.mkPen(color='#F55C3D', width = 2, style = PyQt5.QtCore.Qt.SolidLine), symbol = 'o', symbolSize = 4.5, symbolBrush = ('#F44B2A'), name = "Аппроксимация")

    def refreshGraphics(self):
        if self.validation(self.segments.text(), False):
            self.app = graphics.Approach(int(self.segments.text()))
            self.initGraphics()

    def autoSequence(self):
        value = 0
        self.progressBar.setValue(value)
        eps = self.getPrecision()
        if not eps == None:
            self.app = graphics.Approach(2)
            acc = graphics.Accurate(2)
            flag = True
            while flag:
                flag = False
                for x in self.app.dots:
                    diff = abs(self.app.dots[x] - acc.dots[x])
                    if diff > eps:
                        if value < 100 * 100 / (diff * 100 / eps):
                            value = 100 * 100 / (diff * 100 / eps)
                            self.progressBar.setValue(value)
                        self.app = graphics.Approach(self.app.n + 1)
                        acc = graphics.Accurate(self.app.n)
                        flag = True
                        break
            self.progressBar.setValue(100)
            self.segments.setText(str(self.app.n))
            self.initGraphics()

    def difference(self, acc):
        eps = 0
        for x in self.app.dots:
            if abs(self.app.dots[x] - acc.dots[x]) > eps:
                eps = abs(self.app.dots[x] - acc.dots[x])
        return eps

    def getPrecision(self):
        precision, ok = PyQt5.QtWidgets.QInputDialog.getText(self, "Ввод значения", "Точность:")
        if ok:
            if self.validation(precision, True):
                return float(precision)
            else:
                return None

    def validation(self, value, flag):
        valid = ''
        if flag: valid = '0123456789.'
        else: valid = '0123456789'
        for char in value:
            if not char in valid:
                self.errorMsg()
                return False
        if value[0] == '.' or float(value) == 0:
            self.errorMsg()
            return False
        return True

    def errorMsg(self):
        box = QMessageBox()
        box.setIcon(QMessageBox.Critical)
        box.setText("Неподходящее значение")
        box.setInformativeText("Только положительные значения, в качестве разделителя в дробях используйте точку")
        box.setWindowTitle("Ошибка")
        box.exec_()

