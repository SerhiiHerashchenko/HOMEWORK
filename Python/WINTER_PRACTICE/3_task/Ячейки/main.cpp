#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// ------------------ Riemann midpoint method ------------------

double CellMethod(double (*f)(double, double), double a, double A, double b, double B, int n, int m) {
    double h_a = (A - a) / n;
    double h_b = (B - b) / m;
    double integral = 0.0;

    for (int i = 1; i <= n; i++) {
        double a_tmp = a + i * h_a;
        double A_tmp = a_tmp + h_a;
        for (int j = 1; j <= m; j++) {
            double b_tmp = b + j * h_b;
            double B_tmp = b_tmp + h_b;
            
            double tmp_integral = f((a_tmp + A_tmp) / 2.0, (b_tmp + B_tmp) / 2.0);
            integral += tmp_integral;
        }
    }
    return h_a * h_b * integral;
}

double f(double x, double y) {
    return 2 * x * sin(x * y);
}

// ------------------ My Integral ------------------

int main() {
    double eps = 0.001;
    double a = 0, A = 1;
    double b = 0, B = M_PI / 2;
    int n = 5, m = 5;
    int alg_precision = 1;

    cout << "n = " << n << endl;
    cout << "m = " << m << endl;

    double result_n = CellMethod(f, a, A, b, B, n, m);
    double result_2n = CellMethod(f, a, A, b, B, n * 2, m * 2);

    double E = abs(result_n - result_2n) / (pow(2, alg_precision) - 1);
    cout << "Error: " << E << endl;

// ------------------ Runge Accuracy Control ------------------

    while (E >= eps) {
        n *= 2;
        m *= 2;
        result_n = result_2n;
        result_2n = CellMethod(f, a, A, b, B, n * 2, m * 2);
        E = abs(result_n - result_2n) / (pow(2, alg_precision) - 1);
        cout << "n = " << n << endl;
        cout << "m = " << m << endl;
        cout << "Error: " << E << endl;
    }

    cout << "Riemann midpoint method (h): " << setprecision(6) << result_n << endl;
}