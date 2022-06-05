from numpy import array


str = input()
arr = str.split(" ")
# print(arr) 
ar1 = list(arr[0])
ar2 = list(arr[1])
# print(ar1, ar2 )
# print(ord(ar1[0]))

sum1 = 0 
sum2 = 0 
for i in range(len(ar1)): 
    sum1 = ord(ar1[i])+ sum1 
for i in range(len(ar2)): 
    sum2 = ord(ar2[i])+ sum2 

# print(sum1, sum2 )

if( sum1 == sum2 ) : 
    print("True")
else : 
    print("False")