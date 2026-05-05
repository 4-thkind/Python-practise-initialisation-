#THERE IS NOT PARTICULARLY PYTHON DATA TYPE FOR FRACTION
#SO I CREATED A CLASS TO REPRESENT IT

class Fraction:
    def __init__(self,n,d):
        self.num= n
        self.den=d
    
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        tempNum=self.num*other.den +self.den*other.num
        tempDen= self.den*other.den
        return "{}/{}".format(tempNum,tempDen)
    
    def __sub__(self,other):
        tempNum=self.num*other.den - self.den*other.num
        tempDen= self.den*other.den
        return "{}/{}".format(tempNum,tempDen)
    
    def __mul__(self,other):
        tempNum=self.num*other.num
        tempDen= self.den*other.den
        return "{}/{}".format(tempNum,tempDen)
    
    def __truediv__(self,other):
        tempNum=self.num*other.den
        tempDen= self.den*other.num
        return "{}/{}".format(tempNum,tempDen)

    #the output is not in simplied form, so adding a new function that returns output in simplified form

    def simplify(self,n,d):
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a
        
        common=gcd(n,d)
        numerator=n//common
        denominator=d//common
        
        return numerator,denominator


frac=Fraction(5,6)
frac2=Fraction(2,3)
print(frac)
print(frac2)

print(frac+frac2)
print(frac-frac2)
print(frac*frac2)
print(frac/frac2)