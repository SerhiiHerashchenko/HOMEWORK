#include <cmath>
#include <iostream>
using namespace std;

int main(){
    double eps;
    cout << "Enter a floating-point number eps, ";
    cout << "that is, the precision with which you want to numerically find the sum of the given series" << endl;
    cin >> eps;
    double n = 1;
    double a_i = -1.0/2.0;
    double series_sum = a_i;

    while(abs(a_i) >= eps){
        n++;
        a_i *= -1 / (2 * n);
        //рекурсивно ищем следующий член ряда. Множитель нашли поделив а_i+1 член на a_i член
        series_sum += a_i;
    }

// Воспользовались следствием из признака Лейбница для сходимости знакочередующегося ряда, то есть:
// Остаток сходящегося знакочередующегося ряда по модулю будет меньше первого отброшенного слагаемого
// Что и проверялось на каждой итерации цикла

    cout << series_sum << " " << n;
}