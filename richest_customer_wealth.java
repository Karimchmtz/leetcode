class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        int counter;
        for (int[] array: accounts){
            counter = 0;
            for (int j: array){
                counter += j;
            }
            if (counter > max){
                max = counter;
            }
        }
        return max;
    }
}