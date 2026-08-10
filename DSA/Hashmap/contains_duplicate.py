class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for count in freq.values():
            if count > 1:
                return True

        return False