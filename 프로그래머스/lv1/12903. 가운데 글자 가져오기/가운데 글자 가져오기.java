class Solution {
    public String solution(String s) {
        String answer = "";
        int idx = 0;
        if (s.length() % 2 != 0){
            idx = s.length() / 2 ;
            answer = answer + s.charAt(idx);
        } else {
            int idx2 = 0;
            idx = s.length()/2 -1;
            idx2 = s.length()/2;
            answer = answer + s.charAt(idx) + s.charAt(idx2);
            
        }
        return answer;
    }
}