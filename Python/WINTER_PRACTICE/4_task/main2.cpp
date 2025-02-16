#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

double func(double x) {
    double denominator = x * x - 2 * x - 3;
    if (abs(denominator) < 1e-6) {
        return NAN;
    }
    return 1.0 / denominator;
}

void generate_data(double a, double b, int num_points, ofstream &file, double(* func)(double)) {
    for (int i = 0; i < num_points; ++i) {
        double x = a + i * (b - a) / (num_points - 1);
        double y = func(x);

        if (!isnan(y))
            file << x << " " << y << endl;
    }
    file << endl;
}

int main() {
    double a = -3 * M_PI;
    double b = 2 * M_PI;
    int num_points = 50;

    ofstream file("data.txt");

    generate_data(a, -1, num_points + 75, file, func);
    generate_data(-1, 3, num_points, file, func);
    generate_data(3, b, num_points, file, func);

    file.close();

    system("gnuplot -persist -e \"set grid; plot 'data.txt' with linespoints pointtype 7 linecolor 'blue'\"");
}
