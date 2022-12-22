# time: O(n)
# space: O(1)
class Solution:
    
    def numberToWords(self, num: int) -> str:
  
        mapping = {
            10**9: "Billion",
            10**6: "Million",
            10**3: "Thousand",
            10**2: "Hundred",
            90: "Ninety",
            80: "Eighty",
            70: "Seventy",
            60: "Sixty",
            50: "Fifty",
            40: "Forty",
            30: "Thirty",
            20: "Twenty",
            19: "Nineteen",
            18: "Eighteen",
            17: "Seventeen",
            16: "Sixteen",
            15: "Fifteen",
            14: "Fourteen",
            13: "Thirteen",
            12: "Twelve",
            11: "Eleven",
            10: "Ten",
            9: "Nine",
            8: "Eight",
            7: "Seven",
            6: "Six",
            5: "Five",
            4: "Four",
            3: "Three",
            2: "Two",
            1: "One",
            0: "Zero"
        }
        
        if num <= 20:
            return mapping[num]
        
        result = ''
        orders = sorted(list(mapping.keys()), reverse=True)
        while num > 0:
            for order in orders:
                if num >= order:
                    count = num // order
                    num -= count * order
                    if order >= 100:
                        to_add = f"{self.numberToWords(count)} {mapping[order]}"
                    else:
                        to_add = str(mapping[order])
                    
                    if result:
                        result += f" {to_add}"
                    else:
                        result = to_add
                    break
        
        return result
