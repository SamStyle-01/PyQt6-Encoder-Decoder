from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QMessageBox,\
    QFileDialog, QWidget, QPushButton, QStackedWidget, QLabel, QCheckBox
import sys

class SamStackWidget(QStackedWidget):
    def __init__(self, *args):
        super().__init__()
        self.setWindowTitle("Шифратор-дешифратор")

        for el in args:
            self.addWidget(el)

        self.setFixedSize(310, 470)


class SamMainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(310, 470)
        self.setStyleSheet("background-color: #157F4D")

        self.btn0 = QPushButton("Инструкция", self)
        self.btn1 = QPushButton("Создать и зашифровать файл", self)
        self.btn2 = QPushButton("Прочесть зашифрованный файл", self)
        self.btn3 = QPushButton("Зашифровать существующий файл", self)
        self.btn4 = QPushButton("Расшифровать существующий файл", self)
        self.btn5 = QPushButton("Дополнить существующий файл", self)

        self.btn0.setStyleSheet("background-color: #443355")
        self.btn1.setStyleSheet("background-color: #443355")
        self.btn2.setStyleSheet("background-color: #443355")
        self.btn3.setStyleSheet("background-color: #443355")
        self.btn4.setStyleSheet("background-color: #443355")
        self.btn5.setStyleSheet("background-color: #443355")

        self.btn0.setGeometry(50, 30, 220, 50)
        self.btn1.setGeometry(50, 100, 220, 50)
        self.btn2.setGeometry(50, 170, 220, 50)
        self.btn3.setGeometry(50, 240, 220, 50)
        self.btn4.setGeometry(50, 310, 220, 50)
        self.btn5.setGeometry(50, 380, 220, 50)

        self.btn0.clicked.connect(window0)
        self.btn1.clicked.connect(window1)
        self.btn2.clicked.connect(window2)
        self.btn3.clicked.connect(window3)
        self.btn4.clicked.connect(window4)
        self.btn5.clicked.connect(window5)


class SamMainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 500)
        self.setStyleSheet("background-color: #157F4D")

        self.frame = QWidget(self)
        self.frame.setGeometry(5, 5, 500, 455)
        self.text_in = QTextEdit(self.frame)
        self.text_in.setGeometry(0, 0, 500, 455)
        self.text_in.setPlainText("Введите текст...")
        self.frame.setStyleSheet("background-color: #443355")

        self.lbl1 = QLabel("Введите код:", self)
        self.lbl1.move(542, 25)

        self.lbl2 = QLabel("Введите x-число:", self)
        self.lbl2.move(534, 80)

        self.code = QLineEdit(self)
        self.code.setStyleSheet("background-color: #443355")
        self.code.setGeometry(520, 50, 125, 30)

        self.x_num = QLineEdit(self)
        self.x_num.setStyleSheet("background-color: #443355")
        self.x_num.move(532, 105)

        self.btn1 = QPushButton("Назад", self)
        self.btn2 = QPushButton("Создать файл", self)

        self.btn1.clicked.connect(back01)
        self.btn2.clicked.connect(create_file)

        self.btn1.setStyleSheet("background-color: #443355")
        self.btn2.setStyleSheet("background-color: #443355")

        self.btn1.move(5, 465)
        self.btn2.move(545, 465)


class SamMainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 500)
        self.setStyleSheet("background-color: #157F4D")

        self.frame = QWidget(self)
        self.frame.setGeometry(5, 5, 500, 455)
        self.text_in = QTextEdit(self.frame)
        self.text_in.setGeometry(0, 0, 500, 455)
        self.frame.setStyleSheet("background-color: #443355")
        self.text_in.setReadOnly(True)

        self.lbl1 = QLabel("Введите код:", self)
        self.lbl1.move(542, 25)

        self.code = QLineEdit(self)
        self.code.setStyleSheet("background-color: #443355")
        self.code.setGeometry(520, 50, 125, 30)

        self.btn1 = QPushButton("Назад", self)
        self.btn2 = QPushButton("Открыть", self)

        self.btn1.clicked.connect(back02)
        self.btn2.clicked.connect(read_coded_file)

        self.btn1.setStyleSheet("background-color: #443355")
        self.btn2.setStyleSheet("background-color: #443355")

        self.btn1.move(5, 465)
        self.btn2.move(545, 465)


class SamMainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(320, 150)
        self.setStyleSheet("background-color: #157F4D")

        self.using_file = ""

        self.btn1 = QPushButton("Выбрать файл", self)
        self.btn1.setStyleSheet("background-color: #443355")
        self.btn1.setGeometry(195, 20, 100, 40)
        self.btn1.clicked.connect(choose_file1)

        self.btn2 = QPushButton("Зашифровать", self)
        self.btn2.setStyleSheet("background-color: #443355")
        self.btn2.setGeometry(195, 60, 100, 40)
        self.btn2.clicked.connect(code_file)

        self.code_l = QLabel("Код:", self)
        self.code_l.setGeometry(12, 20, 80, 30)

        self.code = QLineEdit(self)
        self.code.setStyleSheet("background-color: #443355")
        self.code.setGeometry(40, 20, 140, 30)

        self.x_num_l = QLabel("X-число:", self)
        self.x_num_l.setGeometry(12, 65, 80, 30)

        self.x_num = QLineEdit(self)
        self.x_num.setStyleSheet("background-color: #443355")
        self.x_num.setGeometry(70, 65, 70, 30)

        self.btn3 = QPushButton("Назад", self)
        self.btn3.setStyleSheet("background-color: #443355")
        self.btn3.setGeometry(15, 110, 75, 30)
        self.btn3.clicked.connect(back03)

        self.line_ed = QLineEdit(self)
        self.line_ed.move(80, 160)


class SamMainWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(320, 150)
        self.setStyleSheet("background-color: #157F4D")

        self.using_file = ""

        self.btn1 = QPushButton("Выбрать файл", self)
        self.btn1.setStyleSheet("background-color: #443355")
        self.btn1.setGeometry(195, 20, 100, 40)
        self.btn1.clicked.connect(choose_file2)

        self.btn2 = QPushButton("Расшифровать", self)
        self.btn2.setStyleSheet("background-color: #443355")
        self.btn2.setGeometry(195, 60, 100, 40)
        self.btn2.clicked.connect(decode_file)

        self.code_l = QLabel("Код:", self)
        self.code_l.setGeometry(12, 20, 80, 30)

        self.code = QLineEdit(self)
        self.code.setStyleSheet("background-color: #443355")
        self.code.setGeometry(40, 20, 140, 30)

        self.btn3 = QPushButton("Назад", self)
        self.btn3.setStyleSheet("background-color: #443355")
        self.btn3.setGeometry(15, 110, 75, 30)
        self.btn3.clicked.connect(back04)

        self.line_ed = QLineEdit(self)
        self.line_ed.move(80, 160)


class SamMainWindow6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 500)
        self.setStyleSheet("background-color: #157F4D")

        self.frame = QWidget(self)
        self.frame.setGeometry(5, 5, 500, 455)
        self.text_in = QTextEdit(self.frame)
        self.text_in.setGeometry(0, 0, 500, 455)
        self.text_in.setPlainText("Введите текст...")
        self.frame.setStyleSheet("background-color: #443355")

        self.lbl1 = QLabel("Введите код:", self)
        self.lbl1.move(542, 25)

        self.lbl2 = QLabel("Перенос строки", self)
        self.lbl2.setGeometry(535, 125, 150, 30)

        self.code = QLineEdit(self)
        self.code.setStyleSheet("background-color: #443355")
        self.code.setGeometry(520, 50, 125, 30)

        self.btn1 = QPushButton("Назад", self)
        self.btn2 = QPushButton("Дополнить файл", self)
        self.chbtn0 = QCheckBox(self)
        self.chbtn0.setChecked(True)

        self.btn1.clicked.connect(back05)
        self.btn2.clicked.connect(update_file)

        self.btn1.setStyleSheet("background-color: #443355")
        self.btn2.setStyleSheet("background-color: #443355")

        self.btn1.move(5, 465)
        self.btn2.move(545, 465)
        self.chbtn0.move(575, 150)


