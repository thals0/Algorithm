class Solution {
    public String solution(int n) {
        String ans = "";
        for(int i=1; i<=n; i++){
            if(i%2 == 0){
                ans += "박";
            } else{
                ans += "수";
            }
        }
        return ans;
    }
}