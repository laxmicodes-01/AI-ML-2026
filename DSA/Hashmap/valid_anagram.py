class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        f={}
        q={}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for j in t:
            if j in q:
                q[j]+=1
            else:
                q[j]=1
        if f==q:
            return True
        else:
            return False