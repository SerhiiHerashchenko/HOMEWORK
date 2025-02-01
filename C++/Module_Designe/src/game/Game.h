#include <iostream>
#include <string>
#include <C:\Users\tiko1\Documents\GitHub\HOMEWORK\C++\Module_Designe\src\player\StringPlayer.h>

class Game{
public:
    Game(string id, string name){
        player = new StringPlayer(id, name);
    }

    void play(){
        while (true){
            string currentMove = player->makeMove();
            
        }
    }
private:
    StringPlayer* player;
    int guessedNumber;
};