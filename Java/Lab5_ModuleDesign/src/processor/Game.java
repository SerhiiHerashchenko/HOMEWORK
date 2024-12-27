package Lab5_ModuleDesign.src.processor;

import Lab5_ModuleDesign.src.picker.Picker;
import Lab5_ModuleDesign.src.player.Player;
import Lab5_ModuleDesign.src.processor.game.GameProcessor;

public class Game{
    Player player;
    GameProcessor processor;
    Picker p;
    int pickedNumber;

    public Game(Player player, GameProcessor processor, Picker p){
        this.player = player;
        this.processor = processor;
        this.p = p;
        this.pickedNumber = p.pick(100);        
    }

    public void play(){
        System.out.println("The game's started. The number's guessed. " + this.player.getName() + ", your move!");
        while (this.processor.isWinner() != true) {
            this.processor.checkPlayersMove(this.player.makeMove(), this.pickedNumber);
        }
    }
}