class Solution {
    public String solution(String my_string) {
        StringBuffer answer = new StringBuffer();
        for (int i = 0; i < my_string.length(); i++) {
            char s = my_string.charAt(i);
            if (s != 'a' && s != 'e' && s != 'i' && s != 'o' && s != 'u') {
                answer.append(s);
            }
        }
        return answer.toString();
    }
}
