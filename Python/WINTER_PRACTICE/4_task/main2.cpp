#include <iostream>
#include <fstream>
#include <cmath>

const double PI = M_PI;

// Функция f(x)
double func(double x) {
    double denominator = x * x - 2 * x - 3;
    if (std::abs(denominator) < 1e-6) { // Исключаем разрывы
        return NAN;
    }
    return 1.0 / denominator;
}

void generate_data(double a, double b, int num_points, std::ofstream &file) {
    for (int i = 0; i < num_points; ++i) {
        double x = a + i * (b - a) / (num_points - 1);
        double y = func(x);

        if (!std::isnan(y)) { // Записываем только корректные значения
            file << x << " " << y << std::endl;
        }
    }
    file << "\n"; // Добавляем пустую строку между промежутками (разрыв в графике)
}

int main() {
    double a = -3 * PI, b = 2 * PI;
    int num_points = 50;

    std::ofstream file("data.txt"); // Открываем файл (перезапись)
    if (!file) {
        std::cerr << "Ошибка: не удалось создать файл данных!" << std::endl;
        return 1;
    }

    generate_data(a, -1, num_points + 75, file);  // Левый участок
    generate_data(-1, 3, num_points, file);  // Средний участок
    generate_data(3, b, num_points, file);  // Правый участок

    file.close();

    // Запуск gnuplot
    system("gnuplot -persist -e \"set title 'График 1/(x^2 - 2x - 3)'; set grid; plot 'data.txt' with linespoints pointtype 7 linecolor 'blue'\"");

    return 0;
}
