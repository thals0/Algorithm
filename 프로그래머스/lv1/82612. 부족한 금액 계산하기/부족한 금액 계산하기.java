class Solution {
    public long solution(int price, int money, int cnt) {
        long answer = 0;
        long sum = 0;
        for(int i=1; i<=cnt; i++){
            sum += (long) (price * i);
        }
        if ((sum-money) > 0){
            answer = (long) (sum-money);
        } 

        return answer;
    }
}