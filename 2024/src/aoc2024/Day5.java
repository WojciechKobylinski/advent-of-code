package aoc2024;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Day5 implements Day {

    @Override
    public void solve1(List<String> input) {
        int result = 0;

        Set<String> ORDERINGS = new HashSet<>();
        List<String> PAGINGS = new ArrayList<>();
        
        for (String line : input) {
            if (line.contains("|")) {
                ORDERINGS.add(line);
            } else if (line.contains(",")) {
                PAGINGS.add(line);
            }
        }

        nextPage:
        for (String paging : PAGINGS) {
            String[] pages = paging.split(",");
            for (int i=0; i<pages.length-1; i++) {
                for (int j=i+1; j<pages.length; j++) {
                    String wrong = pages[j] + "|" + pages[i];
                    if (ORDERINGS.contains(wrong)) {
                        continue nextPage;
                    };
                }
            }
            result += Integer.parseInt(pages[pages.length/2]);
        }

        System.out.println("Result: "+result);
    }

    @Override
    public void solve2(List<String> input) {
        int result = 0;

        Set<String> ORDERINGS = new HashSet<>();
        List<String> PAGINGS = new ArrayList<>();
        
        for (String line : input) {
            if (line.contains("|")) {
                ORDERINGS.add(line);
            } else if (line.contains(",")) {
                PAGINGS.add(line);
            }
        }

        for (String paging : PAGINGS) {
            String[] pages = paging.split(",");
            boolean sorted = true;

            outer:
            for (int i=0; i<pages.length-1; i++) {
                for (int j=i+1; j<pages.length; j++) {
                    String wrong = pages[j] + "|" + pages[i];
                    if (ORDERINGS.contains(wrong)) {
                        sorted = false;
                        break;
                    };
                }
                
            }
            if (!sorted) {
                Arrays.sort(pages, (a, b) -> ORDERINGS.contains(a+"|"+b) ? -1 : ORDERINGS.contains(b+"|"+a) ? 11 : 0) ;
                result += Integer.parseInt(pages[pages.length/2]);
            }
        }
        

        System.out.println("Result: "+result);
    }
    
}