#include <iostream>
#include <C:\Users\tiko1\Documents\GitHub\HOMEWORK\C++\Module_Designe\src\game\Game.h>
using namespace std;

int main(){
    Game* currentGameSession = new Game("12345", "Hulio");
    currentGameSession->play();
}