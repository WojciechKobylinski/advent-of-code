package aoc2024;

import static java.lang.System.out;

public class Run {
    
    public static void main(String... args) {
        if (args.length < 2) {
            out.println("Provide a day and case please");
            return;
        }
        System.out.println("RUNNING day: "+args[0] + " case: "+ args[1]);
    }
}
