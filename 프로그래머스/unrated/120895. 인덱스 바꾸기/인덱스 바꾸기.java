class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        char[] ca = my_string.toCharArray();
        
        char tmp = ca[num1];
        ca[num1] = ca[num2];
        ca[num2] = tmp;
        
        answer = new String(ca);
        return answer;
    }
}