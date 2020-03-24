from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QLabel, QTextEdit
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPoint
from name_checker import NameResolver
import page_scrapper

import sys
name_resolver = NameResolver()


class HelperWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.X11BypassWindowManagerHint |
                            QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("QLabel {font: 6pt Comic Sans MS}")
        self.setGeometry(QtWidgets.qApp.desktop().availableGeometry())
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1, 1))
        self.setFixedSize(80, 200)
        self.center()
#       labels
        self.item1 = QLabel(self)
        self.item2 = QLabel(self)
        self.item3 = QLabel(self)
        self.item4 = QLabel(self)
        self.item5 = QLabel(self)
        self.item6 = QLabel(self)
        self.labels = [self.item1, self.item2, self.item3, self.item4, self.item5, self.item6]
        posy = 0
        for label in self.labels:
            label.setText("NoneItem")
            label.setGeometry(5, posy, 80, 120)
            posy += 20
#       charselect
        self.input = QTextEdit(self)
        self.input.textChanged.connect(
            lambda: NameResolver.check_name(self.input.document().toPlainText()))
        self.input.setGeometry(0, 5, 80, 25)
        self.oldPos = self.pos()

        self.show()
        self.raise_()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        if name_resolver.is_selected():
            items = page_scrapper.check_build(name_resolver.get_champion())
            self.update_labels(self, items)
            name_resolver.false_selected()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    @staticmethod
    def update_labels(self, items_list):
        counter = 0
        for item in items_list:
            self.labels[counter].setText(item.text)
            counter += 1


app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: darkgray;}")

ex = HelperWindow()
sys.exit(app.exec_())
