public class findMinInRotatedSortedArr {
    private static int findIt(int[] nums) {
        int res = nums[0];
        int l = 0,
            r = nums.length - 1,
            pre = 1,
            post = 1;
        while (r > -1 && l < nums.length) {
            if (pre == 0) {
                pre = 1;
            }
            if (post == 0) {
                post = 1;
            }
            pre = pre * nums[l];
            l += 1;
            post = post * nums[r];
            r -= 1;
            res = Math.max(res, Math.max(pre, post));
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = { 3, 4, 5, 1, 2 };
        System.out.println(findIt(nums));
    }
}
