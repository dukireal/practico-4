import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QWidget,QLabel,QRadioButton,QLineEdit,QVBoxLayout,QHBoxLayout,QPushButton,QMessageBox
from decimal import Decimal
class FormatoDatos():
    def formato_moneda(self,cantidad):
        return f"U$d{cantidad}"
    def formato_fecha(self,dia,mes,anio):
        return f"{mes}/{dia}/{anio}"

class FormatoArgentino(FormatoDatos):
    def formato_moneda(self, cantidad):
        return f"${cantidad}"
    def formato_fecha(self, dia, mes, anio):
        return f"{dia}/{mes}/{anio}"

class FormatoEstadounidense(FormatoDatos):
    def formato_moneda(self, cantidad):
        return super().formato_moneda(cantidad)
    def formato_fecha(self, dia, mes, anio):
        return super().formato_fecha(dia, mes, anio)

class fecha_invalida(Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)


class MainWindow(QMainWindow):
    def __init__(self):
        super(QWidget,self).__init__()
        #titulo
        self.setWindowTitle("punto 3")
        #cantidad plata
        self.cantidad=QLineEdit()
        self.cantidad.setPlaceholderText("ingrese la cantidad de dinero")
        mostar_cantidad=QLabel("monto")
        #seleccion dia
        self.dia=QLineEdit()
        self.dia.setPlaceholderText("ingrese un dia")
        mostar_dia=QLabel("dia")
        #seleccion mes
        self.mes=QLineEdit()
        self.mes.setPlaceholderText("ingrese un mes")
        mostar_mes=QLabel("mes")
        #selccion año
        self.anio=QLineEdit()
        self.anio.setPlaceholderText("ingrese un anio")
        mostar_anio=QLabel("año")
        
        self.boton_formateo=QPushButton("formateo")
        self.boton_formateo.clicked.connect(self.formateo)
        
        
        #definicion formato argentino
        formato_argentino_label=QLabel("formato argentino: ")
        self.formato_argentino_radio=QRadioButton()
        #definicion fromato estadounidense
        formato_estadounidense_label=QLabel("formato estadounidense: ")
        self.formato_estadounidense_radio=QRadioButton()
        #layout y contenedor de los formatos#
        layout2=QHBoxLayout()
        layout2.addWidget(formato_argentino_label)
        layout2.addWidget(self.formato_argentino_radio)
        layout2.addWidget(formato_estadounidense_label)
        layout2.addWidget(self.formato_estadounidense_radio)
        contenedor2=QWidget()
        contenedor2.setLayout(layout2)
        
        #resultados#
        self.fecha_formateada=QLabel("resultado fecha: ")
        self.monto_formateado=QLabel("resultado moneda: ")
        
        #layout y contenedor del programa principal#
        layout=QVBoxLayout()
        layout.addWidget(mostar_cantidad)
        layout.addWidget(self.cantidad)
        layout.addWidget(mostar_anio)
        layout.addWidget(self.anio)
        layout.addWidget(mostar_mes)
        layout.addWidget(self.mes)
        layout.addWidget(mostar_dia)
        layout.addWidget(self.dia)
        layout.addWidget(contenedor2)
        layout.addWidget(self.boton_formateo)
        layout.addWidget(self.fecha_formateada)
        layout.addWidget(self.monto_formateado)
        contenedor=QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
    def formateo(self):
        mensaje=QMessageBox.critical(self,"error fecha", "fecha invalida ingrese nuevamente")
        try:
            cantidad=Decimal(self.cantidad.text())
            dia=int(self.dia.text())
            mes=int(self.mes.text())
            anio=int(self.anio.text())
            
            if 2100<anio<1900:
                raise fecha_invalida(mensaje)
            if 12<mes<0:
                raise fecha_invalida(mensaje)
            if 31<dia<0:
                raise fecha_invalida(mensaje)
            
            if self.formato_argentino_radio.isChecked():
                formato_datos=FormatoArgentino()
            elif self.formato_estadounidense_radio.isChecked():
                formato_datos=FormatoEstadounidense()
            else:
                QMessageBox.critical(self,"error","seleccione un formato")
                return
            
        except ValueError:
            QMessageBox.critical(self,"error","ingrese datos validos")
        fecha_formateada=formato_datos.formato_fecha(str(dia),str(mes),str(anio))
        monto_formateado=formato_datos.formato_moneda(cantidad)
        self.fecha_formateada.setText(f"resultado fecha: {fecha_formateada}")
        self.monto_formateado.setText(f"resultado moneda: {monto_formateado}")

app=QApplication(sys.argv)
ventana=MainWindow()
ventana.show()
app.exec()