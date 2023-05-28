import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QComboBox, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox

class HexCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memory = ['0'] * 4
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Калькулятор в 16-й с.с.')

        # Экземпляр класса QTBoxLayout для управления расположениями виджетов
        main_layout = QVBoxLayout()

        # Создание виджетов для ввода чисел и вывода результата операций над числами
        self.hex_input1 = QLineEdit(self)
        self.hex_input1.setText("Например: F4240")
        self.hex_input2 = QLineEdit(self)
        self.hex_input2.setText("Например: 7A120")
        self.hex_result = QLineEdit(self)
        self.hex_result.setReadOnly(True)

        # Обозначения полей
        main_layout.addWidget(QLabel('Первое число:'))
        main_layout.addWidget(self.hex_input1)
        main_layout.addWidget(QLabel('Второе число:'))
        main_layout.addWidget(self.hex_input2)
        main_layout.addWidget(QLabel('Результат:'))
        main_layout.addWidget(self.hex_result)

        # Создание кнопок с действиями над числами
        add_button = QPushButton('Прибавить', self)
        add_button.clicked.connect(self.add)
        sub_button = QPushButton('Вычесть', self)
        sub_button.clicked.connect(self.subtract)
        mul_button = QPushButton('Умножить', self)
        mul_button.clicked.connect(self.multiply)
        div_button = QPushButton('Разделить', self)
        div_button.clicked.connect(self.divide)

        # Горизонтально распологаем кнопки действий с помощью модуля QHBoxLayout()
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(sub_button)
        buttons_layout.addWidget(mul_button)
        buttons_layout.addWidget(div_button)
        main_layout.addLayout(buttons_layout)

        # Добавление ячеек памяти в список QComboBox с помощью экземпляра класса
        self.memory_combo = QComboBox(self)
        for i in range(4):
            self.memory_combo.addItem(f'Ячейка памяти {i + 1}')
        # Добавление заголовка списка и сам список в главный компоновщик
        main_layout.addWidget(QLabel('Память:'))
        main_layout.addWidget(self.memory_combo)

        # Создание кнопок для сохранения и вызова результат операций, и связка кнопок с соответствующими методами
        store_button = QPushButton('Сохранить', self)
        store_button.clicked.connect(self.store_memory)
        recall_button = QPushButton('Вызвать', self)
        recall_button.clicked.connect(self.recall_memory)

        # Горизонтальное расположение кнопок и их добавление в главный компоновщик
        memory_buttons_layout = QHBoxLayout()
        memory_buttons_layout.addWidget(store_button)
        memory_buttons_layout.addWidget(recall_button)
        main_layout.addLayout(memory_buttons_layout)

        # Создание заголовка для вывода результата операций в 10-й с.с.
        self.dec_result = QLineEdit(self)
        self.dec_result.setReadOnly(True)

        main_layout.addWidget(QLabel('Результат в 10-й с.с:'))
        main_layout.addWidget(self.dec_result)

        # Создание главного виджета, на котором будут расположены все остальные виджеты
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add(self):
        try:
            # конвертация чисел из 16 с.с в 10 с.с
            num1 = int(self.hex_input1.text(), 16)
            num2 = int(self.hex_input2.text(), 16)
            result = num1 + num2
            self.hex_result.setText(hex(result)[2:].upper())
            self.dec_result.setText(str(result))
        except ValueError:
            self.hex_result.setText('Неправильно введены данные!')

    def subtract(self):
        try:
            num1 = int(self.hex_input1.text(), 16)
            num2 = int(self.hex_input2.text(), 16)
            result = num1 - num2
            self.hex_result.setText(hex(result)[2:].upper())
            self.dec_result.setText(str(result))
        except ValueError:
            self.hex_result.setText('Неправильно введены данные!')

    def multiply(self):
        try:
            num1 = int(self.hex_input1.text(), 16)
            num2 = int(self.hex_input2.text(), 16)
            result = num1 * num2
            self.hex_result.setText(hex(result)[2:].upper())
            self.dec_result.setText(str(result))
        except ValueError:
            self.hex_result.setText('Неправильно введены данные!')

    def divide(self):
        try:
            num1 = int(self.hex_input1.text(), 16)
            num2 = int(self.hex_input2.text(), 16)
            if num2 != 0:
                result = num1 // num2
                self.hex_result.setText(hex(result)[2:].upper())
                self.dec_result.setText(str(result))
            else:
                self.hex_result.setText('Нельзя делить на ноль!')
        except ValueError:
            self.hex_result.setText('Неправильно введены данные!')

    def store_memory(self):
        # Получение текущего индекса выбранного элемента из виджета QComboBox
        index = self.memory_combo.currentIndex()
        # Сохранение результата операции с текущим индексом
        self.memory[index] = self.hex_result.text()

    def recall_memory(self):
        # Получение текущего индекса выбранного элемента из виджета QComboBox
        index = self.memory_combo.currentIndex()

        # Создание диалогового окна для выбора аргумента
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Выбор аргумента")
        msgBox.setText("Какой аргумент нужно обновить?")
        msgBox.addButton("1", QMessageBox.YesRole)
        msgBox.addButton("2", QMessageBox.NoRole)
        result = msgBox.exec_()

        # Выбор соответствующего аргумента в зависимости от выбора пользователя
        if result == 0:
            # Обновление первого аргумента
            self.hex_input1.setText(self.memory[index])
        elif result == 1:
            # Обновление второго аргумента
            self.hex_input2.setText(self.memory[index])


def main():
    app = QApplication(sys.argv)
    hex_calc = HexCalculator()
    hex_calc.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()