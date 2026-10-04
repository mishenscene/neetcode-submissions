# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # store a dict of k:v, index:anagram
#         uniq_dict={}
#         for index, elem in enumerate(strs):
#             char_count=''.join(sorted(elem))
#             if not uniq_dict:
#                 uniq_dict[char_count]=[elem]
#             if char_count not in uniq_dict.keys():
#                 uniq_dict[char_count]=[elem]
#             if char_count in uniq_dict.keys():
#                 old_values = uniq_dict.get(char_count)
#                 print(old_values)
#                 if old_values != elem:
#                     old_values.append(elem)
#                     uniq_dict[char_count]=old_values
#         # create the new lists
#         print(uniq_dict)
#         output=[]
#         for key, value in uniq_dict.items():
#             print('>>>blank?',key,value)
#             output.append(list(value))
#         return output

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to map sorted character count to list of anagrams
        uniq_dict = {}
        
        for elem in strs:
            # Create a key by sorting the characters in the string
            char_count = ''.join(sorted(elem))
            
            # If the key is not in the dictionary, initialize it with an empty list
            if char_count not in uniq_dict:
                uniq_dict[char_count] = []
            
            # Append the element to the list of anagrams for this key
            uniq_dict[char_count].append(elem)
        
        # Convert the dictionary values to a list of lists
        output = list(uniq_dict.values())
        
        return output
      