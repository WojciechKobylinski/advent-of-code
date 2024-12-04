package aoc2024;

import java.util.List;

interface Day {
    void solve1(List<String> input);
    void solve2(List<String> input);
    
    default char[][] toCharArray(List<String> input) {
        int rows = numRows(input);
        int cols = numCols(input);

        char[][] result = new char[cols][rows];
        int i=0;
        for (String line : input) {
            result[i] = line.toCharArray();
            i++;
        }
        
        return result;
    }

    default int numRows(List<String> input) {
        return input.size();
    }

    default int numCols(List<String> input) {
        return input.size() > 0 ? input.get(0).length() : 0;
    }
}
