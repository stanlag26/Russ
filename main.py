import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from des import *
import sqlite3


# Реализовывает логику интерфейса программы
class Interface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.table_index = 0
        self.row_count = 1
        self.ui.pushButton_2.clicked.connect(self.add_table_item)

        # Отключаем стандартные границы окна программы
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Обработчики кнопок
        self.ui.pushButton.clicked.connect(self.close)

        # Перетаскивание безрамочного окна

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass

    def add_table_item(self):
        name = None
        how = None
        price = None
        data = None
        count = 1

        if (len(self.ui.lineEdit.text())) > 0:
            name = self.ui.lineEdit.text()
        else:
            return

        if (len(self.ui.lineEdit_2.text())) > 0:
            how = self.ui.lineEdit_2.text()
        else:
            return

        if (len(self.ui.lineEdit_3.text())) > 0:
            price = self.ui.lineEdit_3.text()
        else:
            return

        if (len(self.ui.lineEdit_3.text())) > 0:
            data = self.ui.lineEdit_3.text()
        else:
            return


        self.ui.tableWidget.setRowCount(self.row_count)
        self.ui.tableWidget.setItem(self.table_index, 0, QtWidgets.QTableWidgetItem(count))
        self.ui.tableWidget.setItem(self.table_index, 1, QtWidgets.QTableWidgetItem(name))
        self.ui.tableWidget.setItem(self.table_index, 2, QtWidgets.QTableWidgetItem(how))
        self.ui.tableWidget.setItem(self.table_index, 3, QtWidgets.QTableWidgetItem(price))
        self.ui.tableWidget.setItem(self.table_index, 4, QtWidgets.QTableWidgetItem(data))
        self.table_index += 1
        self.row_count += 1
        count += 1

        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_4.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())
