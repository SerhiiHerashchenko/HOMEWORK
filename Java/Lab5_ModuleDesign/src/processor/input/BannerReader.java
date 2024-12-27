package Lab5_ModuleDesign.src.processor.input;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class BannerReader implements InputData {
    String filePath;
    BufferedReader reader;
    public String data = "";

    public BannerReader(String path){
        filePath = path;
        collectData();
    }

    @Override
    public void collectData() {
        try {
            reader = new BufferedReader(new FileReader(filePath));
            String line = reader.readLine();
            while (line != null) {
                data += "\n" + line;
                line = reader.readLine();
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}