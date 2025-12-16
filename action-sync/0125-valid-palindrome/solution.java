class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder filteredChars = new StringBuilder();
        for ( int i = 0; i <s.length();i++){
            char c = s.charAt(i);
            if (Character.isLetterOrDigit(c)){
                filteredChars.append(Character.toLowerCase(c));
            }
        }
        String normalStr = filteredChars.toString();
        String reversedStr = new StringBuilder(normalStr).reverse().toString();
        return normalStr.equals(reversedStr);
        
    }
}
