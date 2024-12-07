package aoc2024;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Day6 implements Day {
        
    int dir=0, x=0, y=0;

    List<List<Integer>> DIRECTIONS = List.of(
        List.of(0,1),
        List.of(1,0),
        List.of(0,-1),
        List.of(-1,0)
    );

    @Override
    public void solve1(List<String> input) {
        int COLS = numCols(input);
        int ROWS = numRows(input);

        Set<String> OBSTACLES = findObstacles(COLS, ROWS, toCharArray(input));

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

    private Set<String> findObstacles(int COLS, int ROWS, char[][] chars) {
        Set<String> OBSTACLES = new HashSet<>();
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
        return OBSTACLES;
    }

    private boolean isInside(int COLS, int ROWS, int x, int y) {
        return x >= 0 && x < COLS && y >= 0 && y < ROWS;
    }

    @Override
    public void solve2(List<String> input) {
        int result = 0;

        int COLS = numCols(input);
        int ROWS = numRows(input);

        Set<String> OBSTACLES = findObstacles(COLS, ROWS, toCharArray(input));

        int[][] PATH = new int[COLS][ROWS];

        while (isInside(COLS, ROWS, x, y)) {
            
            // System.out.println("AT: "+x+" "+y + " dir "+dir);    
            PATH[x][y] |= (1 << dir);
            // System.out.println("ADD "+x+" "+y+" "+PATH[x][y]+" " + (1 << dir));    

            
            boolean newCycle = check((dir+1)%(DIRECTIONS.size()), OBSTACLES, x, y, PATH, COLS, ROWS);
            if (newCycle) {
                result ++;
            }
            // System.out.println("CHK PATH["+x+"]["+y+"] "+PATH[x][y]+" <- " +turnDir);    
            // have we been there already? if yes, then there would be a cycle
            // if (isInside(COLS, ROWS, x, y) && ((PATH[x][y] & (1 << turnDir)) > 0)) {
            //     System.out.println("CYCLE  DETECTED AT "+x+" "+y+ "!!!!!!!!!1");    
            //     result++;
            // }

            int newX = x + DIRECTIONS.get(dir).get(0);
            int newY = y + DIRECTIONS.get(dir).get(1);
            if (OBSTACLES.contains(newX+"|"+newY)) {
                dir = (dir+1)%(DIRECTIONS.size());
                newX = x + DIRECTIONS.get(dir).get(0);
                newY = y + DIRECTIONS.get(dir).get(1);
            } else {
                // there was no obstacle. but what if we would plant it there...
                
            }
            x = newX;
            y = newY;
            // System.out.println("MOVED TO "+x+" "+y);    

        }

        System.out.println("Result: "+result);
    }

    Map<String, Boolean> MEMO_MAP = new HashMap<>();

    boolean check(int startDir, Set<String> OBSTACLES, int x, int y, int[][] PATH, int COLS, int ROWS) {
        int aDir = startDir;
        while (isInside(COLS, ROWS, x, y)) {
            int newX = x + DIRECTIONS.get(aDir).get(0);
            int newY = y + DIRECTIONS.get(aDir).get(1);
            if (OBSTACLES.contains(newX+"|"+newY)) {
                aDir = (aDir+1)%(DIRECTIONS.size());
                newX = x + DIRECTIONS.get(aDir).get(0);
                newY = y + DIRECTIONS.get(aDir).get(1);
            }
            if ((PATH[x][y] & (1 << aDir)) > 0) return true;
            x = newX;
            y = newY;
        }
        return false;
    }

    // TODO dynamic programming of check(x, y, dir)
    
}