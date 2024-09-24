package Java.Lab2_ArrayList;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class MyComparator<T> implements Comparator<T>{
    @Override
    public int compare(Object o1, Object o2) {
        String s1 = o1.toString();
        String s2 = o2.toString();

        return s2.compareTo(s1);
    }
}

class MainClass<T>{
    public static void main(String[] args){
        // #2
        System.out.println("TASK 2:");
        ArrayList<String> colors = new ArrayList<String>();
        colors.add("Blue");
        colors.add("White");
        colors.add("Purple");
        colors.add("Green");

        for (String color : colors) {
            System.out.println(color);
        }
        System.out.println("");

        // #3
        System.out.println("TASK 3:");

        colors.add(1, "Red");
        System.out.println(colors.get(1));

        System.out.println("");

        // #4
        System.out.println("TASK 4:");

        String task4String = colors.get(3);
        System.out.println(task4String);

        System.out.println("");
        // #5
        System.out.println("TASK 5:");

        String newString = "Black";
        System.out.println("Before: " + colors);
        colors.set(2, newString);
        System.out.println("After: " + colors);

        System.out.println("");
        // #6
        System.out.println("TASK 6:");

        colors.remove(3);
        System.out.println(colors);

        System.out.println("");

        // #7
        System.out.println("TASK 7:");

        String soughString = "White";
        if(colors.contains(soughString)){
            System.out.println("Color " + soughString + " are in colors!");
        }
        else
            System.out.println("Color " + soughString + " are NOT in colors!");

        System.out.println("");

        // #8
        System.out.println("TASK 8:");

        System.out.println("Before " + colors);
        Collections.sort(colors, new MyComparator());
        System.out.println("After " + colors);

        System.out.println("");

        // #9
        System.out.println("TASK 9:");

        ArrayList<String> copyColors = new ArrayList<String>(colors);;
        System.out.println(copyColors);

        System.out.println("");

        // #10
        System.out.println("TASK 10:");

        ArrayList<String> reversedColors = new ArrayList<String>(colors);
        Collections.reverse(reversedColors);
        System.out.println(reversedColors);

        System.out.println("");

        // #11
        System.out.println("TASK 11:");

        System.out.println(colors.equals(reversedColors));
        
        System.out.println("");

        // #12
        System.out.println("TASK 12:");

        reversedColors.clear();
        System.out.println(reversedColors.size());

        System.out.println("");
        // #13
        System.out.println("TASK 13:");

        System.out.println(reversedColors.isEmpty());
        System.out.println(colors.isEmpty());

        System.out.println("");

        // #14
        System.out.println("TASK 14:");

        colors.ensureCapacity(10);
        System.out.println(colors);

        System.out.println("");

        // #15
        System.out.println("TASK 15:");

        colors.ensureCapacity(colors.size());
        System.out.println(colors);
    }

}