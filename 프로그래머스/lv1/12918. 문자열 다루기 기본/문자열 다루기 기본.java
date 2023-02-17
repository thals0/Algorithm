class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        if (s.length() == 4 || s.length() == 6){
            for(int i=0; i<s.length(); i++){
                char ch = s.charAt(i);
                if ('a'<= ch && ch <= 'z' || 'A'<= ch && ch <= 'Z'){
                    answer = false;
                    break;
                }
            }
        } else{
            answer = false;
        }
        return answer;
    }
}