package aoc2024;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Day8 implements Day {

    @Override
    public void solve1(List<String> input) {
        char[][] chars = toCharArray(input);
        int COLS = numCols(input);
        int ROWS = numRows(input);

        Map<Character, List<List<Integer>>> ANTENNAS = new HashMap<>();

        for (int x=0; x<COLS; x++) {
            for (int y=0; y<ROWS; y++) {
                char c = chars[x][y];
                if (c != '.') {
                    if (!ANTENNAS.containsKey(c)) {
                        ANTENNAS.put(c, new ArrayList<>());
                    }
                    ANTENNAS.get(c).add(List.of(x,y));
                }
            }
        }

        Set<String> ANTINODES = new HashSet<>();

        for (Map.Entry<Character, List<List<Integer>>> antenna : ANTENNAS.entrySet()) {
            List<List<Integer>> positions = antenna.getValue();
            for (int i=0; i<positions.size()-1; i++) {
                for (int j=i+1; j<positions.size(); j++) {
                    int xi = positions.get(i).get(0);
                    int yi = positions.get(i).get(1);
                    int xj = positions.get(j).get(0);
                    int yj = positions.get(j).get(1);
                    int x1 = xi - (xj - xi);
                    int y1 = yi - (yj - yi);
                    int x2 = xj - (xi - xj);
                    int y2 = yj - (yi - yj);
                    if (isInside(COLS, ROWS, x1, y1)) ANTINODES.add(x1+"|"+y1);
                    if (isInside(COLS, ROWS, x2, y2)) ANTINODES.add(x2+"|"+y2);
                }
            }
        }

        System.out.println("Result: "+ANTINODES.size());
    }

    
    private boolean isInside(int COLS, int ROWS, int x, int y) {
        return x >= 0 && x < COLS && y >= 0 && y < ROWS;
    }

    @Override
    public void solve2(List<String> input) {
        char[][] chars = toCharArray(input);
        int COLS = numCols(input);
        int ROWS = numRows(input);

        Map<Character, List<List<Integer>>> ANTENNAS = new HashMap<>();

        for (int x=0; x<COLS; x++) {
            for (int y=0; y<ROWS; y++) {
                char c = chars[x][y];
                if (c != '.') {
                    if (!ANTENNAS.containsKey(c)) {
                        ANTENNAS.put(c, new ArrayList<>());
                    }
                    ANTENNAS.get(c).add(List.of(x,y));
                }
            }
        }

        Set<String> ANTINODES = new HashSet<>();

        for (Map.Entry<Character, List<List<Integer>>> antenna : ANTENNAS.entrySet()) {
            List<List<Integer>> positions = antenna.getValue();
            for (int i=0; i<positions.size()-1; i++) {
                for (int j=i+1; j<positions.size(); j++) {
                    int xi = positions.get(i).get(0);
                    int yi = positions.get(i).get(1);
                    int xj = positions.get(j).get(0);
                    int yj = positions.get(j).get(1);
                    int dx = xj - xi;
                    int dy = yj - yi;
                    for (int x=xi, y=yi; isInside(COLS, ROWS, x, y); x-= dx, y-=dy) {
                        ANTINODES.add(x+"|"+y);
                    }
                    for (int x=xj, y=yj; isInside(COLS, ROWS, x, y); x+= dx, y+=dy) {
                        ANTINODES.add(x+"|"+y);
                    }
                }
            }
        }

        System.out.println("Result: "+ANTINODES.size());

    }
}