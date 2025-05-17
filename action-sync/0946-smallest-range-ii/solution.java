import java.util.Arrays;

class Solution {
    public int smallestRangeII(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;

        int result = nums[n - 1] - nums[0]; // 初始范围：全都不动
        for (int i = 0; i < n - 1; i++) {
            int high = Math.max(nums[n - 1] - k, nums[i] + k); // 右边的减 k，左边的加 k
            int low = Math.min(nums[0] + k, nums[i + 1] - k);   // 左边的加 k，右边的减 k
            result = Math.min(result, high - low);
        }

        return result;
    }
}

