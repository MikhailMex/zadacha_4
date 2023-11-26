from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""
        SELECT * FROM coffee_list""").fetchall()
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())