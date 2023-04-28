from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup,
                             QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QMessageBox, QGroupBox)

class Question():
    def __init__(self, question_text, right_answer, wrong1, wrong2, wrong3):
        self.q_text = question_text
        self.r_answer = right_answer
        
