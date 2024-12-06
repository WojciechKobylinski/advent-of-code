package aoc2024;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Day6 implements Day {

    @Override
    public void solve1(List<String> input) {
        int COLS = numCols(input);
        int ROWS = numRows(input);

        char[][] chars = toCharArray(input);

        Set<String> OBSTACLES = new HashSet<String>();
        List<List<Integer>> DIRECTIONS = List.of(
            List.of(0,1),
            List.of(1,0),
            List.of(0,-1),
            List.of(-1,0)
        );
        
        int dir=0, x=0, y=0;

        for (int xx=0; xx<COLS; xx++) {
            for (int yy=0; yy<ROWS; yy++) {
                switch (chars[xx][yy]) {
                    case '#':
                        OBSTACLES.add(xx+"|"+yy);
                        break;
                    case '.':
                        break;
                    case '^':
                        dir = 3;
                        x = xx;
                        y = yy;
                        break;
                    default:
                        break;
                }
            }
        }

        Set<String> PATH = new HashSet<>();

        while (isInside(COLS, ROWS, x, y)) {
            PATH.add(x+"|"+y);
            int newX = x + DIRECTIONS.get(dir).get(0);
            int newY = y + DIRECTIONS.get(dir).get(1);
            if (OBSTACLES.contains(newX+"|"+newY)) {
                dir = (dir+1)%(DIRECTIONS.size());
                newX = x + DIRECTIONS.get(dir).get(0);
                newY = y + DIRECTIONS.get(dir).get(1);
            }
            
            x = newX;
            y = newY;
        }

        System.out.println("Result: "+PATH.size());
    }

    private boolean isInside(int COLS, int ROWS, int x, int y) {
        return x >= 0 && x < COLS && y >= 0 && y < ROWS;
    }

    @Override
    public void solve2(List<String> input) {
        int result = 0;

        

        System.out.println("Result: "+result);
    }
    
}