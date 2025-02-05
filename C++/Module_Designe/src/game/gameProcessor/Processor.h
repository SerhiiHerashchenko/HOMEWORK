#include <iostream>
#include <string>
#include <C:\ALL\FOR-CODING\GitHub repositories\HOMEWORK\C++\Module_Designe\src\game\gameProcessor\EGLU.h>

class Processor{
public:
    EGLU compare(int player_num, int guessed_num, int magic_counter, int magic_number){
        if(magic_counter < 4 && (magic_number == 3 || magic_number == 7)){
            if(player_num < guessed_num) return GREATER;
            else return LESS;
        }
        else{
            if(player_num == guessed_num) return EQUALS;
            else if(player_num > guessed_num) return GREATER;
            else return LESS;
        }
        return EQUALS;
    }

    int random_int(int start, int end){
        srand(time(0));
        return rand() % (end - start + 1) + start;
    }
};