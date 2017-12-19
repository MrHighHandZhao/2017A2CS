 
 x = [2,9,13,37,43,57,88,92,99] 
 SearchedItem = 37 
 Found = False 
 SearchFailed = False 
 
 
 a = 0 
 b = len(x) 
 
 
 while Found == False and SearchFailed == False: 
     c=int((a+b)/2) 
     print(l,b,c) 
     if x[c]==SearchedItem: 
         Found=True 
     else: 
         if l>b: SearchFailed=True 
         else: 
             if x[c]>SearchedItem: 
                 b=b-1 
             else: 
                 a=c+1 
 if Found==True: 
     print(c,x[c]) 
 else: 
     print(-1) 
