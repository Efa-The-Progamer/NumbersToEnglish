def numToText(inputnum):
    firsts = "$ One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
    Seconeds = "Twenty Thirty Fourty Fifty Sixty Seventy Eighty Ninety".split()
    
    def Go(num):
        if num < 20:
            return firsts[num]
        if num < 100:
            return Seconeds[num // 10] + " " + Go(num % 10)
        if num < 1000:
            return firsts[num // 100 + 1] + " Houndred " + Go(num % 100)          
        for p, w in enumerate((' Thousand ', ' Million ', ' Billion '), 1):
            if num < 1000 ** (p + 1):
                return Go(num // 1000 ** p) + w + Go(num % 1000 ** p)
    if inputnum == 0:
        return "zero"
    elif inputnum < 0:
        return "Minus "+''.join(Go(-inputnum))
    else:
        return ''.join(Go(inputnum))

print(numToText(-23223))
# Minus Fourty Three Thousand Three Houndred Fourty Three
