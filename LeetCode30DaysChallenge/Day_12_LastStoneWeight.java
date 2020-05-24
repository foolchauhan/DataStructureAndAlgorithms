import java.util.Collections;
import java.util.PriorityQueue;

class LastStoneWeight {
    LastStoneWeight lastStoneWeight;

    // @BeforeEach
    // public void init() {
    //     lastStoneWeight = new LastStoneWeight();
    // }

    // @Test
    // public void test_first() {
    //     int result = lastStoneWeight(new int[]{2, 7, 4, 1, 8, 1});
    //     Assertions.assertEquals(1,result);
    // }

    // @Test
    // public void test_second() {
    //     int result = lastStoneWeight(new int[]{2});
    //     Assertions.assertEquals(2,result);

    // }

    public int lastStoneWeight(int[] stones) {
        if(stones==null)
            return 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < stones.length; i++) {
            pq.offer(stones[i]);
        }
        while (pq.size() > 1) {
            int first = pq.poll();
            int second = pq.poll();
            if (first != second) {
                int rem = Math.abs(first - second);
                pq.offer(rem);
            }
        }
        return pq.size()==1 ? pq.poll() : 0;
    }
}