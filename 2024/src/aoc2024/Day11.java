package aoc2024;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Day11 implements Day {

    @Override
    public void solve1(List<String> input) {
        List<String> parts = List.of(input.get(0).split(" "));
        for (int i=0; i<25; i++) {
            List<String> newParts = new ArrayList<>();
            for (String part : parts) {
                newParts.addAll(blink(part));
            }
            parts = newParts;
        }
        
        System.out.println("Result: "+parts.size());
    }

    List<String> blink(String s) {
        if ("0".equals(s)) return List.of("1");
        if (s.length()  % 2 == 0) {
            String first = "" + Long.parseLong(s.substring(0, s.length()/2));
            String second = "" + Long.parseLong(s.substring(s.length()/2));
            return List.of(first, second);
        } else {
            return List.of("" + (Long.parseLong(s)*2024));
        }
    }

    @Override
    public void solve2(List<String> input) {
        long result = 0L;

        List<String> parts = List.of(input.get(0).split(" "));
        Map<String, Integer> CACHE = new HashMap<>();
        for (String s: parts) {
            long val = blinkCached(s, 75, CACHE);
            for (int i=0; i<75; i++) {
                List<String> newParts = new ArrayList<>();
                for (String part : parts) {
                    newParts.addAll(blink(part));
                }
                parts = newParts;
            }
            result += val;
        }
        
        System.out.println("Result: "+result);
    }


    // out of memory in this aproach
    int blinkCached(String s, int level, Map<String, Integer> CACHE) {
        if (level == 1) return blink(s).size();
        String key = level+":"+s;
        if (CACHE.containsKey(key)) return CACHE.get(key);
        if ("0".equals(s)) {
            int result = blinkCached("1", level-1, CACHE);
            CACHE.put(key, result);
            return result;
        }
        if (s.length()  % 2 == 0) {
            int result = blinkCached(s.substring(0, s.length()/2), level-1, CACHE);
            result += blinkCached(s.substring(s.length()/2), level-1, CACHE);
            CACHE.put(key, result);
            return result;
        } else {
            int result = blinkCached("" + (Long.parseLong(s)*2024), level-1, CACHE);
            CACHE.put(key, result);
            return result;
        }
    }

}
