class Solution {
    public long[] solution(long x, int n) {
        long[] ans = new long[n];
        long tmp = x;
        for(int i=0; i<n; i++){
            ans[i] += x;
            x += tmp;
        }
        return ans;
    }
}
