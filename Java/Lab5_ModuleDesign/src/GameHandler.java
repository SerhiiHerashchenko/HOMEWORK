package Lab5_ModuleDesign.src;

import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

import Lab5_ModuleDesign.src.picker.NumberPicker;
import Lab5_ModuleDesign.src.player.ConsolePlayer;
import Lab5_ModuleDesign.src.processor.Game;
import Lab5_ModuleDesign.src.processor.game.ConsoleGameProcessor;

public class GameHandler {
    public static void main(String[] args) {

        try {
            System.setOut(new PrintStream(System.out, true, StandardCharsets.UTF_8));
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        final ConsolePlayer player = new ConsolePlayer("Hulio", "1");
        final ConsoleGameProcessor processor = new ConsoleGameProcessor(player);

        final NumberPicker p = new NumberPicker();
        
        Game currentSession = new Game(player, processor, p);
        currentSession.play();
    }
}
