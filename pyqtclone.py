from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Trivia card')
 
main_win.setWindowTitle('Text Cloning')
main_win.entry1 = QLineEdit()
main_win.entry2 = QLineEdit()
main_win.layout().addWidget(self.entry1)
main_win.layout().addWidget(self.entry2)
main_win.entry1.textChanged.connect(self.entry2.setText)

main_win.show()


app.exec_()
