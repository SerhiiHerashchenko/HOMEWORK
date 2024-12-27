package Lab5_ModuleDesign.src;

import Lab5_ModuleDesign.src.picker.NumberPicker;
import Lab5_ModuleDesign.src.player.ConsolePlayer;
import Lab5_ModuleDesign.src.processor.Game;
import Lab5_ModuleDesign.src.processor.game.ConsoleGameProcessor;

public class GameHandler {
    public static void main(String[] args) {
        final ConsolePlayer player = new ConsolePlayer("Hulio", "1");
        final ConsoleGameProcessor processor = new ConsoleGameProcessor(player);

        final NumberPicker p = new NumberPicker();
        
        Game currentSession = new Game(player, processor, p);
        currentSession.play();
    }
}
