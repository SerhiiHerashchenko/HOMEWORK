#include <iostream>
#include <C:\ALL\GitHub repositories\HOMEWORK\C++\Module_Designe\src\game\Game.h>
using namespace std;

int main(){
    Game* currentGameSession = new Game("12345", "Hulio");
    cout << "g";
    currentGameSession->play();
}