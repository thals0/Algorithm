class Solution {
    public long solution(long price, long money, long cnt) {
        long answer = 0;
        long sum = 0;
        for(int i=1; i<=cnt; i++){
            sum += price * i;
        }
        if ((sum-money) > 0){
            answer = sum-money;
        } 

        return answer;
    }
}