package Lab5_ModuleDesign.src.player;

import Lab5_ModuleDesign.src.processor.input.InputData;

public interface Player {
    public InputData makeMove();
    public String getId();
    public String getName();
}
