import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton, QWidget,QLabel,QVBoxLayout,QLineEdit
from eldialgo import CustomDialog

class ConsignaDos(QWidget):
    def __init__(self):
        super().__init__()
        lbl=QLabel("ingrese un texto")
        layout=QVBoxLayout()
        texto=QLineEdit()
        texto.setPlaceholderText("inserte texto:")
        lbl2=QLabel()
        texto.textChanged.connect(lbl2.setText)
        layout.addWidget(lbl)
        layout.addWidget(texto)
        layout.addWidget(lbl2)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dlg2=ConsignaDos()
        self.setWindowTitle("ejercicio 1")
        
        
        lbl=QLabel("seleccione el ejercicio que desea realizar:")
        font = lbl.font()
        font.setPointSize(10)
        lbl.setFont(font)
        
        boton1 = QPushButton("consigna a")
        boton1.clicked.connect(self.opcion1)
    
        boton2 = QPushButton("consigna b")
        boton2.clicked.connect(self.opcion2)
        
        layout=QVBoxLayout()
        layout.addWidget(lbl)
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        
        contenedor=QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        
    def opcion1(self):
        dlg=CustomDialog(self)
        if dlg.exec():
            print("aceptar")
        else:
            print("cancelar")
    def opcion2(self):
        
        if self.dlg2.isVisible():
            self.dlg2.hide()
        else:
            self.dlg2.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()