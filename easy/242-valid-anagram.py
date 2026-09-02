class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        for freq in count:
            if freq != 0:
                return False

        return True