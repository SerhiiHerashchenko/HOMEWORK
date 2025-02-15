#include <iostream>
#include <fstream>
#include <cmath>

void generate_data(double (*f)(double), double a, double b, int num_points) {
    std::ofstream file("data.txt"); // Файл с данными
    if (!file) {
        std::cerr << "Ошибка: не удалось создать файл данных!" << std::endl;
        return;
    }

    // Разбиваем отрезок [a, b] на num_points точек
    for (int i = 0; i < num_points; ++i) {
        double x = a + i * (b - a) / (num_points - 1);
        double y = f(x);
        file << x << " " << y << std::endl;
    }

    file.close();
}

double func(double x) {
    // return exp(sin(x));
    // return exp(cos(x));
    return sin(x);
}

int main() {
    generate_data(func, -3*M_PI, 2 * M_PI, 100);
    

    // Запускаем Gnuplot и строим график
    system("gnuplot -persist -e \"plot 'data.txt' with linespoints pointtype 7 linecolor 'blue'\"");
    
    return 0;
}
