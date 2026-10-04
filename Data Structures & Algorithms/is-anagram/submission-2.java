class Solution {
    public boolean isAnagram(String s, String t) {
        // same no. of char and same chars
        // different composite
        // sort the array
        char[] arrS = s.toCharArray();
        char[] arrT = t.toCharArray();
        Arrays.sort(arrS);
        Arrays.sort(arrT);

        return (Arrays.equals(arrS,arrT));
    }
}
