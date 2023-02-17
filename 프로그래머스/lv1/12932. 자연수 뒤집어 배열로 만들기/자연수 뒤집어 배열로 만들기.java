class Solution {
    public int[] solution(long n) {
        String tmp = Long.toString(n);
        int[] arr = new int[tmp.length()];
        for (int i = tmp.length()-1; i >= 0; i--){
            arr[tmp.length()-1-i] = tmp.charAt(i) - '0';
        }
        return arr;
    }
}
