class Solution {
    public void rotate(int[] nums, int k) {
            int n = nums.length;
            k = k % n;//防止超过边界

            helper(nums,0,n-1);
            helper(nums,0,k-1);
            helper(nums,k,n-1);

        }
        private void helper( int[]nums, int left, int right){
            while (left<right){
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            }
        
    }
}
