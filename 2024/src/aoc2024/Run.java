package aoc2024;

import static java.lang.System.out;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Run {
    
    public static void main(String... args) {
        if (args.length < 3) {
            out.println("Provide a day[1..25] variant[1|2] and case[a|b] please");
            return;
        }
        String day = args[0];
        String variant = args[1];
        String fileName = "input"+day+args[2]+".txt";
        try {
            Class<?> clazz = Class.forName("aoc2024.Day"+day);
            Day daySolver = (Day) clazz.getDeclaredConstructor().newInstance();
            List<String> input = Files.readAllLines(Path.of(fileName));
            if (!"2".equals(variant)) {
                daySolver.solve1(input);
            } else {
                daySolver.solve2(input);
            }
        } catch (ClassNotFoundException e) {
            System.err.println("Something's wrong, maybe wrong day: "+day);
        } catch (NoSuchMethodException | InstantiationException | IllegalAccessException | InvocationTargetException e) {
            System.err.println(e.toString());
        } catch (IOException e) {
            System.err.println("Cannot find file "+fileName);
        }
    }
}
