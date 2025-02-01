#include <iostream>
#include <string>
#include <C:\Users\tiko1\Documents\GitHub\HOMEWORK\C++\Module_Designe\src\data\processData\DataProcessorInterface.h>

using namespace std;

class StringDataProcessor:DataProcessorInterface{
public:
    virtual void readData() { cin >> data; }
    virtual string getData() { return data; }
    
private:
    string data;
};