from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        counter = Counter(s)
        for index,char in enumerate(s):
            if counter[char] == 1:
                return index
        return -1
        