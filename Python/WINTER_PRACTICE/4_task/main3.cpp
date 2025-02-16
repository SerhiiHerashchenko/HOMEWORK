#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

void generate_data(double a, double num_points) {
    ofstream file("data.txt");

    for (int i = 0; i < num_points; ++i) {
        double theta = -M_PI + i * (2 * M_PI) / (num_points - 1);
        double r2 = 2 * a * a * cos(2 * theta);

        if (r2 > 0) {
            double r = sqrt(r2);
            double x = r * cos(theta);
            double y = r * sin(theta);
            file << x << " " << y << endl;
        } else {
            file << endl;
        }
    }

    file.close();
}

int main() {
    int num_points = 100;
    double a = 3;

    generate_data(a, num_points);

    system("gnuplot -persist -e \"set title 'Lemniscate of Bernoulli'; set grid; plot 'data.txt' with linespoints pointtype 7 linecolor 'blue'\"");
}
