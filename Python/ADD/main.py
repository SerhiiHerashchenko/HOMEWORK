import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, 
    QCheckBox, QRadioButton, QSlider, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt


class SurveyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Оценка преподавания курса Python")
        self.setGeometry(100, 100, 500, 400)
        
        self.init_ui()

    def init_ui(self):
        # Основной виджет
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Макет для размещения виджетов
        layout = QVBoxLayout()

        # Вопрос 1: Как вас зовут? (Текстовое поле)
        layout.addWidget(QLabel("1. Как вас зовут?"))
        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_input)

        # Вопрос 2: Вам понравился курс? (Флажки)
        layout.addWidget(QLabel("2. Вам понравился курс?"))
        self.like_check = QCheckBox("Да, мне всё понравилось", self)
        self.like_check2 = QCheckBox("Не всё понравилось, есть замечания", self)
        layout.addWidget(self.like_check)
        layout.addWidget(self.like_check2)

        # Вопрос 3: Оцените качество преподавания (Радиокнопки)
        layout.addWidget(QLabel("3. Как вы оцениваете качество преподавания?"))
        self.radio_good = QRadioButton("Отлично", self)
        self.radio_average = QRadioButton("Хорошо", self)
        self.radio_poor = QRadioButton("Удовлетворительно", self)
        layout.addWidget(self.radio_good)
        layout.addWidget(self.radio_average)
        layout.addWidget(self.radio_poor)

        # Вопрос 4: Насколько сложным был курс? (Слайдер)
        layout.addWidget(QLabel("4. Какой уровень сложности вы бы поставили курсу? (1 - Легкий, 10 - Очень сложный)"))
        self.difficulty_slider = QSlider(Qt.Horizontal, self)
        self.difficulty_slider.setMinimum(1)
        self.difficulty_slider.setMaximum(10)
        self.difficulty_slider.setValue(5)
        layout.addWidget(self.difficulty_slider)

        # Вопрос 5: Что вы хотите улучшить? (Выпадающий список)
        layout.addWidget(QLabel("5. Что бы вы хотели улучшить?"))
        self.improve_combo = QComboBox(self)
        self.improve_combo.addItems([
            "Больше практических задач",
            "Лучше объяснять теорию",
            "Добавить материалы для самостоятельного изучения",
            "Улучшить обратную связь от преподавателя"
        ])
        layout.addWidget(self.improve_combo)

        # Кнопка отправки
        self.submit_button = QPushButton("Отправить", self)
        self.submit_button.clicked.connect(self.show_result)
        layout.addWidget(self.submit_button)

        # Устанавливаем макет
        self.central_widget.setLayout(layout)

    def show_result(self):
        # Сбор ответов
        name = self.name_input.text()
        like = self.like_check.isChecked()
        like_partial = self.like_check2.isChecked()

        if self.radio_good.isChecked():
            quality = "Отлично"
        elif self.radio_average.isChecked():
            quality = "Хорошо"
        elif self.radio_poor.isChecked():
            quality = "Удовлетворительно"
        else:
            quality = "Не выбрано"

        difficulty = self.difficulty_slider.value()
        improve = self.improve_combo.currentText()

        # Создаем сообщение с результатами
        result = (
            f"Спасибо за участие, {name}!\n\n"
            f"Ваши ответы:\n"
            f"- Курс понравился: {'Да' if like else 'Нет' if not like_partial else 'Частично'}\n"
            f"- Качество преподавания: {quality}\n"
            f"- Уровень сложности: {difficulty}\n"
            f"- Что вы хотите улучшить: {improve}"
        )

        # Показываем сообщение
        QMessageBox.information(self, "Результаты опроса", result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SurveyApp()
    window.show()
    sys.exit(app.exec_())
