import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int count = 0;
        for (int num : arr) {
            if (num % divisor == 0) {
                count++;
            }
        }

        if (count == 0) {
            return new int[]{-1};
        }

        int[] ans = new int[count];
        int index = 0;
        for (int num : arr) {
            if (num % divisor == 0) {
                ans[index++] = num;
            }
        }
        Arrays.sort(ans);
        return ans;
    }
}