#S3C2 Carl Zhao
#CodingBat Answers
#CodingBat Factorial
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
#BunnyEars
def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    return bunnyEars(bunnies-1)+2
#Fibonacci
def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibonacci(x-2)+fibonacci(x-1)
#BunnyEars
def bunnyEars2(bunnies):
    if bunnies == 0:
        return 0
    if bunnies%2 ==0:
        return bunnyEars2(bunnies-1)+3
    if bunnies%2 ==1:
        return bunnyEars2(bunnies-1)+2
#Triangle
def triangle(x):
    if x == 0:
        return 0
    return triangle(x-1)+x
#Sumdigits
def sumDigits(x):
    if x == 0:
        return 0
    return sumDigits(x-x%10)
print(sumDigits(126))
#Count7
def count7(x):
    if x==0:
        return 0
    if x%10==7:
        return count7(int(x/10))+1
    if x%10!=7:
        return count(int(x/10))
#Count8
def count8(x):
    if x==0:
        return == 0
    if x%10==8:
        return count8(int(x/10))+1
            if x/10%10 ==8：
                return count(int(x/10))+2
    if x%10!=8:
        return count(int(x/10))

#PowerN
def PowerN(base,n):
    if n==0:
        return 1
    if n==1:
        return base
    return base*PowerN(base,n-1)

#countX
def countX(content):
    if len(content)==0:
        return 0
    if content[0]==x:
        return countX(content[1:])+1
    return countX(content[1:])

#countHi
def countHi:
    if len(content)<2:
        return 0
    if content[0]=="h" and content[1]=="i":
        return countHi(content[1:])+1
    return countHi(content[1:])

#changeXY
def changeXY(content):
    if len(content)==0:
        return content
    character = content[0]
    if character == "x":
        return "y"+changeXY(content[1:])
    return character+changeXY(content[1:])

#changePi
def changePi(content):
    if len(content)==0:
        return 0
    if content[0]=="p" and content[1]=="i":
        return "3.14"+changePi(content[1:])
    return content[0]+changePi(content[1:])

#noX
def noX(content):
    if len(content)==0:
        return 0
    if content[0]=="x":
        return ""+noX(content[1:])
    return content[0]+noX(content[1:])

#array6
def array6(content,i):
    if content[i]==6:
        return True
    if i+1==len(content):
        return False
    return array6(content,i+1)

#array11
def array11(content,i):
    if i+1==len(content):
        return 0
    if content[i]==11:
        return 1+array11(content,i+1)
    return array11(content,i+1)

#array220
def array220(content,i):
    if i+1==len(content):
        return False
    if content[i]*10==content[i+1]:
        return True
    return array220(content,i+1)

#allStar
def allStar(content):
    if len(content)==1:
        return content

    return content[0]+"*"+allStar(content[1:])

#pairStar
def pairStar(content):
    if len(content)==1:
        return content
    if content[0]==content[1]:
        return content[0]+"*"+pairStar(content[1:])
    return content[0]+pairStar(content[1:])

#endX
def endX(content):
    if len(content)==0:
        return ""
    if content[0]=="x":
        return endX(content[1:])+"x"
    return content[0]+endX(content[1:])

#countPairs
def countPairs(content):
    if len(content)==2:
        return 0
    if content[0]==content[2]:
        return 1+countPairs(content[1:])
    return countPairs(content[1:])

#countABC
def countABC(content):
    if len(content)==2:
        return 0
    if content[0:3]=="abc" or content[0:3]=="aba":
        return 1+countABC(content[1:])
    return countABC(content[1:])

#count11
def count11(content):
    if len(content)<=1:
        return 0
    if content[0:2]=='11':
        return 1+count11(content[2:])
    return count11(content[1:])

#stringClean
def stringClean(content):
    if len(content)==1:
        return content
    if content[0]==content[1]:
        return stringClean(content[1:])
    return content[0]+stringClean(content[1:])

#countHi2
def countHi2(content):
    if len(content)==1:
        return 0
    if content[0]=="x":
        return countHi2(content[2:])
    if content[0:2]=="hi":
        return 1+countHi2(content[1:])
    return countHi2(content[1:])

#parentBit
def parentBit(content):
    if len(content)==0:
        return ""
    if content[0]=="(" and content[-1]==")":
        return content
    if content[0]=="(":
        return parentBit(content[:-1])
#nestParen
def nestParen(content):
    if len(content)<=3 and content[0]=="("and content[-1]==")":
        return True
    if len(content)<=3:
        return False
    if content[0]=="(" and content[-1]==")":
        return nestParen(content[-1:1])
    return False

#strCount
def strCount(content,subc):
    if len(subc)>len(content):
        return 0
    if subc==content[:len(subc)]:
        return 1+strCount(content[len(sub):],subc)
    return strCount(content[1:],subc)

#strCopies
def strCopies(content,subc,n):
    if len(subc)>len(content) and n!=0:
        return False
    if len(subc)>len(content) and n==0:
        return True
    if subc==content[:len(subc)]:
        return strCopies(content[1:],subc,n)
    
#strDist
def strDist(content,subc):
    if len(subc)>len(content):
        return 0
    if subc==content[-len(subc):] and subc==content[:len(subc)]:
        return len(content)
    if subc == content[:len(subc)]:
        return strDist(content[:-1],subc)
    if subc == content[-len(subc):]:
        return strDist(content[1:],subc)
    return strDist(content[1:-1],subc)
    
        

    
            



