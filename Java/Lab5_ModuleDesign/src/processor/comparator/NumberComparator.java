package Lab5_ModuleDesign.src.processor.comparator;

import Lab5_ModuleDesign.src.processor.game.EGLU;

public class NumberComparator implements Comparator {
    @Override
    public<T> EGLU compare(T givenEntity, T playerEntity, T magicEntity, int magicCounter){
        if (givenEntity instanceof Integer && playerEntity instanceof Integer && magicEntity instanceof Integer) {
            int givenNumber = (int)givenEntity;
            int playerNumber = (int)playerEntity;
            int magicNumber = (int)magicEntity;
            if(magicCounter >= 3 || (magicNumber != 7 && magicNumber != 3)) {
                if(givenNumber == playerNumber) { return EGLU.Equals; }
                else if(givenNumber > playerNumber) { return EGLU.Less; }
                else { return EGLU.Greater; }
            }
            else {
                magicCounter++;
                if(givenNumber == playerNumber) {
                    if (magicNumber == 7) { return EGLU.Greater; }
                    else { return EGLU.Less; }
                }
                else if(givenNumber > playerNumber) { return EGLU.Greater; }
                else { return EGLU.Less; }
            }
        }
        else{
            return EGLU.Uncomparable;
        }
    }
}