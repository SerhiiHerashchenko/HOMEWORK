#include <string>
#include <C:\ALL\FOR-CODING\GitHub repositories\HOMEWORK\C++\Battleship_Game\src\GameProcessor\game\Game.h>
#include <C:\ALL\FOR-CODING\GitHub repositories\HOMEWORK\C++\Battleship_Game\src\player\ConsolePlayer.h>
#include <C:\ALL\FOR-CODING\GitHub repositories\HOMEWORK\C++\Battleship_Game\src\GameProcessor\processor\BattleshipProcessor.h>

using namespace std;

class ConsoleGame : Game{
public:
    ConsoleGame(string player_name){
        this->player = new ConsolePlayer(player_name);
        this->opponent = new ConsolePlayer("opponent");
        this->processor = new BattleshipProcessor(player, opponent);

    }
    virtual bool play(){
        
    };
private:
    BattleshipProcessor* processor;
    ConsolePlayer* player;
    ConsolePlayer* opponent;
};