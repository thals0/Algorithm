class Solution {
    public int[] solution(int[] arr) {
        int x = arr[0];
        for(int i=0; i<arr.length; i++){
            if(arr[i] < x){
                x = arr[i];
            } 
        }
        
        if (arr.length == 1){
            return new int[]{-1};
        }
        
        int[] ans = new int[arr.length-1];
        
        int index = 0;
        
        for(int i=0; i < arr.length; i++){
            if (arr[i] == x){
                continue;
            } 
            ans[index++] = arr[i];
        }
        return ans;
    }
}