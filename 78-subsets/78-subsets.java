class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        backtrack(0,nums,ans,answer);
        return answer;
    }
    
    public void backtrack(int index,int[] nums,List<Integer> ans,List<List<Integer>> answer) {
        if(index>nums.length) {
            return;
        }
        answer.add(new ArrayList<>(ans));
        for(int i=index;i<nums.length;i++) {
            ans.add(nums[i]);
            backtrack(i+1,nums,ans,answer);
            ans.remove(ans.size()-1);
        }
        return;
    }
}