class Solution {
    public String solution(String s) {
        StringBuilder ans = new StringBuilder();
        String[] words = s.split(" ", -1);

        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);

                if (i % 2 == 0) {
                    ans.append(Character.toUpperCase(ch));
                } else {
                    ans.append(Character.toLowerCase(ch));
                }
            }
            ans.append(" ");
        }

        // 마지막 공백 제거
        if (ans.length() > 0) {
            ans.deleteCharAt(ans.length() - 1);
        }

        return ans.toString();
    }
}
