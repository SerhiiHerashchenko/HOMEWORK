#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

void generate_data(double a, int num_points) {
    ofstream file("data.txt");

    bool firstPart = true; // Флаг для отслеживания разрыва графика

    for (int i = 0; i < num_points; ++i) {
        double theta = -M_PI + i * (2 * M_PI) / (num_points - 1);
        double r2 = 2 * a * a * cos(2 * theta);

        if (r2 > 0) {
            double r = sqrt(r2);
            double x = r * cos(theta);
            double y = r * sin(theta);
            file << x << " " << y << endl;
            firstPart = true;  // График продолжается
        } else if (firstPart) {
            file << "0 0" << endl;  // Добавляем точку (0,0) в разрыв
            firstPart = false;
        }
    }

    file.close();
}

int main() {
    int num_points;

    cout << "Enter number of points(int), ";
    cout << "that is, the precision with which you want to draw approximate graph of the lemniscate function" << endl;
    cin >> num_points;

    double a;
    cout << "Enter focus value " << endl;
    cin >> a;

    generate_data(a, num_points);

    system("gnuplot -persist -e \"set title 'Lemniscate of Bernoulli'; set grid; plot 'data.txt' with linespoints pointtype 7 linecolor 'blue'\"");
}