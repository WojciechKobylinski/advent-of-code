package aoc2024;

import static java.lang.System.out;

import java.lang.reflect.InvocationTargetException;

public class Run {
    
    public static void main(String... args) {
        if (args.length < 2) {
            out.println("Provide a day and case please");
            return;
        }
        String day = args[0];
        String fileName = "input"+day+args[1]+".txt";
        try {
            Class clazz = Class.forName("aoc2024.Day"+day);
            @SuppressWarnings("unchecked")
            Day daySolver = (Day) clazz.getDeclaredConstructor().newInstance();
            daySolver.solve(fileName);
        } catch (ClassNotFoundException e) {
            System.err.println("Something's wrong, maybe wrong day: "+day);
        } catch (NoSuchMethodException | InstantiationException | IllegalAccessException | InvocationTargetException e) {
            System.err.println(e.toString());
        }
    }
}
