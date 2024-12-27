package Lab5_ModuleDesign.src.processor.comparator;

import Lab5_ModuleDesign.src.processor.game.EGLU;

public interface Comparator {
    public<T> EGLU compare(T givenEntity, T playerEntity, T magicEntity, int magicCounter);
}
