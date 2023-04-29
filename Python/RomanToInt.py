class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, total = 0, 0
        for i in s:
            current = roman[i]
            total += current
            # need to subtract
            if current > prev:
                total -= 2 * prev
            prev = current
        return total