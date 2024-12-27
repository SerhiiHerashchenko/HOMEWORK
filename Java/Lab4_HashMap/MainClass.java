package Lab4_HashMap;

import java.util.ArrayList;

public class MainClass {
    public static void main(String[] args) {
        final Restaurant restaurant = new Restaurant();

        final ArrayList<String> dishes1 = new ArrayList<>();
        dishes1.add("суп");
        dishes1.add("пюре");
        dishes1.add("котлета");
        dishes1.add("салат");
        dishes1.add("компот");

        final Order order1 = new Order(1, "Julia", dishes1);

        final ArrayList<String> dishes2 = new ArrayList<>();
        dishes2.add("супчик");
        dishes2.add("пюрешка");
        dishes2.add("бифштекс");
        dishes2.add("огурцы");
        dishes2.add("чай");

        final Order order2 = new Order(2, "Kate", dishes2);

        final ArrayList<String> dishes3 = new ArrayList<>();
        dishes3.add("борщ");
        dishes3.add("пельмени");
        dishes3.add("гречка с подливой");
        dishes3.add("салат оливье");
        dishes3.add("компот");

        final Order order3 = new Order(3, "Anna", dishes3);

        final ArrayList<String> dishes4 = new ArrayList<>();
        dishes4.add("салат Цезарь");
        dishes4.add("картошка фри");
        dishes4.add("сосиски");
        dishes4.add("каша овсяная");
        dishes4.add("кофе");

        final Order order4 = new Order(4, "Mike", dishes4);

        final ArrayList<String> dishes5 = new ArrayList<>();
        dishes5.add("ухо");
        dishes5.add("паста Болоньезе");
        dishes5.add("курица гриль");
        dishes5.add("тушёные овощи");
        dishes5.add("морс");

        final Order order5 = new Order(5, "Igor", dishes5);

        ArrayList<String> dishes6 = new ArrayList<>();
        dishes6.add("шаурма");
        dishes6.add("лимонад");

        Order order6 = new Order(6, "Sergey", dishes6);

        ArrayList<String> dishes7 = new ArrayList<>();
        dishes7.add("пицца");
        dishes7.add("сок");

        Order order7 = new Order(7, "Olga", dishes7);

        ArrayList<String> dishes8 = new ArrayList<>();
        dishes8.add("блины");
        dishes8.add("кисель");

        Order order8 = new Order(8, "Ivan", dishes8);

        ArrayList<String> dishes9 = new ArrayList<>();
        dishes9.add("плов");
        dishes9.add("айран");

        Order order9 = new Order(9, "Marina", dishes9);

        ArrayList<String> dishes10 = new ArrayList<>();
        dishes10.add("гамбургер");
        dishes10.add("кока-кола");

        Order order10 = new Order(10, "Dmitry", dishes10);

        restaurant.add(order1, "Hulio");
        restaurant.add(order2, "Hulio2");
        restaurant.add(order3, "Hulio3");
        restaurant.add(order4, "Hulio4");
        restaurant.add(order5, "Hulio5");
        restaurant.add(order6, "Hulio6");
        restaurant.add(order7, "Hulio7");
        restaurant.add(order8, "Hulio8");
        restaurant.add(order9, "Hulio9");
        restaurant.add(order10, "Hulio10");

        System.out.print(restaurant.toString());

        ArrayList<String> dishes11 = new ArrayList<>();
        dishes11.add("гамбургер");
        dishes11.add("кока-кола");

        Order order11 = new Order(11, "Dmitry", dishes11);

        restaurant.add(order11, "Hulio11");
    }
}