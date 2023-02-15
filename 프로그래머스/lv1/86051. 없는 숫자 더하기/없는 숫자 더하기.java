class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int sum = 0;
        int total = 0;
        for (int i = 0; i < 10; i++) {
            sum += i;
        }

        for (int number : numbers) {
            total += number;
        }
        answer = sum - total;


        return answer;
    }
}