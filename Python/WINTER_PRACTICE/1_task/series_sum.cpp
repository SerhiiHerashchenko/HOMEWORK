#include <cmath>
#include <iostream>
using namespace std;

unsigned int factorial(int n){
    if (n < 0) throw new invalid_argument("You've entered negative number");
    if (n == 0) return 1;

    int i = n - 1;

    while(i != 0){
        n *= i;
        i--;
    }
    return n;
}

int main(){
    double eps = 0.001;
    int n = 1;
    double a_i = pow(-1, n) / (pow(2, n) * factorial(n));
    double series_sum = a_i;

    while(abs(a_i) >= eps){
        n++;
        a_i = pow(-1, n) / (pow(2, n) * factorial(n));
        series_sum += a_i;
    }

// Воспользовались следствием из признака Лейбница для сходимости знакочередующегося ряда, то есть:
// Остаток сходящегося знакочередующегося ряда по модулю будет меньше первого отброшенного слагаемого
// Что и проверялось на каждой итерации цикла

    cout << series_sum << " " << n;
}