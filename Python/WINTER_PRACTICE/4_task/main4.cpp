#include <iostream>
#include <fstream>
#include <cmath>

const int NUM_POINTS = 50; // Количество точек по каждой оси
const double X_MIN = -2, X_MAX = 2; // Границы x
const double Y_MIN = -2 * M_PI, Y_MAX = 2 * M_PI; // Границы y

// Функция для генерации данных
void generate_data() {
    std::ofstream file("data3d.txt"); // Открываем файл для записи
    if (!file) {
        std::cerr << "Ошибка: не удалось создать файл данных!" << std::endl;
        return;
    }

    for (int i = 0; i < NUM_POINTS; ++i) {
        double x = X_MIN + i * (X_MAX - X_MIN) / (NUM_POINTS - 1);
        for (int j = 0; j < NUM_POINTS; ++j) {
            double y = Y_MIN + j * (Y_MAX - Y_MIN) / (NUM_POINTS - 1);
            double z = 3 * x * x - 2 * sin(y) * sin(y);
            file << x << " " << y << " " << z << std::endl;
        }
        file << "\n"; // Разрыв строк для gnuplot
    }

    file.close();
}

int main() {
    generate_data();

    // Запуск Gnuplot
    system("gnuplot -persist -e \"set dgrid3d 50,50; set hidden3d; set title 'z = 3x^2 - 2sin^2(y)'; splot 'data3d.txt' with lines\"");

    return 0;
}
