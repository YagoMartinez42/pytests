from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox)
from random import shuffle

class Question():
    def __init__(
self, question, right_answer, 
wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(
Question('¿Qué nacionalidad no existe?', 
'Smurfs', 'Enets', 'Chulyms', 'Aleutas'))
questions_list.append(
Question('El idioma nacional de Portugal', 
'Portugués', 'Inglés', 'Español', 'Francés'))
questions_list.append(
Question('¿Qué color no está en la bandera de Italia?', 
'Azul', 'Verde', 'Rojo', 'Blanco'))
questions_list.append(
Question('¿Sobre qué camina un funambulista?', 
'Cuerda tensa', 'Brasas', 'Clavos', 'Hielo'))

def ask(q: Question):
    shuffle(answers)
    questionLbl.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    answerLbl.hide()
    answButton.clicked.connect(checkAnswer)
    answButton.setText('Responder')

def nextQuest():
    window.curQuestion += 1
    if window.curQuestion >= len(questions_list):
        window.curQuestion = 0
    ask(questions_list[window.curQuestion])

def checkAnswer():
    if answers[0].isChecked():
        answer.setText('¡Correcto!')
    else:
        answer.setText('No es correcto')
    answerLbl.show()
    answButton.clicked.connect(nextQuest)
    answButton.setText('Siguiente pregunta')

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Trivia card')
answButton = QPushButton('Siguiente pregunta')
questionLbl = QLabel()
answerLbl = QLabel()
RadioGroupBox = QGroupBox('Opciones de respuesta')
rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()
layout_sqr1 = QHBoxLayout()   
layout_col1 = QVBoxLayout() 
layout_col2 = QVBoxLayout()
layout_col1.addWidget(rbtn_1) 
layout_col1.addWidget(rbtn_2)
layout_col2.addWidget(rbtn_3) 
layout_col2.addWidget(rbtn_4)
layout_sqr1.addLayout(layout_col1)
layout_sqr1.addLayout(layout_col2)
RadioGroupBox.setLayout(layout_sqr1)
line = QVBoxLayout()
line.addWidget(questionLbl, alignment = Qt.AlignCenter)
line.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
line.addWidget(answButton, alignment = Qt.AlignCenter, stretch = 3)
line.addWidget(answerLbl, alignment = Qt.AlignCenter)
answerLbl.hide()
line.setSpacing(15)
main_win.setLayout(line)

window.curQuestion = -1
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
answButton.clicked.connect(nextQuest)
main_win.show()
app.exec_()
