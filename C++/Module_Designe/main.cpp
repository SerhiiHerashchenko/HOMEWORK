#include <iostream>
#include <C:\ALL\FOR-CODING\GitHub repositories\HOMEWORK\C++\Module_Designe\src\game\Game.h>
using namespace std;

int main(){
    while (true){
        Game* current_game_session = new Game("12345", "Hulio");

        cout << "Let's get ready to rumble!\n";
        current_game_session->play();

        delete current_game_session;
        
        cout << "Do you want to continue playing?\nY:1/N:0\n";

        bool continue_play = false;
        cin >> continue_play;
        if (!continue_play){
            cout << "Thank you for playing!";
            break;
        }
    }
}