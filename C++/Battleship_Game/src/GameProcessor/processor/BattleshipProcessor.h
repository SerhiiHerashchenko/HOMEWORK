#include <cstdlib>
#include <ctime>
#include <string>
#include <iostream>
#include <C:\ALL\FOR-CODING\GitHub repositories\HOMEWORK\C++\Battleship_Game\src\player\ConsolePlayer.h>

using namespace std;

class BattleshipProcessor{
public:
    int random_int(int start, int end){
        srand(time(0));
        return rand() % (end - start + 1) + start;
    }

    pair<int, int> str_to_int_coordinates(string point){
        int x = point[0] - '0' - 48;
        int y = point[0] - '0';
        pair<int, int> p(x, y);
        return p;
    }

    bool check_move(string move){ }

    int** map_generator(){
        int** map = new int*[10];
        for (int i = 0; i < 10; i++){
            map[i] = new int[10];
            for (int j = 0; j < 10; j++)
                map[i][j] = 0;
        }
        return map;
    }
};