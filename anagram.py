#first solution

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        else:
            l="abcdefghijklmnopqrstuvwxyz"
            for i in l:
                if s.count(i)!=t.count(i):
                    return False
            return True


#second solution


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=''.join(sorted(s))
        b=''.join(sorted(t))
        if a==b:
            return True
        else:
            return False
