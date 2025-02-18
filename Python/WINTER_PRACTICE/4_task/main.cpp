#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

void generate_data(double (*f)(double), double a, double b, int num_points) {
    ofstream file("data.txt");
    
    for (int i = 0; i < num_points; ++i) {
        double x = a + i * (b - a) / (num_points - 1);
        double y = f(x);
        file << x << " " << y << endl;
    }

    file.close();
}

double func(double x) {
    // return exp(sin(x));
    return exp(cos(x));
    // return sin(x);
}

int main() {
    double a = -3 * M_PI;
    double b = 2 * M_PI;
    int num_points = 100;

    generate_data(func, a, b, num_points);
    
    system("gnuplot -persist -e \"set grid; plot 'data.txt' with linespoints pointtype 7 linecolor 'blue'\"");
}