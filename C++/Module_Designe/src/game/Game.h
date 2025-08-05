#include <iostream>
#include <string>
#include "src\player\PlayerInterface.h"
#include "src\player\StringPlayer.h"
#include "src\game\gameProcessor\Processor.h"
#include "src\data\processData\BannerProcessor.h"

class Game{
public:
    Game(string id, string name){
        processor = new Processor;
        player = new StringPlayer(id, name);
        guessed_number = processor->random_int(1, 99);
    }
    ~Game(){
        delete processor;
        delete player;
    }

    bool play(){
        cout << "Let's get ready to rumble!\n";
        cout << guessed_number;
        while (!is_winner){
            try{
                string current_move_str = player->makeMove();
                int current_move_int = stoi(current_move_str);

                int magic_number = processor->random_int(1, 9);
                if(magic_counter < 4 && (magic_number == 3 || magic_number == 7))
                    magic_counter++;

                EGLU condition = processor->compare(current_move_int, guessed_number, magic_counter, magic_number);
                if(condition == EQUALS){
                    is_winner = true;
                    cout << "Yes, finally, you pick the right number. That didn't take a centure\n";
                    BannerProcessor* bp = new BannerProcessor();
                    bp->readData("./Module_Designe/src/resources/Winner_Banner.txt");
                    cout << bp->getData();
                    cout << "Do you want to continue playing?\nY:1/N:0\n";
                    
                    cin >> is_winner;
                    if (!is_winner){
                        cout << "Thank you for playing!";
                        return false;
                    }
                    return true;
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
        return false;
    }
private:
    Processor* processor;
    PlayerInterface* player;
    int guessed_number;
    int magic_counter;
    bool is_winner = false;
};