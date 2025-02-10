class Solution(object):
    def romanToInt(self, s):
        roman_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, 
                    "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
        total = 0
        prev_value = 0

        # reverse order
        for char in reversed(s):
            curr_value = roman_dict[char]
            # If smaller value comes before a larger one, subtract it
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value  
        return total
