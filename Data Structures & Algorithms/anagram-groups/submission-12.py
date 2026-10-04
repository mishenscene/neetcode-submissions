class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store a dict of k:v, index:anagram
        uniq_dict={}
        for index, elem in enumerate(strs):
            char_count=''.join(sorted(elem))
            # create entries
            if char_count not in uniq_dict.keys():
                uniq_dict[char_count]=[]
            # add entries
            if char_count in uniq_dict.keys():
                uniq_dict[char_count].append(elem)
        output = list(uniq_dict.values())
        return output