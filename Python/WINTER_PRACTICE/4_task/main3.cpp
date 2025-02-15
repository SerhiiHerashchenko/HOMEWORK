#include <iostream>
#include <fstream>
#include <cmath>

const double PI = M_PI;
const int NUM_POINTS = 5000; // Количество точек

// Параметр лемнискаты
const double a = 3;

// Функция генерации точек
void generate_data() {
    std::ofstream file("data.txt"); // Открываем файл для записи
    if (!file) {
        std::cerr << "Ошибка: не удалось создать файл данных!" << std::endl;
        return;
    }

    for (int i = 0; i < NUM_POINTS; ++i) {
        double theta = -PI + i * (2 * PI) / (NUM_POINTS - 1); // Углы от -π до π
        double r2 = 2 * a * a * cos(2 * theta); // r^2 = 2a^2 cos(2θ)

        if (r2 > 0) { // Проверяем, что r² > 0 (иначе r не определён)
            double r = sqrt(r2);
            double x = r * cos(theta);
            double y = r * sin(theta);
            file << x << " " << y << std::endl;
        } else {
            file << "\n"; // Добавляем пустую строку для разрыва
        }
    }

    file.close();
}

int main() {
    generate_data();

    // Запуск gnuplot
    system("gnuplot -persist -e \"set title 'Лемниската Бернулли (a=3)'; set grid; plot 'data.txt' with linespoints pointtype 7 linecolor 'blue'\"");

    return 0;
}
