package aoc2024;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

class Day10 implements Day {

    @Override
    public void solve1(List<String> input) {
        int result = 0;

        int[][] AREA = toIntArray(input);
        int COLS = numCols(input);
        int ROWS = numRows(input);

        for (int x=0; x<COLS; x++) {
            for (int y=0; y<ROWS; y++) {
                if (AREA[x][y] == 0) {
                    result += countTrailheads(AREA, x, y, COLS, ROWS);
                }
            }
        }
        
        System.out.println("Result: "+result);
    }

    int countTrailheads(int[][] AREA, int startX, int startY, int COLS, int ROWS) {
        int result=0;
        LinkedList<Integer> QUEUE = new LinkedList<>();
        Set<Integer> VISITED = new HashSet<>();
        QUEUE.add(point(startX,startY));
        VISITED.add(point(startX,startY));

        while (!QUEUE.isEmpty()) {
            int point = QUEUE.pop();
            int x = x(point);
            int y = y(point);
            int height = AREA[x][y];
            if (height == 9) result++;

            for (int n: neighbors(x, y, COLS, ROWS)) {
                if (VISITED.contains(n)) continue;
                int neighborHeight = AREA[x(n)][y(n)];
                if (neighborHeight == height+1) {
                    QUEUE.add(n);
                    VISITED.add(n);
                }
            }
        }
        return result;
    }

    List<Integer> neighbors(int x, int y, int COLS, int ROWS) {
        List<Integer> result = new ArrayList<>();
        if (x>0) result.add(point(x-1, y));
        if (x<COLS-1) result.add(point(x+1, y));
        if (y>0) result.add(point(x, y-1));
        if (y<ROWS-1) result.add(point(x, y+1));
        return result;
    }

    int point(int x, int y) {
        return 100*x+y;
    }

    int x(int p) {
        return p/100;
    }

    int y(int p) {
        return p%100;
    }

    @Override
    public void solve2(List<String> input) {
        long result = 0L;
        int[][] AREA = toIntArray(input);
        int COLS = numCols(input);
        int ROWS = numRows(input);

        for (int x=0; x<COLS; x++) {
            for (int y=0; y<ROWS; y++) {
                if (AREA[x][y] == 0) {
                    result += countTrails(AREA, x, y, COLS, ROWS);
                }
            }
        }
        
        System.out.println("Result: "+result);
    }

    int countTrails(int[][] AREA, int startX, int startY, int COLS, int ROWS) {
        int result=0;
        LinkedList<Integer> QUEUE = new LinkedList<>();
        QUEUE.add(point(startX,startY));

        while (!QUEUE.isEmpty()) {
            int point = QUEUE.pop();
            int x = x(point);
            int y = y(point);
            int height = AREA[x][y];
            if (height == 9) result++;

            for (int n: neighbors(x, y, COLS, ROWS)) {
                int neighborHeight = AREA[x(n)][y(n)];
                if (neighborHeight == height+1) {
                    QUEUE.add(n);
                }
            }
        }
        return result;
    }
}
