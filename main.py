import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnResult.clicked.connect(self.on_btnResult_click)
        self.ui.btnClear.clicked.connect(self.on_btnClear_click)

    def on_btnResult_click(self):
        calculation = self.ui.txt_lineEdit.text()
        result = eval(calculation)

        self.ui.txtResult.setText(str(result))

    def on_btnClear_click(self):
        clear = ""
        self.ui.txt_lineEdit.setText(clear)
        self.ui.txtResult.setText(clear)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
