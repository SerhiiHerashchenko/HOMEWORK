#ifndef DATAPROCESSORINTERFACE_H
#define DATAPROCESSORINTERFACE_H

#include <string>

using namespace std;

class DataProcessorInterface{
public:
    virtual string getData() = 0;
    virtual void readData(string path) = 0;
};

#endif