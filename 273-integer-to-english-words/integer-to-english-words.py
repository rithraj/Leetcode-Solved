class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
                "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        thousands = ["", "Thousand", "Million", "Billion"]

        # Helper to convert numbers less than 1000 to words
        def threeDigitToWords(n):
            res = ""
            if n >= 100:
                res += ones[n // 100] + " Hundred "
                n %= 100
            if n >= 20:
                res += tens[n // 10] + " "
                n %= 10
            if n > 0:
                res += ones[n] + " "
            return res.strip()

        result = ""
        i = 0  # Index for thousands
        
        while num > 0:
            if num % 1000 != 0:
                result = threeDigitToWords(num % 1000) + " " + thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()
