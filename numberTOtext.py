def numToText(o):
    s = "$ One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
    b = "Twenty Thirty Fourty Fifty Sixty Seventy Eighty Ninety".split()
    
    def Go(n):
        if n < 20:
            return s[n]
        if n < 100:
            return b[n//100] + " " + Go(n%10)
        if n < 1000:
            return s[n//1000 + 1] + " Houndred " + Go(n%100)          
        for p, w in enumerate((' Thousand ', ' Million ', ' Billion '), 1):
            if n < 1000 ** (p + 1):
                return Go(n // 1000 ** p) + w + Go(n % 1000 ** p)
    if o == 0:return "zero"
    elif o < 0:return "Minus "+''.join(Go(-o))
    else:return ''.join(Go(o))

print(numToText(-23223))