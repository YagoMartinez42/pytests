from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox)

def checkAnswer():
    if rbtn_2.isChecked():
        answer.setText('¡Correcto!')
    else:
        answer.setText('No es correcto')

        answer.show()
    app = QApplication([])
    main_win = QWidget()

    main_win.setWindowTitle('Trivia card')
    answButton = QPushButton('Respuesta')
    question = QLabel('¿Qué nacionalidad no existe?')
    answer = QLabel('')

    RadioGroupBox = QGroupBox("Opciones de respuesta")
    rbtn_1 = QRadioButton('Enets')
    rbtn_2 = QRadioButton('Pitufos')
    rbtn_3 = QRadioButton('Chulyms')
    rbtn_4 = QRadioButton('Aleutas')
    layout_ans1 = QHBoxLayout()   
    layout_ans2 = QVBoxLayout() 
    layout_ans3 = QVBoxLayout()
    layout_ans2.addWidget(rbtn_1) 
    layout_ans2.addWidget(rbtn_2)
    layout_ans3.addWidget(rbtn_3) 
    layout_ans3.addWidget(rbtn_4)
    layout_ans1.addLayout(layout_ans2)
    layout_ans1.addLayout(layout_ans3)
    RadioGroupBox.setLayout(layout_ans1)

    answButton.clicked.connect(checkAnswer)

    line = QVBoxLayout()
    line.addWidget(question, alignment = Qt.AlignCenter)
    line.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
    line.addWidget(answButton, alignment = Qt.AlignCenter, stretch = 3)
    line.addWidget(answer, alignment = Qt.AlignCenter)
    answer.hide()
    line.setSpacing(15)
    main_win.setLayout(line)

    main_win.show()
    app.exec_()
