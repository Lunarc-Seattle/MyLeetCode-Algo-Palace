class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length-1; i >=0; i--){
            if (digits[i] < 9){
                digits[i] ++; 
                return digits;
            }
            digits[i]= 0;}

        
        // 如果我们走完了整个循环，说明原数组全是 9，比如 999 → 1000
        int [] result = new int[digits.length+1];
        result[0] = 1;
        return result;
    }
}
