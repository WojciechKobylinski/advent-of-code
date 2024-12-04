package aoc2024;

import java.util.ArrayList;
import java.util.List;

class Day4 implements Day {

    @Override
    public void solve1(List<String> input) {
        int result = 0;
        
        List<Integer[][]> ALL_DIRECTIONS = new ArrayList<>();
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {0,-1}, {0,-2}, {0,-3}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {0,1}, {0,2}, {0,3}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {-1,-1}, {-2,-2}, {-3,-3}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {1,1}, {2,2}, {3,3}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {-1,0}, {-2,0}, {-3,0}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {1,0}, {2,0}, {3,0}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {-1,1}, {-2,2}, {-3,3}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {1,-1}, {2,-2}, {3,-3}});
        
        char[][] chars = toCharArray(input);

        int COLS = numCols(input);
        int ROWS = numRows(input);

        String PATTERN = "XMAS";

        result = countPatterns(PATTERN, ALL_DIRECTIONS, chars, COLS, ROWS);

        System.out.println("Result: "+result);
    }

    @Override
    public void solve2(List<String> input) {
        int result = 0;
        
        List<Integer[][]> ALL_DIRECTIONS = new ArrayList<>();
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {-1,-1}, {-1,1}, {1,-1}, {1,1}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {-1,-1}, {1,-1}, {-1,1}, {1,1}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {1,1}, {-1,1}, {1,-1}, {-1,-1}});
        ALL_DIRECTIONS.add(new Integer[][]{{0,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}});
        
        char[][] chars = toCharArray(input);

        int COLS = numCols(input);
        int ROWS = numRows(input);

        String PATTERN = "AMMSS";

        result = countPatterns(PATTERN, ALL_DIRECTIONS, chars, COLS, ROWS);

        System.out.println("Result: "+result);
    }

    private int countPatterns(String PATTERN, List<Integer[][]> ALL_DIRECTIONS, char[][] chars, int COLS, int ROWS) {
        int result = 0;
        for (int x=0; x<COLS; x++) {
            for (int y=0; y<ROWS; y++) {
                if (chars[x][y] == PATTERN.charAt(0)) {
                    // check other directions for 'MAS' sequence
                    nextDir:
                    for (Integer[][] dir : ALL_DIRECTIONS) {
                        for (int offset=0; offset<PATTERN.length(); offset++) {
                            int xx = x + dir[offset][0];
                            int yy = y + dir[offset][1];
                            if (xx < 0 || xx >= COLS || yy < 0 || yy >= ROWS || chars[xx][yy] != PATTERN.charAt(offset)) {
                                continue nextDir;
                            }
                        }
                        result++;
                    }
                }
            }
        }
        return result;
    }
    
}