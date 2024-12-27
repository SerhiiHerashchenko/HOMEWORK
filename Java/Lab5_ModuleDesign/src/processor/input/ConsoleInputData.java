package Lab5_ModuleDesign.src.processor.input;

import java.util.Scanner;

public class ConsoleInputData implements InputData {
    private Scanner console;
    public String data;

    @Override
    public void collectData() {
        console = new Scanner(System.in);
        data = console.nextLine();
    }
}
