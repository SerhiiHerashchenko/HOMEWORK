package Java.Lab2_ArrayList;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class MyComparator implements Comparator{
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
        ArrayList<String> colors = new ArrayList<String>();
        colors.add("Blue");
        colors.add("White");
        colors.add("Purple");
        colors.add("Green");

        for (String color : colors) {
            System.out.println(color);
        }
        System.out.println("\n");

        // #3
        colors.add(1, "Red");
        System.out.println(colors.get(1));

        // #4
        String task4String = colors.get(3);
        System.out.println(task4String);

        // #5
        String newString = "Black";
        colors.set(2, newString);

        // #6
        colors.remove(3);

        // #7
        String soughString = "White";
        if(colors.contains(soughString)){
            System.out.println("Color " + soughString + " are in colors!");
        }
        else
            System.out.println("Color " + soughString + " are NOT in colors!");

        // #8
        System.out.println("Before " + colors);
        Collections.sort(colors, new MyComparator());
        System.out.println("After " + colors);

        // #9
        ArrayList<String> copyColors = colors;
        System.out.println(copyColors);

        // #10
        ArrayList<String> reversedColors = reverse(colors);
        System.out.println(reversedColors);

        // #11
        System.out.println(compare(colors, reversedColors));

        ArrayList<Integer> integers = new ArrayList<Integer>();
        for (int i = 0; i < colors.size() + 1; i++) {
            integers.add(i);
        }
        System.out.println(compare(colors, integers));
        
        // #12
        integers.clear();
        System.out.println(integers.size());

        // #13
        System.out.println(integers.isEmpty());
        System.out.println(colors.isEmpty());

        // #14
        colors.ensureCapacity(10);
        System.out.println(colors);

    }
    // #14
    public static<T> ArrayList<T> increaseCapacity(ArrayList<T> array, int newCapacity){
        // Function increase capacity of the given generic arraylist
        // Fills new slots with null
        int currentCapacity = array.size();
        ArrayList<T> newArray = new ArrayList<T>(newCapacity);

        for (int i = 0; i < currentCapacity; i++) {
            newArray.add(i, array.get(i));
        }
        for (int i = currentCapacity; i < newCapacity; i++) {
            newArray.add(i, null);
        }
        return newArray;
    }
    // #11
    public static<T, E> boolean compare(ArrayList<T> array1, ArrayList<E> array2){
        // Function compare two generic arraylists by their lengths
        // Return TRUE if length of the first arraylist is longer than second arraylist
        // In other cases return FALSE
        int length1 = array1.size();
        int length2 = array2.size();
        if(length1 >= length2) return true;
        else return false;
    }
    // #10
    public static<T> ArrayList<T> reverse(ArrayList<T> array){
        int length = array.size();
        if(length != 0){
            ArrayList<T> reversedArray = new ArrayList<T>();

            for (int j = length - 1; j >= 0; j--) {
                reversedArray.add(array.get(j));
            }
            array = reversedArray; 
        }
        return array;
    }
}