package aoc2024;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Day12 implements Day {

    char[][] INPUT;
    int COLS;
    int ROWS;

    @Override
    public void solve1(List<String> input) {
        long result = 0;

        INPUT = toCharArray(input);
        COLS = numCols(input);
        ROWS = numRows(input);

        Set<Integer> VISITED = new HashSet<>();

        for (int x=0; x<COLS; x++) {
            for (int y=0; y<ROWS; y++) {
                if (!VISITED.contains(p(x,y))) {
                    Set<Integer> area = new HashSet<>();
                    visit(INPUT[x][y], x, y, VISITED, area);
                    int fence = 4 * area.size();
                    for (int p : area) {
                        if (area.contains(left(p))) fence -= 2;
                        if (area.contains(up(p))) fence -= 2;
                    }
                    result += area.size() * fence;
                }
            }
        }

        println("Result: "+result);
    }

    void visit(char c, int x, int y, Set<Integer> VISITED, Set<Integer> area) {
        if (INPUT[x][y] == c && !VISITED.contains(p(x,y))) {
            VISITED.add(p(x,y));
            area.add(p(x,y));
            for (int n : neighbors(x, y)) {
                visit(c, x(n), y(n), VISITED, area);
            }
        }
    }

    List<Integer> neighbors (int x, int y) {
        List<Integer> result = new ArrayList<>();
        if (x>0) result.add(p(x-1,y));
        if (x<ROWS-1) result.add(p(x+1,y));
        if (y>0) result.add(p(x,y-1));
        if (y<COLS-1) result.add(p(x,y+1));
        return result;
    }

    @Override
    public void solve2(List<String> input) {
        long result = 0;

        INPUT = toCharArray(input);
        COLS = numCols(input);
        ROWS = numRows(input);

        Set<Integer> VISITED = new HashSet<>();

        for (int x=0; x<COLS; x++) {
            for (int y=0; y<ROWS; y++) {
                if (!VISITED.contains(p(x,y))) {
                    Set<Integer> area = new HashSet<>();
                    visit(INPUT[x][y], x, y, VISITED, area);
                    // println(INPUT[x][y] + " Area "+Arrays.toString(area.toArray()));
                    Set<Integer> sides = area.stream().filter(p -> !area.containsAll(Set.of(up(p), down(p), left(p), right(p)))).collect(Collectors.toSet());
                    // println(INPUT[x][y] + " Edge "+Arrays.toString(sides.toArray()));
                    
                    // this produces more than one outline, but there is one that is the outer and we just go through this one
                    Set<Integer> outer = buildOuter(sides);
                    // println("OUTER "+Arrays.toString(outer.toArray()));

                    int edgeCount = countEdges(outer);

                    println("EDGES "+edgeCount);

                    
                    println(INPUT[x][y] + " -->  "+area.size()+" * "+edgeCount);

                    result += area.size() * edgeCount;
                }
            }
        }

        println("Result: "+result);
    }


    Set<Integer> buildOuter(Set<Integer> sides) {
        return sides.stream().flatMap(p -> outer(x(p), y(p)).stream()).filter(p -> !sides.contains(p)).collect(Collectors.toSet());
    }
    

    int p(int x, int y) { return 1000*x + y; }

    int x(int p) { return p/1000; }
    int y(int p) { return p%1000; }

    int up(int p) { return p-1000; }
    int down(int p) { return p+1000; }
    int left(int p) { return p-1; }
    int right(int p) { return p+1; }

    
    // all points around (x,y)
    List<Integer> outer (int x, int y) {
        List<Integer> result = new ArrayList<>();
        result.add(p(x-1,y));
        result.add(p(x+1,y));
        result.add(p(x,y-1));
        result.add(p(x,y+1));
        result.add(p(x-1,y-1));
        result.add(p(x+1,y-1));
        result.add(p(x-1,y+1));
        result.add(p(x+1,y+1));
        return result;
    }

    int countEdges(Set<Integer> outline) {
        int result = 0;
        // assumption: we start from the smallest value which is most to the north and then to the left. That means
        int first = outline.stream().min(Integer::compareTo).orElse(null);
        int prev = first;
        int prevDir = 0;
        Set<Integer> VISITED = new HashSet<>();
        int curr =first;
        do {
            VISITED.add(curr);
            int dir = curr - prev;
            // count turns
            if (dir != prevDir) result++;
            prevDir = dir;
            prev = curr;
            curr = next(curr, outline, VISITED, first);
        } while (curr != first);
        return result;
    }

    int next(int curr, Set<Integer> outline, Set<Integer> VISITED, int first) {
        for (int n : Set.of(up(curr), down(curr), left(curr), right(curr))) {
            if (outline.contains(n) && !VISITED.contains(n)) return n;
        }
        return first;
    }
}
