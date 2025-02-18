#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

// ------------------ Gauss Quadrature for Double Integrals ------------------
double Gauss_Quadrature_2d(double (*f)(double, double), double a, double A, double b, double B, int n){
    vector<double> roots;
    vector<double> weights;

    if(n == 5){
        roots.assign({-0.906179845938664, -0.538469310105683, 0, 0.538469310105683, 0.906179845938664});
        weights.assign({0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189});
    }
    else if(n == 4){
        roots.assign({-0.861136311594053, -0.339981043584856, 0.339981043584856, 0.861136311594053});
        weights.assign({0.3478548451374529, 0.6521451548625463, 0.6521451548625463, 0.3478548451374529});
    }
    else if(n == 3){
        roots.assign({-0.774596669241483, 0, 0.774596669241483});
        weights.assign({0.555555555555556, 0.888888888888889, 0.555555555555556});
    }
    else if(n == 2){
        roots.assign({-0.577350269189626, 0.577350269189626});
        weights.assign({1, 1});
    }
    else{
        roots.assign({0});
        weights.assign({2});
    }

    vector<double> x_roots_transformed;
    vector<double> y_roots_transformed;

    for(double root : roots){
        x_roots_transformed.push_back(((A - a) / 2) * root + (A + a) / 2);
        y_roots_transformed.push_back(((B - b) / 2) * root + (B + b) / 2);
    }
    
    double integral = 0;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            integral += (weights[i] * weights[j] * f(x_roots_transformed[i], y_roots_transformed[j]));
        }
    }
    
    return ((A - a) / 2) * ((B - b) / 2) * integral;
}

double func(double x, double y) { return 2 * x * sin(x * y); }
// ------------------ My Integral ------------------

int main(){
    double eps = 0.001;

    double a = 0;
    double A = 1;

    double b = 0;
    double B = M_PI / 2;
    
    int n = 2;
    int alg_presicion = 2 * n - 1;
    
    cout << "n = " << n << endl;
    
    double result_h = Gauss_Quadrature_2d(func, a, A, b, B, n);
    double result_2h = Gauss_Quadrature_2d(func, a, A, b, B, int(n / 2));
    
    double E = abs(result_h - result_2h) / (pow(2, alg_presicion) - 1);
    cout << "Error: " << E << endl;
    
    // ------------------ Runge Accuracy Control ------------------
    while(E >= eps){
        n = 2 * n;
        result_h = Gauss_Quadrature_2d(func, a, A, b, B, n);
        result_2h = Gauss_Quadrature_2d(func, a, A, b, B, int(n / 2));
        E = abs(result_h - result_2h) / (pow(2, alg_presicion) - 1);
        cout << "n = " << n << endl;
        cout << "Error: " << E << endl;
    }

    cout << result_h;
}