from PyQt6 import uic, QtWidgets

class AddEditCoffeeForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)

    def getData(self):
        sort = self.findChild(QtWidgets.QLineEdit, "sortLineEdit").text()
        roast = self.findChild(QtWidgets.QLineEdit, "roastLineEdit").text()
        grind_or_beans = self.findChild(QtWidgets.QComboBox, "grindComboBox").currentText()
        taste = self.findChild(QtWidgets.QTextEdit, "tasteTextEdit").toPlainText()
        price = float(self.findChild(QtWidgets.QLineEdit, "priceLineEdit").text())
        volume = float(self.findChild(QtWidgets.QLineEdit, "volumeLineEdit").text())
        return (sort, roast, grind_or_beans, taste, price, volume)

    def setData(self, data):
        sort, roast, grind_or_beans, taste, price, volume = data
        self.findChild(QtWidgets.QLineEdit, "sortLineEdit").setText(sort)
        self.findChild(QtWidgets.QLineEdit, "roastLineEdit").setText(roast)
        index = self.findChild(QtWidgets.QComboBox, "grindComboBox").findText(grind_or_beans)
        if index >= 0:
            self.findChild(QtWidgets.QComboBox, "grindComboBox").setCurrentIndex(index)
        self.findChild(QtWidgets.QTextEdit, "tasteTextEdit").setPlainText(taste)
        self.findChild(QtWidgets.QLineEdit, "priceLineEdit").setText(str(price))
        self.findChild(QtWidgets.QLineEdit, "volumeLineEdit").setText(str(volume))