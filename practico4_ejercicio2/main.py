import sys
import shutil
from PyQt6.QtWidgets import QDialog,QMainWindow,QApplication,QFileDialog,QLabel,QHBoxLayout,QVBoxLayout,QPushButton

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.setWindowTitle("Copiar Archivo")
        self.setGeometry(100, 100, 250, 200)

        # Abrir
        self.__message_label = QLabel("Selecciona un archivo:")
        self.__button_open = QPushButton("Examinar")
        self.__button_open.clicked.connect(self.open_file)

        # Guardar
        self.__message_label_2 = QLabel("Selecciona una ubicación de destino:")
        self.__button_save = QPushButton("Examinar")
        self.__button_save.clicked.connect(self.destination_folder)

        # Copiar
        self.__button_copy = QPushButton("Copiar")
        self.__button_save.clicked.connect(self.copy_file)

        # Viseño vertical
        layout = QVBoxLayout()
        layout.addWidget(self.__message_label)
        layout.addWidget(self.__button_open)
        layout.addWidget(self.__message_label_2)
        layout.addWidget(self.__button_save)
        layout.addWidget(self.__button_copy)
        self.setLayout(layout)

    def open_file(self):
        self.open, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos All Files (*);;Text Files (*.txt)")
        self.__message_label.setText(f"Ubicacion seleccionada: {self.open}")

    def destination_folder(self):
        self.save_folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta de destino")

    def copy_file(self):
        if self.open and self.save_folder:
            try:
                shutil.copy(self.open,self.save_folder)
                self.__message_label.setText("Archivo copiado con éxito.")
            except Exception as e:
                self.__message_label.setText(f"Error al copiar el archivo: {str(e)}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()