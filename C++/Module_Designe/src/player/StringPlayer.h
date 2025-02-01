#include <iostream>
#include <string>
#include <C:\Users\tiko1\Documents\GitHub\HOMEWORK\C++\Module_Designe\src\data\processData\StringDataProcessor.h>

using namespace std;

class StringPlayer{
public:
    string makeMove(){
        StringDataProcessor* data = new StringDataProcessor();
        data->readData();
        return data->getData();
    }

    StringPlayer(string id, string name): id(id),name(name){}
    string getId() { return this->id; }
    string getName() { return this->name; }

private:
    string id;
    string name;
};