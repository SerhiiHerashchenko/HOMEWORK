package Lab4_HashMap;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class Restaurant {
    private final HashMap<String, Order> orders = new HashMap<String, Order>();

    public void add(Order order, String waiterName){
        if (orders.size()>=10) {
            System.out.println("All waiters are busy! Please, wait a little bit");
            return;
        }
        orders.put(waiterName, order);
    }

    public void removeOrder(int orderNumber){
        final String neededWaiter = getWaiter(orderNumber);

        orders.remove(neededWaiter);
    }

    public Order getOrder(int orderNumber){
        String neededWaiter = getWaiter(orderNumber);

        return orders.get(neededWaiter);
    } 

    private String getWaiter(int orderNumber){
        if (orderNumber < 1 && orderNumber > orders.size()) {
            return null;
        }

        final Set<Map.Entry<String,Order>> s = orders.entrySet();
        Order neededOrder = new Order();
        String neededWaiter = "";

        for (Order order : orders.values()) {
            if (order.GetOrderNumber() == orderNumber) {
                neededOrder = order;
                break;
            }
        }

        for (Entry<String,Order> entry : s) {
            if (neededOrder.equals(entry.getValue())) {
                neededWaiter = entry.getKey();
            }
        }
        return neededWaiter;
    } 

    @Override
    public String toString(){
        String s = "";
        final Set<Map.Entry<String,Order>> waiters_orders = orders.entrySet();
        final ArrayList<String> waiters = new ArrayList<>();
        for (Entry<String,Order> entry : waiters_orders) {
            waiters.add(entry.getKey());
        }
        for (String waiter : waiters) {
            s += (waiter + ":\n" + orders.get(waiter).toString() + "\n\n");
        }
        return s;
    }
}