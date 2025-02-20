#include <cmath>
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double x;
    double eps;

    cout << "Enter x: ";
    cin >> x;
    cout << "Enter occuracy: ";
    cin >> eps;

    double n = 1;

    double sum = 0;
    
    if(x == 0) { sum = 0; }
    else if(x == 1) { sum = 1; }
    else if(0 < x && x < 1){
        n = ceil(log(eps * (1.0 - x)) / log(x));

        for (int i = 0; i <= n; i++){
            sum += pow(x, double(i)) / ((double(i) + 1.0) * (double(i) + 2.0));
        }

        sum *= pow(x, 6.0);
    }
    else if(-1 <= x && x < 0) {
        double a_i = 1.0 / 2.0;
        int i = 1;
        
        sum = 0;
        while (abs(a_i) >= eps) {
            sum += a_i;
            a_i = pow(x, double(i)) / ((double(i) + 1.0) * (double(i) + 2.0));
            i++;
        }
    
        sum *= pow(x, 6.0);
    }
    
    double z = log(eps) / log(10);

    cout << setprecision(z + 1) << sum;
}