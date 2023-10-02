import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QPushButton, QGroupBox, QMessageBox
from PyQt6.QtCore import Qt
from datetime import datetime
from decimal import Decimal

class FormatoDatos:
    def formatear_moneda(self, cantidad):
        return f"u$d{cantidad:.2f}"

    def formatear_fecha(self, dia, mes, año):
        return f"{mes}/{dia}/{año}"

class FormatoEstadounidense(FormatoDatos):
    pass

class FormatoArgentino(FormatoDatos):
    def formatear_moneda(self, cantidad):
        return f"${cantidad:,.2f}"
    def formatear_fecha(self, dia, mes, año):
        return f"{dia}/{mes}/{año}"

class InterfazGrafica(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Formateador de Datos")
        self.setGeometry(100, 100, 400, 300)

        self.cantidad_label = QLabel("Cantidad de dinero:")
        self.cantidad_edit = QLineEdit()

        self.dia_label = QLabel("Día:")
        self.dia_edit = QLineEdit()

        self.mes_label = QLabel("Mes:")
        self.mes_edit = QLineEdit()

        self.año_label = QLabel("Año:")
        self.año_edit = QLineEdit()

        self.formato_group = QGroupBox("Formato")
        self.formato_estadounidense_radio = QRadioButton("Estadounidense")
        self.formato_argentino_radio = QRadioButton("Argentino")

        self.resultado_moneda_label = QLabel("Resultado Moneda: ")
        self.resultado_fecha_label = QLabel("Resultado Fecha: ")

        self.boton = QPushButton("Formatear")
        self.boton.clicked.connect(self.formatear)

        self.init_layout()

    def init_layout(self):
        layout = QVBoxLayout()

        layout.addWidget(self.cantidad_label)
        layout.addWidget(self.cantidad_edit)

        layout.addWidget(self.dia_label)
        layout.addWidget(self.dia_edit)

        layout.addWidget(self.mes_label)
        layout.addWidget(self.mes_edit)

        layout.addWidget(self.año_label)
        layout.addWidget(self.año_edit)

        formato_layout = QHBoxLayout()
        formato_layout.addWidget(self.formato_estadounidense_radio)
        formato_layout.addWidget(self.formato_argentino_radio)
        self.formato_group.setLayout(formato_layout)
        layout.addWidget(self.formato_group)

        layout.addWidget(self.resultado_moneda_label)
        layout.addWidget(self.resultado_fecha_label)

        layout.addWidget(self.boton)

        self.setLayout(layout)

    def formatear(self):
        try:
            cantidad = Decimal(self.cantidad_edit.text())
            dia = int(self.dia_edit.text())
            mes = int(self.mes_edit.text())
            año = int(self.año_edit.text())

            if self.formato_estadounidense_radio.isChecked():
                formato_datos = FormatoEstadounidense()
            elif self.formato_argentino_radio.isChecked():
                formato_datos = FormatoArgentino()
            else:
                QMessageBox.critical(self, "Error", "Seleccione un formato.")
                return

            fecha_formateada = formato_datos.formatear_fecha(str(dia), str(mes), str(año))
            moneda_formateada = formato_datos.formatear_moneda(cantidad)

            self.resultado_fecha_label.setText(f"Resultado Fecha: {fecha_formateada}")
            self.resultado_moneda_label.setText(f"Resultado Moneda: {moneda_formateada}")

        except ValueError:
            QMessageBox.critical(self, "Error", "Ingrese datos válidos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = InterfazGrafica()
    ventana.show()
    sys.exit(app.exec())
