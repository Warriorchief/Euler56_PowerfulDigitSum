"""Euler56_PowerfulDigitSum
A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""
def assembleProds():
    prods=[]
    for a in range(1,100):
        for b in range(1,100):
            prods.append(a**b)
    return prods  
def calcDigSum(x):
    i=0
    out=0
    while i<len(str(x)):
        out+=int(str(x)[i])
        i+=1
    return out
def main():
    prods=assembleProds()
    maxMark=0
    i=0
    while i<len(prods):
        if calcDigSum(prods[i])>maxMark:
            maxMark=calcDigSum(prods[i])
        i+=1
    print(maxMark)
    return maxMark
main() #-->972