class SamInstruction(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 500)
        self.setStyleSheet("background-color: #157F4D")

        self.frame = QWidget(self)
        self.frame.setGeometry(5, 5, 640, 455)
        self.text_in = QTextEdit(self.frame)
        self.text_in.setGeometry(0, 0, 640, 455)
        self.frame.setStyleSheet("background-color: #443355")
        self.text_in.setReadOnly(True)
        self.text_in.setPlainText("1. Опция \"Создать и зашифровать файл\". Здесь вы можете ввести текст, после чего "\
                                  "вы сможете его тут же зашифровать и сохранить получившийся шифр в файл.\n\n"\
                                  "2. Опция \"Прочесть зашифрованный файл\". Вы можете прочитать шифр из файла, "\
                                  "но при этом сам файл изменяться не будет. Вы просто просматриваете информацию " \
                                  "в нём.\n\n3. Опция \"Зашифровать существующий файл\". Похож на 1 опцию, но отличие "\
                                  "в том, что текст вы не вводите, а автоматически берёте из файла. И туда же " \
                                  "(в этот же файл) записываете его в зашифрованном виде.\n\n4. Опция \"Расшифровать "\
                                  "существующий файл\". Похож на 2 опцию, но в этом случае вы не выводите всё на "\
                                  "экран, а сразу расшифровываете прямо в файле.\n\n"\
                                  "5. Опция \"Дополнить существующий файл\". В уже созданный ранее зашифрованный файл "\
                                  "вы можете добавить какое-то количество требуемых вам строк, символов и т.д. "\
                                  "Кнопка \"Перенос строки\" определяет, будет ли начинаться ваше дополнение "\
                                  "в зашифрованном тексте с новой строки или нет. По умолчанию перенос включен.\n\n"\
                                  "6. Параметр x-числа имеет границы. Во-первых, это должно быть целочисленное "\
                                  "значение. Во-вторых, число должно быть в "\
                                  "диапозоне от 1 до 100 включительно. Во всех иных случаях будет ошибка. "\
                                  "Само x-число запоминать не нужно.\n\n"\
                                  "7. Кодом могут быть цифры, буквы, некоторые символы, слово, несколько слов и т.д. "\
                                  "Выбор кодового слова по большей части мало чем ограничивается. "\
                                  "Код нужно запомнить. Без него данные станут недоступны.\n\n"\
                                  "8. Для нормальной работы программы используйте текстовые файлы в кодировке "\
                                  "UTF-8. Это кодировка в текстовом файле Windows по умолчанию. "\
                                  "Просто не изменяйте её.")

        self.btn1 = QPushButton("Назад", self)

        self.btn1.clicked.connect(back00)

        self.btn1.setStyleSheet("background-color: #443355")

        self.btn1.move(5, 465)


def create_file():
    text, code, x_num = window01.text_in.toPlainText(), window01.code.text(), window01.x_num.text()
    if (text == "" or code == "" or x_num == "" or any((c.isalpha() for c in x_num))):
        QMessageBox.warning(window01, "Неверные данные", "Вы ввели некорректные данные.")
        return
    if int(x_num) > 100 or int(x_num) < 1:
        QMessageBox.critical(window03, "Неверные данные", "x-число должно быть в диапозоне от 1 до 101.")
        return
    path, b_p = QFileDialog.getSaveFileName(window01, "Создать и зашифровать файл", first_path, "Text File (*.txt)")
    if (b_p):
        x_num = int(x_num)
        file = open(path, "w", encoding='utf-8')
        for i in range(len(code)):
            file.write(str(bin(ord(code[i]) * x_num * multiples[len(multiples) - (i % len(multiples)) - 1] - 1))[2:])
            if i < len(code) - 1:
                file.write(" ")
        file.write("\n")
        file.write(str(bin(x_num * 1824 - 1799))[2:] + "\n")
        file.write(code_it(text, code, x_num))
        file.close()
        QMessageBox.information(window01, "Операция завершена", "Файл был создан и закодирован.")
        window01.text_in.setPlainText(str())
        window01.code.setText(str())
        window01.x_num.setText(str())


