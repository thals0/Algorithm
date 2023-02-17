import java.util.*;

class Solution {
    public long solution(long n) {
        String ans = "";
        String tmp = Long.toString(n);
        int[] arr = new int[tmp.length()];
        for (int i = 0; i < tmp.length(); i++){
            arr[i] = tmp.charAt(i)-'0';
        }
        Arrays.sort(arr);
        for (int i = arr.length-1; i >= 0; i--){
            ans += arr[i];
        }
        return Long.parseLong(ans);
    }
}