#include <iostream>
#include <string>
#include <C:\ALL\GitHub repositories\HOMEWORK\C++\Module_Designe\src\data\processData\StringDataProcessor.h>
#include <C:\ALL\GitHub repositories\HOMEWORK\C++\Module_Designe\src\player\PlayerInterface.h>

using namespace std;

class StringPlayer : public PlayerInterface{
public:
    StringPlayer(string id, string name): id(id),name(name){}

    virtual string makeMove(){
        StringDataProcessor* data = new StringDataProcessor();
        data->readData();
        return data->getData();
    }

    virtual string getId() { return this->id; }
    virtual string getName() { return this->name; }

private:
    string id;
    string name;
};