class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // 跳过左边非字母数字
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            // 跳过右边非字母数字
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // 忽略大小写比较
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}


