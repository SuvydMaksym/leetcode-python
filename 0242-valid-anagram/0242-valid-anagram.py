class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_counter = {}
        t_counter = {}
        for let in s:
            s_counter[let] = s_counter.get(let,0) + 1
        for let in t:
            t_counter[let] = t_counter.get(let, 0) + 1 
        if s_counter == t_counter:
            return True
        return False