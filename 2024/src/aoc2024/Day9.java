package aoc2024;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

class Day9 implements Day {

    @Override
    public void solve1(List<String> input) {
        long result = 0L;

        char[] LINE = input.get(0).toCharArray();
        
        int size = 0;
        for (char block : LINE) {
            size += block - '0';
        }

        int[] DISK = new int[size];
        boolean free = false;
        int pos = 0;
        int nr = 0;
        for (char block : LINE) {
            int blockLen = block - '0';
            for (int j=0; j<blockLen; j++) {
                DISK[pos+j] = free ? -1 : nr;
            }
            pos += blockLen;
            if (free) {
                free = false;
                nr++;
            } else {
                free = true;
            }
        }

        for (int from=0, to=DISK.length-1; from<=to; from++) {
            if (DISK[from] >= 0) {
                result += DISK[from]*from;
            } else {
                result += DISK[to]*from;
                to--;
                while (to>from && DISK[to] < 0) {
                    to--;
                }
            }
        }

        System.out.println("Result: "+result);
    }

    class Block {
        Integer val;
        Boolean free;
        Integer start;
        Integer len;
        public Block(Integer val, Boolean free, Integer start, Integer len) {
            this.val=val;
            this.free=free;
            this.start=start;
            this.len=len;
        }
    }

    @Override
    public void solve2(List<String> input) {
        long result = 0L;

        char[] LINE = input.get(0).toCharArray();
        LinkedList<Block> BLOCKS = new LinkedList<>();

        int NR_BLOCKS = 0;
        int start = 0;
        boolean free = false;
        for (char block : LINE) {
            int blockLen = block - '0';
            BLOCKS.add(new Block(NR_BLOCKS, free, start, blockLen));
            start += blockLen;
            if (free) {
                free = false;
            } else {
                NR_BLOCKS++;
                free = true;
            }
        }
        
        Iterator<Block> fromBack = BLOCKS.descendingIterator();
        while (fromBack.hasNext()) {
            Block b = fromBack.next();
            if (b.free) continue;
            Iterator<Block> it = BLOCKS.iterator();
            // try to find space in front of disk
            while (it.hasNext()) {
                Block o = it.next();
                if (b.val == o.val && b.free == o.free) break;
                if (o.free && b.len <= o.len) {
                    b.start = o.start;
                    o.start += b.len;
                    o.len -= b.len;
                    break;
                }
            }
            result += checksum(b.start, b.val, b.len);
        }

        System.out.println("Result: "+result);
    }

    private long checksum(int start, int val, int len) {
        long result = 0;
        for (int i=start; i<start+len; i++) result += i*val;
        return result;
    }
}