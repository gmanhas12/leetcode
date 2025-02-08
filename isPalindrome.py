class Solution(object):
    def isPalindrome(self, x):
        length = len(str(x))
        y = str(x)

        for i in range(length):
            if y[i] == y[length - 1 - i]:
                i += 1
            else:
                return False

        return True
