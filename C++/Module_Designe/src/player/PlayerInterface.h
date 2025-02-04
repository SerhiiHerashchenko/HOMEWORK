#ifndef PLAYERINTERFACE_H
#define PLAYERINTERFACE_H

#include <iostream>
#include <string>

using namespace std;

class PlayerInterface{
public:
    virtual string makeMove() = 0;
    virtual string getId() = 0;
    virtual string getName() =0;
};

#endif