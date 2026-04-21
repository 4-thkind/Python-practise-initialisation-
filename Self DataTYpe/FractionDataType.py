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
