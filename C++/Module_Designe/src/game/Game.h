#include <iostream>
#include <string>
#include <C:\ALL\GitHub repositories\HOMEWORK\C++\Module_Designe\src\player\StringPlayer.h>
#include <C:\ALL\GitHub repositories\HOMEWORK\C++\Module_Designe\src\player\PlayerInterface.h>
#include <C:\ALL\GitHub repositories\HOMEWORK\C++\Module_Designe\src\game\gameProcessor\Processor.h>

class Game{
public:
    Game(string id, string name){
        player = new StringPlayer(id, name);
    }

    void play(){
        while (!is_winner){
            try{
                string current_move_str = player->makeMove();
                int current_move_int = stoi(current_move_str);
                Processor* p = new Processor;
                //////Random value
                int magic_number = 0;
                if(magic_counter < 4 && (magic_number == 3 || magic_number == 7))
                    magic_counter++;
                //////
                EGLU condition = p->compare(current_move_int, guessed_number, magic_counter, magic_number);
                if(condition == EQUALS){
                    is_winner = true;
                    cout << "Yes, finally, you pick the right number. That didn't take a centure\n"; 
                }
                else if(condition == GREATER)
                    cout << "Your number is greater than I guessed. Try again!\n"; 
                else 
                    cout << "Your number is less than I guessed. Try again!\n"; 
            }
            catch(invalid_argument iv){
                cout << "Enter correct number, you've written something wrong\n";
            }
        }
    }
private:
    PlayerInterface* player;
    int guessed_number = 16;
    int magic_counter;
    bool is_winner = false;
};