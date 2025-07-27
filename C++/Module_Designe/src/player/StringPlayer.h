#include <string>
#include "src\data\processData\StringDataProcessor.h"
#include "src\player\PlayerInterface.h"

using namespace std;

class StringPlayer : public PlayerInterface{
public:
    StringPlayer(string id, string name){
        this->id = id;
        this->name = name;
        data = new StringDataProcessor();
    }
    ~StringPlayer(){
        delete data;
    }

    virtual string makeMove(){
        data->readData();
        return data->getData();
    }

    virtual string getId() { return this->id; }
    virtual string getName() { return this->name; }

private:
    StringDataProcessor* data;
    string id;
    string name;
};