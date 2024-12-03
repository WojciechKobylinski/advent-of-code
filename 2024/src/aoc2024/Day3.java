package aoc2024;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Day3 implements Day {

    @Override
    public void solve1(List<String> input) {
        int result = 0;
        Pattern p = Pattern.compile("mul\\((\\d+),(\\d+)\\)");
        for (String line : input) {
            Matcher m = p.matcher(line);
            while (m.find()) {
                String matched1st = m.group(1);
                String matched2nd = m.group(2);
                result += Integer.parseInt(matched1st)*Integer.parseInt(matched2nd);
            }
        }

        System.out.println("Result: "+result);
    }

    @Override
    public void solve2(List<String> input) {
        int result = 0;
        
        Pattern p = Pattern.compile("mul\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\)");
        boolean active = true;
        for (String line : input) {
            Matcher m = p.matcher(line);
            while (m.find()) {
                switch (m.group(0)) {
                    case "do()":
                        active = true;
                        break;
                    case "don't()":
                        active = false;
                        break;
                    default:
                        if (active) {
                            result += Integer.parseInt(m.group(1))*Integer.parseInt(m.group(2));
                        }
                        break;
                }
            }
        }

        System.out.println("Result: "+result);
    }
    
}