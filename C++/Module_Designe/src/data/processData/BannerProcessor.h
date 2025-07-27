#include <fstream>
#include <string>
#include "src\data\processData\DataProcessorInterface.h"

using namespace std;

class BannerProcessor:DataProcessorInterface{
public:
    virtual void readData(string path){
        ifstream input_banner;
        input_banner.open(path);
        string tmp;
        while (getline(input_banner, tmp))
            data += (tmp + "\n");
        input_banner.close();
    }
    virtual string getData() { return data; }
    
private:
    string data = "";
};