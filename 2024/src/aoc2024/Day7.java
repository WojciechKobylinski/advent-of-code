package aoc2024;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Day7 implements Day {

    @Override
    public void solve1(List<String> input) {
        long result = 0;

        for (String line : input) {
            String[] split = line.split(": ");
            long end = Long.parseLong(split[0]);
            long[] inputs = Arrays.stream(split[1].split(" ")).mapToLong(Long::parseLong).toArray();
            result += dfs(inputs[0], end, inputs, 1);
        }

        System.out.println("Result: "+result);
    }

    long dfs(long acc, long expected, long[] inputs, int which) {
        if (which == inputs.length) {
            if (acc == expected) return acc;
            else return 0;
        } 
        if (acc > expected) return 0;
        return Math.max(dfs(acc+inputs[which], expected, inputs, which+1), dfs(acc*inputs[which], expected, inputs, which+1));
    }

    @Override
    public void solve2(List<String> input) {
        long result = 0;

        for (String line : input) {
            String[] split = line.split(": ");
            long end = Long.parseLong(split[0]);
            long[] inputs = Arrays.stream(split[1].split(" ")).mapToLong(Long::parseLong).toArray();
            result += dfs2(inputs[0], end, inputs, 1);
        }

        System.out.println("Result: "+result);
    }
    
    long dfs2(long acc, long expected, long[] inputs, int which) {
        if (which == inputs.length) {
            if (acc == expected) return acc;
            else {
                // System.out.println(acc+"!="+expected);
                return 0;}
        } 
        if (acc > expected) {
            // System.out.println(acc+">"+expected);
            return 0;
        }

        // System.out.println("Chk "+acc+" "+which);

        long best = 0;

        try {
            best = dfs2(concat(acc,inputs[which]), expected, inputs, which+1);
        } catch (TooBigException e) {}
        
        try {
            best = Math.max(best, dfs2(add(acc,inputs[which]), expected, inputs, which+1));
        } catch (TooBigException e) {System.out.println("Add");}
        
        try {
            best = Math.max(best, dfs2(mul(acc,inputs[which]), expected, inputs, which+1));
        } catch (TooBigException e) {System.out.println("Mul");}
        return best;
    }

    long concat(long a, long b) {
        String s = ("" + a) + b;
        if (s.length() > 19 || s.compareTo(String.valueOf(Long.MAX_VALUE)) > 0) throw new TooBigException();
        return Long.parseLong(s);
    }

    long add(long a, long b) {
        if (a > 0 && b > Long.MAX_VALUE - a) {
            throw new TooBigException();
        }
        return a + b;
    }

    long mul(long a, long b) {
        if (a > Long.MAX_VALUE / b) {
            throw new TooBigException();
        }
        return a * b;
    }

    class TooBigException extends RuntimeException {}
    
}