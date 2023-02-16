class Solution {
    boolean solution(String s) {
        boolean ans = true;
        s = s.toLowerCase();
        char[] arr = s.toCharArray();
        int cntp =0, cnty =0;
        for(char ch: arr){
            if(ch == 'p'){
                cntp += 1;
            } else if(ch == 'y'){
                cnty += 1;
            }
        }
        
        if (cntp != cnty){
            ans = false;
        }
        return ans;
    }
}