def read_coded_file():
    user_code = window02.code.text()
    if user_code == "":
        QMessageBox.critical(window02, "Некорректные данные", "Вы оставили поле для кода пустым.")
        return
    path, b_p = QFileDialog.getOpenFileName(window02, "Прочитать зашифрованный файл", first_path, "Text File (*.txt)")
    if (b_p):
        file = open(path, "r", encoding='utf-8')
        try:
            code_source = [int(i, 2) for i in file.readline()[:-1].split()]
        except:
            QMessageBox.critical(window02, "Что-то пошло не так", "Неверный или повреждённый файл.")
            return
        x_num = int((int(file.readline()[:-1], 2) + 1799) / 1824)
        code = str()
        for i in range(len(code_source)):
            code += chr(int((code_source[i] + 1) / (x_num * multiples[len(multiples) - (i % len(multiples)) - 1])))
        if user_code != code:
            QMessageBox.critical(window02, "В доступе отказано", "Был введён неверный ключ.")
            return
        source_text = file.read()
        text = decode_it(source_text, code, x_num)
        file.close()
        window02.text_in.setPlainText(text)
        QMessageBox.information(window02, "Операция завершена", "Файл был открыт и расшифрован.")


def code_file():
    code, x_num = window03.code.text(), window03.x_num.text()
    if code == "" or x_num == "" or any((c.isalpha() for c in x_num)):
        QMessageBox.critical(window03, "Неверные данные", "Вы оставили поле для кода пустым.")
        return
    if int(x_num) > 100 or int(x_num) < 1:
        QMessageBox.critical(window03, "Неверные данные", "x-число должно быть в диапозоне от 1 до 101.")
        return
    if window03.using_file == "":
        QMessageBox.critical(window03, "Не указан файл", "Вы не указали путь к файлу.")
        return
    x_num = int(x_num)
    file0 = open(window03.using_file, "r", encoding='utf-8')
    text = file0.read()
    file0.close()
    file = open(window03.using_file, "w", encoding='utf-8')
    for i in range(len(code)):
        file.write(str(bin(ord(code[i]) * x_num * multiples[len(multiples) - (i % len(multiples)) - 1] - 1))[2:])
        if i < len(code) - 1:
            file.write(" ")
    file.write("\n")
    file.write(str(bin(x_num * 1824 - 1799))[2:] + "\n")
    file.write(code_it(text, code, x_num))
    file.close()
    QMessageBox.information(window03, "Операция завершена", "Файл был закодирован.")
    window03.code.setText(str())
    window03.x_num.setText(str())
    window03.using_file = ""


def decode_file():
    user_code = window04.code.text()
    if user_code == "":
        QMessageBox.critical(window04, "Некорректные данные", "Вы ввели некорректные данные.")
        return
    if window04.using_file == "":
        QMessageBox.critical(window04, "Не указан файл", "Вы не указали путь к файлу.")
        return
    file = open(window04.using_file, "r", encoding='utf-8')
    try:
        code_source = [int(i, 2) for i in file.readline()[:-1].split()]
    except:
        QMessageBox.critical(window04, "Что-то пошло не так", "Неверный или повреждённый файл.")
        return
    x_num = int((int(file.readline()[:-1], 2) + 1799) / 1824)
    code = str()
    for i in range(len(code_source)):
        code += chr(int((code_source[i] + 1) / (x_num * multiples[len(multiples) - (i % len(multiples)) - 1])))
    if user_code != code:
        QMessageBox.critical(window04, "В доступе отказано", "Был введён неверный ключ.")
        return
    source_text = file.read()
    text = decode_it(source_text, code, x_num)
    file.close()
    file0 = open(window04.using_file, "w", encoding='utf-8')
    file0.write(text)
    file0.close()
    window04.using_file = ""
    QMessageBox.information(window04, "Операция завершена", "Файл был расшифрован.")


