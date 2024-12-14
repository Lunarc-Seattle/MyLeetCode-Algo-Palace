class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>>ans = new HashMap<>();
            for (String word : strs){
                int [] count = new int[26];
                for ( char c : word.toCharArray()){
                    count[c-'a']++;
                }
                StringBuilder sb = new StringBuilder();
                for( int c : count ){
                    sb.append(c).append("#");
                } 
                String key = sb.toString();
                if(!ans.containsKey(key)){
                    ans.put(key, new ArrayList<>());
                }
                ans.get(key).add(word);
            }
            return new ArrayList<>(ans.values());
        
    }
}
