from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle


class Question():
    def __init__(self,question,right_answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question # Вопрос.
        self.right_answer = right_answer # Правильный ответ
        self.wrong_answer1 = wrong_answer1 # Неправильный ответ 1
        self.wrong_answer2 = wrong_answer2 # Неправильный ответ 2
        self.wrong_answer3 = wrong_answer3 # Неправильный ответ 3

questions_list = [] 



questions_list.append(Question("Вы носите маску?","Да","Нет","Иногда","Никогда"))
questions_list.append(Question("Вы работаете качественно?","Всегда","Редко","Иногда","Никогда"))
questions_list.append(Question("Вы платите налоги?","Да","Нет","Иногда","Никогда"))
questions_list.append(Question("Вы отдаёте деньги на благотворительность?","Да","Нет","Иногда","Никогда"))
questions_list.append(Question("Вы даёте деньги нищим?","Да","Нет","Иногда","Никогда"))

questions_list.append(Question("Вы поддерживаете президента России?","Да","Нет","Иногда","Никогда"))
questions_list.append(Question("Вы вакцинированы?","Да","Нет","Не хочу","Буду вакцинирован(а)"))
questions_list.append(Question("Вы переболели Covid-19?","Да","Нет","Давно","Ещё нет"))
questions_list.append(Question("Вы хотите быть президентом?","Да","Нет","Иногда","Никогда"))
questions_list.append(Question("Во время опроса вы отвечали чесно?","Да","Нет","Иногда","Никогда"))


app = QApplication([])



window = QWidget()
window.setWindowTitle('Опрос от Госуслуги')
 
'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа 

lb_Question = QLabel('Вам хорошо платят на вашей работе?') # текст вопроса
 
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('Очень хорошо')
rbtn_2 = QRadioButton('Плохо')
rbtn_3 = QRadioButton('Не платят')
rbtn_4 = QRadioButton("Совсе немного")

ResultGroupBox = QGroupBox("Результат ответа")
lb_result = QLabel("Правильно/Непревильно")
lb_correct = QLabel("Правильный ответ")

layout_res = QVBoxLayout()
layout_res = QVBoxLayout(lb_correct)
layout_res.addWidget(lb_result)
ResultGroupBox.setLayout(layout_res)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
 
RadioGroupBox.setLayout(layout_ans1) # готова "панель"
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
 
layout_line2.addWidget(ResultGroupBox)
ResultGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 




# ----------------------------------------------------------
# Виджеты и макеты созданы, далее - функции:
# ----------------------------------------------------------

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):
    lb_Question.setText(q.question)
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_answer1)
    answers[2].setText(q.wrong_answer2)
    answers[3].setText(q.wrong_answer3)

q = Question('Вам хорошо платят на вашей работе?','Очень хорошо','Плохо','Не платят',"Совсе немного")

ask(q)


def check_asw():
    if answers[0].isChecked():
        print("Правильный ответ")
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        print("Неправильно")
    else:
        print("Вы не выбрали ни одного варианта ответа")

def show_result():
    ResultGroupBox.show()
    RadioGroupBox.hide()
    btn_OK.setText("Следующий вопрос")

def next_question():
    ResultGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Ответить")

#def test():
#    if btn_OK.text() == "Ответить":
#        show_result()   
#    else:
#       next_question()





btn_OK.clicked.connect(check_asw)
#btn_OK.clicked.connect(test)
window.setLayout(layout_card)
window.show()
app.exec()