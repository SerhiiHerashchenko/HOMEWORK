#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;

// ------------------ Gauss Quadrature for Double Integrals ------------------
double Gauss_Quadrature_2d(double (*f)(double, double), double a, double A, double b, double B, int n, int p) {
    vector<double> roots, weights;

    if (p == 5) {
        roots = {-0.906179845938664, -0.538469310105683, 0, 0.538469310105683, 0.906179845938664};
        weights = {0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189};
    } else if (p == 4) {
        roots = {-0.861136311594053, -0.339981043584856, 0.339981043584856, 0.861136311594053};
        weights = {0.3478548451374529, 0.6521451548625463, 0.6521451548625463, 0.3478548451374529};
    } else if (p == 3) {
        roots = {-0.774596669241483, 0, 0.774596669241483};
        weights = {0.555555555555556, 0.888888888888889, 0.555555555555556};
    } else if (p == 2) {
        roots = {-0.577350269189626, 0.577350269189626};
        weights = {1, 1};
    } else {
        roots = {0};
        weights = {2};
    }

    double h_a = (A - a) / n;
    double h_b = (B - b) / n;
    double integral = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            double a_tmp = a + i * h_a;
            double A_tmp = a_tmp + h_a;
            double b_tmp = b + j * h_b;
            double B_tmp = b_tmp + h_b;

            double tmp_integral = 0;

            for (int k = 0; k < p; k++) {
                double x_mapped = (A_tmp - a_tmp) / 2 * roots[k] + (A_tmp + a_tmp) / 2;

                for (int l = 0; l < p; l++) {
                    double y_mapped = (B_tmp - b_tmp) / 2 * roots[l] + (B_tmp + b_tmp) / 2;
                    tmp_integral += weights[k] * weights[l] * f(x_mapped, y_mapped);
                }
            }

            integral += ((A_tmp - a_tmp) / 2) * ((B_tmp - b_tmp) / 2) * tmp_integral;
        }
    }

    return integral;
}


double func(double x, double y) { return 2 * x * sin(x * y); }

// ------------------ My Integral ------------------

int main(){
    double eps;

    cout << "Enter a floating-point number eps, ";
    cout << "that is, the precision with which you want to numerically find approximate value of the given integral" << endl;
    cin >> eps;

    double a = 0;
    double A = 1;

    double b = 0;
    double B = M_PI / 2;
    
    int n = 2;
    int p = n;
    int alg_presicion = 2 * n - 1;
    
    cout << "n = " << n << endl;
    
    double result_n = Gauss_Quadrature_2d(func, a, A, b, B, n, p);
    double result_2n = Gauss_Quadrature_2d(func, a, A, b, B, 2 * n, p);
    
    double E = abs(result_n - result_2n) / (pow(2, alg_presicion) - 1);
    cout << "Error: " << E << endl;
    
    // ------------------ Runge Accuracy Control ------------------
    while(E >= eps){
        n = 2 * n;
        result_n = result_2n;
        result_2n = Gauss_Quadrature_2d(func, a, A, b, B, 2 * n, p);
        E = abs(result_n - result_2n) / (pow(2, alg_presicion) - 1);
        cout << "n = " << n << endl;
        cout << "Error: " << E << endl;
    }
    
    double z = log(eps)/log(10);

    cout << "Trapezoidal rule (h): " << setprecision(z + 1) << result_n;
}