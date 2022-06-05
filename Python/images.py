str = input()
arr = str.split(" ")
#strFinal = ""
final =""
# print(arr)

for i in range(len(arr)):     
    strFinal= (arr[i].split("."))
    final  = final + strFinal[1] + " "
# print(final)
pngCount = 0 
bmpCount = 0 
jpegCount = 0 

finalFinal = final.split(" ")
for i in range(len(finalFinal)): 
    if( finalFinal[i] =="png" ):
        pngCount = pngCount + 1
    elif (finalFinal[i]=="bmp" ): 
        bmpCount = bmpCount + 1 
    elif( finalFinal[i]== "jpeg"):
        jpegCount = jpegCount + 1  

print(pngCount," " , bmpCount," ",jpegCount )