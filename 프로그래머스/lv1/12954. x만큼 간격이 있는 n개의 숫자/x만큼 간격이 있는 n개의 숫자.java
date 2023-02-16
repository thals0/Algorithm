class Solution {
    public long[] solution(int x, int n) {
        long[] ans = new long[n];
        long num = x;
        for(int i=0; i<n; i++){
            ans[i] += num;
            num += x;
        }
        return ans;
    }
}
