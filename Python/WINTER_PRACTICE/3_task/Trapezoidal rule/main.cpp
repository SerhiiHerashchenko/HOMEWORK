#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double func(double x, double y){
    return 2 * x * sin(x * y);
}
double Trapezoidal_cubature_rule(double f(double x, double y), double a, double A, double b, double B, int n, int m, double h, double k){
    double x = a;
    double y = b;
    double integral = 0;
    double w = 1;

    for(int i = 0; i <= n; i++){
        y = b;
        for(int j = 0; j <= m; j++){
            if ((i > 0) && (i < n) && (j > 0) && (j < m))
                w = 1;
            else if ((i==0 | i==n ) & (j==0 | j==m))
                w = 0.25;
            else
                w = 0.5;
            integral += w * f(x, y);
            y += k;
        }
        x += h;
    }

    integral *= (h * k);
    return integral;
}
int main(){
    double eps = 0.001;
    double a = 0;
    double A = 1;
    double b = 0;
    double B = M_PI / 2;

    int n = 3;
    int m = 3;
    double h = (A - a) / n;
    double k =  (B - b) / m;

    int alg_precision = 1;

    cout << "n = " << n << "\n";
    cout << "m = " << m << "\n";

    double fi_h = Trapezoidal_cubature_rule(func, a, A, b, B, n, m, h, k);
    double fi_2h = Trapezoidal_cubature_rule(func, a, A, b, B, n/2, m/2, 2*h, 2*k);

    cout << setprecision(4);

    double E = abs(fi_h - fi_2h) / (pow(2, alg_precision) - 1);
    cout << "Error: " << E << "\n";

    while(E >= eps){
        h = h / 2;
        k = k / 2, 
        n = 2 * n;
        m = 2 * m,
        fi_h = Trapezoidal_cubature_rule(func, a, A, b, B, n, m, h, k);
        fi_2h = Trapezoidal_cubature_rule(func, a, A, b, B, n/2, m/2, 2*h, 2*k);
        E = abs(fi_h - fi_2h) / (pow(2, alg_precision) - 1);
        cout << "Error: " << E << "\n";
    }
    cout << "Trapezoidal rule (h): " << fi_h << "\n";
}