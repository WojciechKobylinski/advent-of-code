package aoc2024;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Day1 implements Day {

    @Override
    public void solve1(List<String> input) {
        List<Integer> first = new ArrayList<>();
        List<Integer> second = new ArrayList<>();
        
        for (String line : input) {
            String[] parts = line.trim().split("\\s+");
            first.add(Integer.valueOf(parts[0]));
            second.add(Integer.valueOf(parts[1]));
        }
        
        Collections.sort(first);
        Collections.sort(second);
        
        int result = 0;
        int size = Math.min(first.size(), second.size());
        for (int i=0; i<size; i++) {
            result += Math.abs(first.get(i)-second.get(i));
        }
        System.out.println("Result: "+result);
    }

    @Override
    public void solve2(List<String> input) {
        List<Integer> numbers = new ArrayList<>();
        Map<Integer, Integer> freq = new HashMap<>();
        
        for (String line : input) {
            String[] parts = line.trim().split("\\s+");
            numbers.add(Integer.valueOf(parts[0]));
            Integer second = Integer.valueOf(parts[1]);
            freq.put(second, freq.getOrDefault(second, 0) + 1);
        }

        int result = 0;
        for (Integer i : numbers) {
            result += i * freq.getOrDefault(i, 0);
        }

        System.out.println("Result: "+result);
    }
}