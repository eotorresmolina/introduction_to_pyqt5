from PyQt5 import uic, QtWidgets

qtCreatorFile = r'C:\Users\Emmanuel\Documents\GitHub\introduction_to_pyqt5\temperature_converter\temperature_converter.ui'


class MainApp(QtWidgets.QMainWindow):
    def __init__(self, title='MainWindow', *args):
        super(MainApp, self).__init__()  # Equivale a: super().__init__()
        uic.loadUi(uifile=qtCreatorFile, baseinstance=self)
        self.setWindowTitle(title)

        # ------ SIGNALS ------
        self.Button_celsius.clicked.connect(self.converterFtoC)
        self.Button_fahrenh.clicked.connect(self.converterCtoF)
        self.Button_exit.clicked.connect(self.closeWindow)


    # ------ SLOTS ------
    
    # Conversor de Fahrenheit a Celsius. 
    def converterFtoC(self):
        temperature_f = self.get_valueLineEdit('fahrenheit')
        if self.is_digit(temperature_f):
            temperature_c = str(round(float((5/9) * (float(temperature_f) - 32)), 2))
        else:
            temperature_c = 'NaN'
        self.lineEdit_celsius.setText(temperature_c)

    # Conversor de Celsius a Fahrenheit. 
    def converterCtoF(self):
        temperature_c = self.get_valueLineEdit('celsius')
        if self.is_digit(temperature_c):
            temperature_f = str(round(float((9/5) * (float(temperature_c) + 32)), 2))
        else:
            temperature_f = 'NaN'
        self.lineEdit_fahrenheit.setText(temperature_f)

    def closeWindow(self):
        self.close()


    # ------ METHODS -------
    def initUi(self):
        # Inicialización de Botones.
        self.Button_celsius.setText('Fahrenheit --> Celsius')
        self.Button_fahrenh.setText('Celsius --> Fahrenheit')
        self.Button_exit.setText('Exit')

        # Inicialización de Etiquetas.
        self.label_f.setText('° F')
        self.label_c.setText('° C')

        # Inicialización de lineEdit:
        self.lineEdit_fahrenheit.setPlaceholderText('Ingresar Temperatura en ° F')
        self.lineEdit_celsius.setPlaceholderText('Ingresar Temperatura en ° C')
        self.lineEdit_fahrenheit.setClearButtonEnabled(True)
        self.lineEdit_celsius.setClearButtonEnabled(True)


    def get_valueLineEdit(self, label=''):
        if label == 'fahrenheit':
            return self.lineEdit_fahrenheit.text()
        elif label == 'celsius':
            return self.lineEdit_celsius.text()
        else:
            return ''


    def is_digit(self, my_str):
        if '.' in my_str:
            digits = my_str.split('.')
            if digits[0][0] is '-':
                if digits[0].split('-')[1].isdigit() and digits[1].isdigit():
                    return True
                else:
                    return False
            else:
                if digits[0].isdigit() and digits[1].isdigit():
                    return True
                else:
                    return False
        else:
            if my_str[0] == '-':
                digits = my_str.split('-')
                if digits[1].isdigit():
                    return True
                else:
                    return False
            else:
                if my_str.isdigit():
                    return True
                else:
                    return False


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainApp(title='Temperature Converter')
    window.initUi()
    window.show()
    app.exec_()
    