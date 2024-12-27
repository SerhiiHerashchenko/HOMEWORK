package Lab4_HashMap;
import java.util.ArrayList;

public class Order {
    private final int orderNumber;
    private final String customerName;
    private final ArrayList<String>dishes;

    public Order(int orderNumber, String customerName, ArrayList<String> dishes){
        this.customerName = customerName;
        this.orderNumber = orderNumber;
        this.dishes = dishes;
    }
    public Order(){
        this.customerName = "";
        this.orderNumber = -1;
        this.dishes = new ArrayList<String>();
    }

    public int GetOrderNumber(){
        return this.orderNumber;
    }

    @Override
    public String toString(){
        final String s = customerName + ": " + dishes.toString() + " \nOrder number:" + orderNumber;
        return s;
    }
}
