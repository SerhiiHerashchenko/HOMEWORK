#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double func(double x, double y){
    return 2 * x * sin(x * y);
}
double Trapezoidal_cubature_rule(double f(double x, double y), double a, double A, double b, double B, int n, int m){
    double h = (A - a) / n;
    double k =  (B - b) / m;
    double x = a;
    double y = b;
    double integral = 0;
    double w = 1;

    for(int i = 0; i <= n; i++){
        y = b;
        for(int j = 0; j <= m; j++){
            if ((i > 0) && (i < n) && (j > 0) && (j < m))
                w = 1;
            else if ((i==0 || i==n ) && (j==0 || j==m))
                w = 0.25;
            else
                w = 0.5;
            integral += w * f(x, y);
            y += k;
        }
        x += h;
    }

    return h * k * integral;
}

int main(){
    double eps;

    cout << "Enter a floating-point number eps, ";
    cout << "that is, the precision with which you want to numerically find approximate value of the given integral" << endl;
    cin >> eps;

    double a = 0;
    double A = 1;

    double b = 0;
    double B = M_PI / 2;

    int n = 3;
    int m = 3;

    int alg_precision = 1;

    cout << "n = " << n << "\n";
    cout << "m = " << m << "\n";

    double result_n = Trapezoidal_cubature_rule(func, a, A, b, B, n, m);
    double result_2n = Trapezoidal_cubature_rule(func, a, A, b, B, n * 2, m * 2);

    double E = abs(result_n - result_2n) / (pow(2, alg_precision) - 1);
    cout << "Error: " << E << "\n";

    while(E >= eps){
        n = 2 * n;
        m = 2 * m,
        result_n = result_2n;
        result_2n = Trapezoidal_cubature_rule(func, a, A, b, B, n * 2, m * 2);
        E = abs(result_n - result_2n) / (pow(2, alg_precision) - 1);
        cout << "n = " << n << "\n";
        cout << "m = " << m << "\n";        
        cout << "Error: " << E << "\n";
    }

    double z = log(eps)/log(10);

    cout << "Trapezoidal rule (h): " << setprecision(z + 1) << result_n << "\n";
}