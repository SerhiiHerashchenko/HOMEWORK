package Lab5_ModuleDesign.src.picker;

import java.util.InputMismatchException;

public class NumberPicker implements Picker {
    @Override
    public <T> int pick(T data){
        int num;
        if (data instanceof Integer) {
            int max = (int)data;
            num = (int)(Math.random() * max) + 1;  
        }
        else{
            throw new InputMismatchException();
        }
        return num;
    }
}
