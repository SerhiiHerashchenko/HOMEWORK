#include <iostream>
#include <string>
#include <C:\ALL\FOR-CODING\GitHub repositories\HOMEWORK\C++\Module_Designe\src\data\processData\DataProcessorInterface.h>

using namespace std;

class StringDataProcessor:DataProcessorInterface{
public:
    virtual void readData(string path = "") { cin >> data; }
    virtual string getData() { return data; }
    
private:
    string data;
};