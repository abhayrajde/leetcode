class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<Integer> ans= new ArrayList<Integer>();
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(0,nums,ans,answer);
        return answer;
    }
    
    public void backtrack(int index,int[] nums,List<Integer> ans,List<List<Integer>> answer) {
        if(index>nums.length) {
            return;
        }
        answer.add(new ArrayList<>(ans));
        int i = index;
        while(i<nums.length) {
            while(i>index && i<nums.length && nums[i]==nums[i-1]) {
                i+=1;
            }
            if(i<nums.length) {
                ans.add(nums[i]);
                backtrack(i+1,nums,ans,answer);
                ans.remove(ans.size()-1);
                i+=1;
            }
        }
    }
}