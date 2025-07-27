#include <iostream>
#include <string>
#include "src\data\processData\DataProcessorInterface.h"

using namespace std;

class StringDataProcessor:DataProcessorInterface{
public:
    virtual void readData(string path = "") { cin >> data; }
    virtual string getData() { return data; }
    
private:
    string data;
};