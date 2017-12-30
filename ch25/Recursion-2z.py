#S3C2 Carl Zhao
#CodingBat Recursion2

#groupSum
def groupSum(start,content,end):
    if end==0:
        return True
    if start==len(content):
        return False
    return groupSum(start+1,content,end)

#groupSum6
def groupSum6(start,content,end):
    if start==len(content) and end==0:
        return True
    if start==len(content) and end!=0:
        return False
    if content[start]==6:
        return groupSum6(start+1,content,end-content[start])
    return groupSum6(start+1,content,end-content[start])

#groupNoAdj
def groupNoAdj(start,content,end):
    if end==0:
        return True
    if start>=len(content):
        return False
    return groupNoAdj(start+1,content,end)

#groupSum5
def groupSum5(start,content,end):
    if start+1 > len(content):
	    return end == 0 

    if content[start]%5 == 0 and content[start+1] == 1:
	    return groupSum5(start+2,content,end-content[start])
    elif content[start]%5 == 0:
	    return groupSum5(start+1,content,end-content[start])
    return groupSum5(start+1,content,end) or groupSum5(start+1,content,end-content[start])

#splitArray
def splitArray(content,start,a,b):
    if start==len(content):
        return a==b
    return splitArray(content,start+1,a+content[start],b) or splitArray(content,start+1,a+content[start])

#splitOdd10
def splitOdd10(content,start=0,a=0,b=0):
    if start==len(content):
        return (a%10==0 and b%2==1)
    return splitOdd10(content,start+1,a+content[start],b) or splitOdd10(content,start+1,b,a+content[start])

#split53
def split53(nums,start,l,r):
    start=0
    l=0
    r=0
    if start==len(nums):
        return l==r
    if nums[start]%3==0:
        return split53(nums,start+1,l+3,r)
    if nums[start]%5==0:
        return split53(nums,start+1,l,r+5)
    return split53(nums,start+1,l+nums[start],r)
    










