class Solution(object):
    def brute(self,string1,string2):
        if len(string1) != len(string2):
            return False
        s1 = sorted(string1)
        s2 = sorted(string2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        else:
            return True
    
    def optimize(self,string1,string2):
        if len(string1) != len(string2):
            return False
        hashMap = {}
        for char in string1:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
        for char in string2:
            if char in hashMap:
                hashMap[char] -= 1
        
        for key in hashMap:
            if hashMap[key] != 0:
                return False
        else:
            return True


    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return self.brute(s,t)
        return self.optimize(s,t)