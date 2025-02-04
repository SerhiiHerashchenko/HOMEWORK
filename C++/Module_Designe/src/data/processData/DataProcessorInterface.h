#ifndef DATAPROCESSORINTERFACE_H
#define DATAPROCESSORINTERFACE_H


#include <iostream>
#include <string>
using namespace std;

class DataProcessorInterface{
public:
    virtual string getData() = 0;
    virtual void readData() = 0;
};

#endif