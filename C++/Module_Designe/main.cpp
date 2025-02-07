#include <windows.h>
#include <C:\ALL\FOR-CODING\GitHub repositories\HOMEWORK\C++\Module_Designe\src\game\Game.h>
using namespace std;

int main(){
    SetConsoleOutputCP(65001);
    bool continue_play = true;
    while (continue_play){
        Game* current_game_session = new Game("12345", "Hulio");

        continue_play = current_game_session->play();

        delete current_game_session;
    }
}