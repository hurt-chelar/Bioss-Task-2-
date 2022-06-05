###################
def triangle(a,b,c): 
  if(a+b>c and a+c>b and b+c>a): 
    return True 
  else: 
    return False  
n1 = int(input())# this is no of test cases 

for i in range(n1):
    a,b,r = map(int,input().strip().split(" "))
    count = 0 
    n=int(input())# this is length 
    str = input()
    l=str.split(" ")
    # l=[]
    # for i in range(n):
    #     l.append(int(input())) 
    for i in range(n):
        #print(" ",l[i])
        if(triangle(a,b,int(l[i]))==True) :
            #print("Done")
            count = count + 1 



print(count) 
if (count>int(r)    ): 
    print("Natsu")
else: 
    print("Grey") 