def update_file():
    user_code = window05.code.text()
    if user_code == "":
        QMessageBox.critical(window05, "Некорректные данные", "Вы оставили поле для кода пустым.")
        return
    path, b_p = QFileDialog.getOpenFileName(window05, "Дополнить зашифрованный файл", first_path, "Text File (*.txt)")
    if (b_p):
        file = open(path, "r", encoding='utf-8')
        try:
            code_source = [int(i, 2) for i in file.readline()[:-1].split()]
        except:
            QMessageBox.critical(window02, "Что-то пошло не так", "Неверный или повреждённый файл.")
            return
        x_num = int((int(file.readline()[:-1], 2) + 1799) / 1824)
        code = str()
        for i in range(len(code_source)):
            code += chr(int((code_source[i] + 1) / (x_num * multiples[len(multiples) - (i % len(multiples)) - 1])))
        if user_code != code:
            QMessageBox.critical(window05, "В доступе отказано", "Был введён неверный ключ.")
            return
        file.close()
        file0 = open(path, "a", encoding='utf-8')
        if window05.chbtn0.isChecked():
            file0.write(code_it("\n", code, x_num))
        file0.write(code_it(window05.text_in.toPlainText(), code, x_num))
        file0.close()
        QMessageBox.information(window05, "Операция завершена", "Файл был дополнен.")
        window05.code.setText(str())
        window05.text_in.setPlainText(str())


def choose_file1():
    window03.using_file, _ = QFileDialog.getOpenFileName(window03, "Укажите файл для зашифровки", first_path,\
                                                         "Text File (*.txt)")

def choose_file2():
    window04.using_file, _ = QFileDialog.getOpenFileName(window04, "Укажите файл для зашифровки", first_path,\
                                                         "Text File (*.txt)")


def window1():
    window01.show()
    stack.setFixedSize(650, 500)
    main_window.hide()


def back01():
    main_window.show()
    stack.setFixedSize(310, 470)
    window01.hide()
    window01.text_in.setPlainText("Введите текст...")
    window01.code.setText(str())
    window01.x_num.setText(str())


def window2():
    window02.show()
    stack.setFixedSize(650, 500)
    main_window.hide()


def back02():
    main_window.show()
    stack.setFixedSize(310, 470)
    window02.hide()
    window02.text_in.setPlainText(str())
    window02.code.setText(str())


def window3():
    window03.show()
    stack.setFixedSize(320, 150)
    main_window.hide()


def back03():
    main_window.show()
    stack.setFixedSize(310, 470)
    window03.hide()
    window03.code.setText(str())
    window03.x_num.setText(str())
    window03.using_file = ""


def window4():
    window04.show()
    stack.setFixedSize(320, 150)
    main_window.hide()


def back04():
    main_window.show()
    stack.setFixedSize(310, 470)
    window04.hide()
    window04.code.setText(str())
    window04.using_file = ""


def window0():
    window00.show()
    stack.setFixedSize(650, 500)
    main_window.hide()


def back00():
    main_window.show()
    stack.setFixedSize(310, 470)
    window00.hide()


def window5():
    window05.show()
    stack.setFixedSize(650, 500)
    main_window.hide()


def back05():
    main_window.show()
    stack.setFixedSize(310, 470)
    window05.hide()
    window05.text_in.setPlainText("Введите текст...")
    window05.code.setText(str())
    window05.chbtn0.setChecked(True)


multiples = (5, 18, 9, 4, 6, 11, 8, 14, 22, 31, 28, 20, 10, 6, 15, 3, 2, 13)
first_path = "C:\\"

def code_it(text, code, x_num):
    result = str()
    for let_txt in text:
        for num_code in range(len(code)):
            result += str(bin(ord(let_txt) * ord(code[num_code]) * multiples[num_code % len(multiples)] * x_num))[2:]
            result += " "
        result += "\n"
    return result


def decode_it(coded_text, code, x_num):
    sum_code = 0
    for i in range(len(code)):
        sum_code += ord(code[i]) * multiples[i % len(multiples)]
    result = str()
    temp_str = str()
    for i in range(len(coded_text)):
        if (coded_text[i] == "\n"):
            temp_nums = temp_str.split()
            temp_str = str()

            temp_sum = sum([int(el, 2) for el in temp_nums])
            result += chr(int(temp_sum / sum_code / x_num))
        else:
            temp_str += coded_text[i]
    return result

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = SamMainWindow1()
    window01 = SamMainWindow2()
    window02 = SamMainWindow3()
    window03 = SamMainWindow4()
    window04 = SamMainWindow5()
    window05 = SamMainWindow6()
    window00 = SamInstruction()

    stack = SamStackWidget(main_window, window01, window02, window03, window04, window05, window00)

    stack.show()
    sys.exit(app.exec())