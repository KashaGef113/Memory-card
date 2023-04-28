# создай приложение для запоминания информации
from random import shuffle
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
questions_list.append(q3)

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory card')

question = QLabel()
btn_OK = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов:')

rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()

ans_v_line_1 = QVBoxLayout()
ans_v_line_2 = QVBoxLayout()
ans_h_line = QHBoxLayout()

ans_v_line_1.addWidget(rbtn_1)
ans_v_line_1.addWidget(rbtn_2)
ans_v_line_2.addWidget(rbtn_3)
ans_v_line_2.addWidget(rbtn_4)

ans_h_line.addLayout(ans_v_line_1)
ans_h_line.addLayout(ans_v_line_2)

RadioGroupBox.setLayout(ans_h_line)

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# форма ответа

AnsGroupBox = QGroupBox()
result = QLabel()
correct = QLabel()
res_v_line = QVBoxLayout()
res_v_line.addWidget(result, alignment=(Qt.AlignTop | Qt.AlignLeft))
res_v_line.addWidget(correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(res_v_line)
#####################

question_h_line = QHBoxLayout()
group_h_line = QHBoxLayout()
btn_h_line = QHBoxLayout()

question_h_line.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
group_h_line.addWidget(RadioGroupBox)
group_h_line.addWidget(AnsGroupBox)
AnsGroupBox.hide()

btn_h_line.addStretch(1)
btn_h_line.addWidget(btn_OK, stretch=2)
btn_h_line.addStretch(1)

main_v_line = QVBoxLayout()
main_v_line.addLayout(question_h_line)
main_v_line.addLayout(group_h_line)
main_v_line.addLayout(btn_h_line)

main_win.setLayout(main_v_line)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)





answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q):
    shuffle(answers)
    question.setText(q.q_text)
    answers[0].setText(q.r_answer)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    correct.setText(q.r_answer)
    show_question()

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Не правильно!')

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question == len(questions_list):
        main_win.cur_question = 0
    q = questions_list[main_win.cur_question]
    ask(q)

def test():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


btn_OK.clicked.connect(test)
main_win.cur_question = -1
next_question()
main_win.show()
app.exec()
