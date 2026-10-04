class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> sCounter = new HashMap<>();
        Map<Character, Integer> tCounter = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            sCounter.merge((Character)s.charAt(i), 1, Integer::sum);
            tCounter.merge((Character)t.charAt(i), 1, Integer::sum); 
        }

        return sCounter.equals(tCounter);
    }
}
