package aoc2024;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Day2 implements Day {

    @Override
    public void solve1(List<String> input) {
        int countSafe = 0;

        for (String line : input) {
            List<Integer> levels = Arrays.stream(line.split("\\s+")).map(Integer::parseInt).collect(Collectors.toList());
            if (findBadIndex(levels) == null) {
                countSafe++;
            }
        }
        
        System.out.println("Result: "+countSafe);
    }

    @Override
    public void solve2(List<String> input) {
        int countSafe = 0;

        outer:
        for (String line : input) {
            List<Integer> levels = Arrays.stream(line.split("\\s+")).map(Integer::parseInt).collect(Collectors.toList());
            Integer badIndex = findBadIndex(levels);
            if (badIndex == null) {
                countSafe++;
                continue;
            }
            for (int i=0;i<levels.size();i++) {
                List<Integer> without = new ArrayList<>(levels);
                int removeIndex = i;
                without.remove(removeIndex);
                if (findBadIndex(without) == null) {
                    countSafe++;
                    continue outer;
                }
            }
            
        }
        
        System.out.println("Result: "+countSafe);
    }

    private Integer findBadIndex(List<Integer> levels) {
        int lastDiff = levels.get(1) - levels.get(0);
        for (int i=0; i<levels.size()-1; i++) { 
            int diff = levels.get(i+1) - levels.get(i);
            if (diff * lastDiff < 0) { // one of them is negative
                return i;
            };
            if (Math.abs(diff) < 1 || Math.abs(diff) > 3)  {
                return i;
            }
            lastDiff = diff;
        }
        return null;
    }

    
}