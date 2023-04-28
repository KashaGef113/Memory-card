from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup,
                             QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QMessageBox, QGroupBox)

class Question():
    def __init__(self, question_text, right_answer, wrong1, wrong2, wrong3):
        self.q_text = question_text
        self.r_answer = right_answer
        self.w1 = wrong1
        self.w2 = wrong2
        self.w3 = wrong3

questions_list = []
q1 = Question('Самая быстрая машина в мире?', 'Koenigsegg Jesko Absolut', 'Lamborghini Huracan', 'Bugatti Chiron', 'Ferrari')
q2 = Question('Самая дорогая машина в мире?', 'Ferrari 335 S Spider', 'Rolce Royse Fantom', 'Bugatti Veyron', 'Lamborghini Aventador')
q3 = Question('Самый мощный ноутбук в мире?', 'GPD Win Max 2', 'ASUS TUF', 'ASUS Rog', 'HP')
questions_list.append(q1)
questions_list.append(q2)
