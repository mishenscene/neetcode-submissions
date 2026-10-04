class Solution {
    public boolean hasDuplicate(int[] nums) {
        // convert to arraylist
        List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toCollection(ArrayList::new));
        List<Integer> copy = new ArrayList<>(list);
        for (int i = 0; i < list.size(); i++) {
            Integer num = list.get(i);
            copy.remove(num);
            if (copy.contains(num)) {
                return true;
            }
        }
        return false;
    }
}