def numToText(o):

    s = "$ One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
    b = "Twenty Thirty Fourty Fifty Sixty Seventy Eighty Ninety".split()        
    
    Dic = { "." : "Point" , "%" : "Percent" , "$" : "Dollars" , "₤" : "Pounds" , "€" : "Euros" , "m" : "Meters" , "kh" : "Kilometers Per Hour" , "ft" : "Feet" , "L" : "Liters" , "tbsp" : "tablespoons" , "tsb" : "teaspoon"}
    
    val_list = list(Dic.values())
    key_list = list(Dic.keys())   

    def finder(m):
        Point = [] 
        for p, w in enumerate(('.', '%', '$' , '₤' , '€' , 'm' , 'kh' , 'ft' , 'L' , 'tsb' , 'tbsp'), 0):
            if m.find(w) > -1:
                Point.append(Dic.get(w))
        return Point

    def PointGo(num):
        position=False
        if num.find('.') != -1 : position=True  

        Point = finder(num)    

        pointer_1 = key_list[val_list.index(Point[0])]
        p_1 = num.find(pointer_1)

        PointIndex = num.split(pointer_1)
        
        if len(Point) > 1 and position == True:
            pointer_2 = key_list[val_list.index(Point[1])]
            p_2 = num.find(pointer_2)
            if p_1 < p_2:
                o_1 = PointIndex[0]
                o_2 = PointIndex[1].split(pointer_2)[0]   
            else:
                o_1 = PointIndex[1]
                o_2 = PointIndex[0].split(pointer_2)[1]  
                o_1,o_2=o_2,o_1 

        if len(Point) == 1:
            if position == True:
                i,G,d=len(d),'',PointIndex[1]
                while(i>0):
                    i -= 1
                    f = (int(d) - int(d) % 10**i) // 10**i
                    d = int(d) % 10**i
                    G += str(Go(f)) + ' '
                return " {} {} {} ".format(Go(int(PointIndex[0])),Point[0],G)
            else:
                if p_1 ==0:
                    return " {} {}".format(Go(int(PointIndex[1])),Point[0])
                else:
                    return " {} {}".format(Go(int(PointIndex[0])),Point[0])           
        else:
            if pointer_2 == '$' or pointer_2 == '₤' or pointer_2 == '€':
                return " {} {} and {}".format(Go(int(o_1)),Point[1],Go(int(o_2)))
            else:
                i,G=len(o_2),''
                while(i>0):
                    i -= 1
                    f = (int(o_2) - int(o_2) % 10**i) // 10**i
                    o_2 = int(o_2) % 10**i
                    G += str(Go(f)) + ' '
                return " {} {} {} {}".format(Go(int(o_1)),Point[0],G,Point[1])

    def Go(n):
        if n == 0:
            return ''
        if n < 20:
            return s[n]
        if n < 100:
            return b[n//10 - 2] + ' ' + Go(n%10)
        if n < 1000:
            return s[n//100] + ' Houndred ' + Go(n%100)          
        for p, w in enumerate((' Thousand ', ' Million ', ' Billion ' , ' Trillion '), 1):
            if n < 1000 ** (p + 1):
                return Go(n // 1000 ** p) + w + Go(n % 1000 ** p)

    if type(o) is not str:
        if o == 0:
            return "zero" 
        elif o < 0:
            p=-o
            return "Minus "+''.join(Go(p))
        else:
            return ''.join(Go(o))        
    else:
        if o.find("km/h") > -1 : o=o.replace("km/h","kh",1)
        z = o.find('-')
        if z > -1:
            return "Minus"+''.join(PointGo(o[1:]))
        else:
            return ''.join(PointGo(o))

print(numToText("$45123456"))
print(numToText("45123456₤"))
print(numToText("45.123456€"))
print(numToText("-45123456%"))
print(numToText("-45.123456%"))
print(numToText("45.12m"))
print(numToText("45.123km/h"))
print(numToText("45ft"))
print(numToText("45.123L"))
print(numToText("45.1234tsb"))
print(numToText("45.123456tbsp"))
print(numToText(321457654321232))
