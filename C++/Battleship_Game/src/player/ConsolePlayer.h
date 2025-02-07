#include <string>
#include <iostream>

using namespace std;

class ConsolePlayer{
public:
    ConsolePlayer(string name){
        this->name = name;
        this->id = 42;
    }
    
    virtual string make_move(){
        string move;
        cin >> move;
        return move;
    }

    void set_boat(int ship_length, int ship_amount){
        for (int i = 0; i < ship_amount; i++){
            cout << "Enter start end final cells, where you want your boat set";
            string start_cell;
            string end_cell;
            bool ship_setted = false;
            while(!ship_setted){
                cin >> start_cell >> end_cell;
                if ((start_cell.length() != 2 || end_cell.length() != 2) || ((start_cell[0] != end_cell[0]) && (start_cell[1] != end_cell[1])) || ((start_cell[0] != end_cell[0]) && (end_cell[0] - start_cell[0] + 1 = )))
                    cout << "You have written wrong format location of the ship, try again";
                else ship_setted = true;
            }
            if (start_cell[0] != end_cell[0]){
                for (int j = start_cell[0] - 1; j < end_cell[0] - 1; j++)
                    map[j][start_cell[1] - 1] = 1;
            }
            else{
                for (int j = start_cell[1] - 1; j < end_cell[1] - 1; j++)
                    map[start_cell[0] - 1][j] = 1;
            }
        }
        
    }

    string get_name(){ return this->name; }
    int get_id(){ return this->id; }
    void set_map(int** map){ this->map = map; }
private:
    string name;
    int id;
    int** map;
};