#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

double func(double x, double y) {
    return 3 * x * x - 2 * sin(y) * sin(y);
}

void generate_data(double x_min, double x_max, double y_min, double y_max, int num_points, double (*func)(double, double)) {
    ofstream file("data3d.txt");
    for (int i = 0; i < num_points; ++i) {
        double x = x_min + i * (x_max - x_min) / (num_points - 1);
        for (int j = 0; j < num_points; ++j) {
            double y = y_min + j * (y_max - y_min) / (num_points - 1);
            double z = func(x, y);
            file << x << " " << y << " " << z << endl;
        }
        file << endl;
    }

    file.close();
}

int main() {
    int num_points = 50;
    double x_min = -2;
    double x_max = 2;
    double y_min = -2 * M_PI;
    double y_max = 2 * M_PI;
    generate_data(x_min, x_max, y_min, y_max, num_points, func);

    system("gnuplot -persist -e \"set dgrid3d 50,50; set hidden3d; splot 'data3d.txt' with lines\"");
}
