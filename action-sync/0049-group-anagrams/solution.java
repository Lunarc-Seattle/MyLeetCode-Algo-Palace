class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> ans = new HashMap<>();
            for(String s: strs){
                int count[] = new int[26];
                for (char c : s.toCharArray() ){
                    count[c - 'a']++;
                }
                StringBuilder sb = new StringBuilder();
                for (int e : count){
                    sb.append(e).append("#");
                }
                String key = sb.toString();
                if(!ans.containsKey(key)){
                    ans.put(key,new ArrayList<>());
                }
                ans.get(key).add(s);


            }
            return new ArrayList<>(ans.values());
        
    }
}
