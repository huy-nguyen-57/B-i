from gitdb.util import close

from Ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.calculateBMI)
        self.pushButton_2.clicked.connect(close)

    def calculateBMI(self):
        weight = float(self.lineEdit.text())
        height = float(self.lineEdit_2.text())
        height = height / 100
        BMI = weight / (height * height)
        BMI = round(BMI, 2)
        comment = ""
        if BMI < 16:
            comment = "Severe Thinness"
        elif BMI < 17:
            comment = "Moderate Thinness"
        elif BMI < 18.5:
            comment = "Mild Thinness"
        elif BMI < 25:
            comment = "Normal"
        elif BMI < 30:
            comment = "Overweight"
        elif BMI < 35:
            comment = "Obese Class I"
        elif BMI < 40:
            comment = "Obese Class II"
        else:
            comment = "Obese Class III"
        self.lineEdit_3.setText(str(BMI))
        self.lineEdit_4.setText(comment)

    def show(self):
        self.MainWindow.show()