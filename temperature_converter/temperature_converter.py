import sys
import os
from PyQt5 import uic, QtWidgets

script_path = os.path.dirname(os.path.abspath(__file__))
qtcreatorfile= os.path.join(script_path, 'temperature_converter.ui')


# Translate asset paths to useable format for PyInstaller
'''
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
'''


class MainApp(QtWidgets.QMainWindow):
    def __init__(self, title='MainWindow', *args):
        super(MainApp, self).__init__()  # Equivale a: super().__init__()
        uic.loadUi(uifile=qtcreatorfile, baseinstance=self)
        self.setWindowTitle(title)
        self.setFixedSize(700, 250)
        self.setStyleSheet("background-color: rgb(42, 42, 42)")

        # ------ SIGNALS ------
        self.Button_celsius.clicked.connect(self.converterFtoC)
        self.Button_fahrenh.clicked.connect(self.converterCtoF)
        self.Button_exit.clicked.connect(self.closeWindow)

    # ------ SLOTS ------
    
    # Conversor de Fahrenheit a Celsius. 
    def converterFtoC(self):
        temperature_f = self.get_valueLineEdit('fahrenheit')
        if temperature_f is not '':
            if self.is_digit(temperature_f):
                temperature_c = str(round(float((5/9) * (float(temperature_f) - 32)), 2))
            else:
                temperature_c = 'NaN'
        else:
            temperature_c = ''
        self.lineEdit_celsius.setText(temperature_c)

    # Conversor de Celsius a Fahrenheit. 
    def converterCtoF(self):
        temperature_c = self.get_valueLineEdit('celsius')
        if temperature_c is not '':
            if self.is_digit(temperature_c):
                temperature_f = str(round(float((9/5) * (float(temperature_c) + 32)), 2))
            else:
                temperature_f = 'NaN'
        else:
            temperature_f = ''
        self.lineEdit_fahrenheit.setText(temperature_f)

    def closeWindow(self):
        self.close()


    # ------ METHODS -------
    def initUi(self):
        # Inicialización de Botones.
        self.Button_celsius.setText('Fahrenheit --> Celsius')
        self.Button_fahrenh.setText('Celsius --> Fahrenheit')
        self.Button_exit.setText('Salir')
        self.Button_celsius.setStyleSheet('background-color: rgb(0, 118, 177); color: rgb(244, 244, 244);'
                                            + 'font: 70 10.5pt "Arial Black"')
        self.Button_fahrenh.setStyleSheet('background-color: rgb(0, 118, 177); color: rgb(244, 244, 244);'
                                            + 'font: 70 10.5pt "Arial Black"')
        self.Button_exit.setStyleSheet('background-color: rgb(0, 118, 177); font: 70 17pt "Arial Black"')

        # Inicialización de Etiquetas.
        self.label_f.setText('°F')
        self.label_c.setText('°C')
        self.label_c.setStyleSheet('color: red; font: 70 16pt "Arial Black"')
        self.label_f.setStyleSheet('color: red; font: 70 16pt "Arial Black"')

        # Inicialización de lineEdit:
        self.lineEdit_fahrenheit.setPlaceholderText('Temperatura en °F')
        self.lineEdit_celsius.setPlaceholderText('Temperatura en °C')
        self.lineEdit_fahrenheit.setClearButtonEnabled(True)
        self.lineEdit_celsius.setClearButtonEnabled(True)
        self.lineEdit_fahrenheit.setStyleSheet('background-color: rgb(255, 255, 255);'
                                                + 'font: 63 italic 13pt "Segoe UI Semibold"')
        self.lineEdit_celsius.setStyleSheet('background-color: rgb(255, 255, 255);'
                                                + 'font: 63 italic 13pt "Segoe UI Semibold"')


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
    #if hasattr(sys, '_MEIPASS'):
    #    os.chdir(sys._MEIPASS)

    app = QtWidgets.QApplication(sys.argv) # En este caso se puede reemplazar por: QtWidgets.QApplication([])
    window = MainApp(title='Temperature Converter')
    window.initUi()
    window.show()
    sys.exit(app.exec_())
    