package Lab5_ModuleDesign.src.player;

import Lab5_ModuleDesign.src.processor.input.ConsoleInputData;
import Lab5_ModuleDesign.src.processor.input.InputData;

public class ConsolePlayer implements Player {
    private final InputData data = new ConsoleInputData();
    private String name;
    private String id;

    public ConsolePlayer(String name, String id){
        this.id = id;
        this.name = name;
    }
    public String getId() { return id; }
    public String getName() { return name; }

    @Override
    public InputData makeMove(){
        data.collectData();
        return data;
    }
}
