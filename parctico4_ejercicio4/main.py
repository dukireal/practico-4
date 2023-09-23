import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QComboBox,QVBoxLayout,QPushButton,QMessageBox
from Idiomas import Frances,Ingles,Portugues
class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        #definicion del titulo#
        self.setWindowTitle("ejercicio 4")
        self.setGeometry(300,150,500,340)
        #idiomas#
        self.idioma_ingles=Ingles('','','','','','')
        self.idioma_frances=Frances('','','','','','')
        self.idioma_portugues=Portugues('','','','','','')
        label=QLabel("idioma:")
        #labels#
        self.saludo=QLabel("saludo:")
        self.despedida=QLabel("despedida:")
        self.disculpas=QLabel("disculpas:")
        self.pedir_cafe=QLabel("pedir cafe: ")
        self.pedir_precio=QLabel("pedir precio: ")
        self.pedir_ubicacion=QLabel("preguntar por ubicacion: ")
        
        #barrita para dezplazar idiomas#
        self.idiomas_disponibles=QComboBox()
        self.idiomas_disponibles.setPlaceholderText("selccione un idioma...")
        self.idiomas_disponibles.addItems(["ingles","frances","portugues"])
        #boton de traduccion#
        boton_traducir=QPushButton("traducir")
        boton_traducir.clicked.connect(self.traduccion)
        #layout#
        layout=QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.idiomas_disponibles)
        layout.addWidget(self.saludo)
        layout.addWidget(self.despedida)
        layout.addWidget(self.disculpas)
        layout.addWidget(self.pedir_cafe)
        layout.addWidget(self.pedir_precio)
        layout.addWidget(self.pedir_ubicacion)
        layout.addWidget(boton_traducir)
        contenedor=QWidget()
        contenedor.setLayout(layout)
        
        self.setCentralWidget(contenedor)
    def traduccion(self):
        try:
            opcion_seleccionada=self.idiomas_disponibles.currentText()
            if opcion_seleccionada=="ingles":
                self.saludo.setText(f"saludo: {self.idioma_ingles.saludar()}")
                self.despedida.setText(f"despedida: {self.idioma_ingles.despedirse()}")
                self.disculpas.setText(f"disculpas: {self.idioma_ingles.perdon()}")
                self.pedir_cafe.setText(f"pedir cafe: {self.idioma_ingles.pedirCafe()}")
                self.pedir_precio.setText(f"pedir precio: {self.idioma_ingles.cuantoCuesta()}")
                self.pedir_ubicacion.setText(f"preguntar ubicacion: {self.idioma_ingles.dondeQueda()}")
            elif opcion_seleccionada=="frances":
                self.saludo.setText(f"saludo: {self.idioma_frances.saludar()}")
                self.despedida.setText(f"despedida: {self.idioma_frances.despedirse()}")
                self.disculpas.setText(f"disculpas: {self.idioma_frances.perdon()}")
                self.pedir_cafe.setText(f"pedir cafe: {self.idioma_frances.pedirCafe()}")
                self.pedir_precio.setText(f"pedir precio: {self.idioma_frances.cuantoCuesta()}")
                self.pedir_ubicacion.setText(f"preguntar ubicacion: {self.idioma_frances.dondeQueda()}")
            elif opcion_seleccionada=="portugues":
                self.saludo.setText(f"saludo: {self.idioma_portugues.saludar()}")
                self.despedida.setText(f"despedida: {self.idioma_portugues.despedirse()}")
                self.disculpas.setText(f"disculpas: {self.idioma_portugues.perdon()}")
                self.pedir_cafe.setText(f"pedir cafe: {self.idioma_portugues.pedirCafe()}")
                self.pedir_precio.setText(f"pedir precio: {self.idioma_portugues.cuantoCuesta()}")
                self.pedir_ubicacion.setText(f"preguntar ubicacion: {self.idioma_portugues.dondeQueda()}")
            else:
                QMessageBox.critical(self,"error","seleccione entre los idiomas disponibles")
        finally:
            pass

app=QApplication(sys.argv)
m=MainWindows()
m.show()
app.exec()