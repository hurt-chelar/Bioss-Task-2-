



text = input()
### splitting into 2 parts 
lp = text.split("@")
localPart=lp[0]
# print(localPart)
dp= lp[1].split(".")
domainPart= dp[0]
# print(domainPart)
extension= dp[1]
# print(extension)
# print(localPart," ",domainPart, " ", extension)

def length():
    if(len(localPart)<64):
        return 1
    else :
        return 0 

localPartList= list(localPart) # the list of domain 
# print(localPartList)

def localVerification():
    m = 1 
    for i in range(len(localPartList)):
        x = ord(localPartList[i])
        if(  (x>=65 and x<=90)or (x>=97 and x<=122)or(x>=48 and x<=57)or (x>=33 and x<=47)):
            m = m and 1
        else :
            m = 0
            break 
    return m 





def localSpecialVerificationException():
    m = 1 
    for i in range(len(localPartList)): 
        x = ord(localPartList[i])
        if((x==34) or (x==40) or (x==41) or (x==44)): 
            m = 0 and m 
            break 
    return m 

def dotVerification():
    m = 1
    x=localPartList
    if(x[0]=="." or x[len(localPartList)-1]=="." ):
        m = 0 
    return m 


    
localFinal = localSpecialVerificationException() and localVerification() and length() and dotVerification()

### local part verification is done 

domainPartList = list(domainPart)
def domainVerification():
    m = 1 
    for i in range(len(domainPartList)):
        x = ord(domainPartList[i])
        if(  (x>=65 and x<=90)or (x>=97 and x<=122)or x==45	or (x>=48 and x<=57) ):
            m = m and 1
        else :
            m = 0
            break 
    return m 


def entireNumeric():
    count = 0  
    for i in range(len(domainPartList)): 
        x = ord(domainPartList[i]) 
        if(x>=48 and x<=57): 
            count = count + 1 
    if(count == len(domainPartList)):
        m = 0 
    else : 
        m = 1
    return m 




def hyphenVerfication(): 
    m = 1 
    n = 0 
    x = domainPartList
    
    for i in range(1,len(domainPartList)-2): 
        if(x[i]=="-"):
            n = n or 1  
    if(x[0]=='-' or x[len(domainPartList)-1]=='-'): 
        m = 1 
    if(m==1 and n==0) : 
        return 1 
    else : 
        return 0 






domainFinal = domainVerification() and entireNumeric() and hyphenVerfication() ##
## this is the final domanin verification 

extensionList = list(extension) 
# print(extensionList)

def maxLenExtension(): 
    if(len(extensionList)>3) : 
        return 0 
    else : 
        return 1 


def extensionVerfication(): 
    n = 1 
    for i in range(len(extensionList)): 
        x = ord(extensionList[i])
        if( (x>=32 and x<=47)  or (x>= 58 and x<= 64) or (x>=91 and x<= 96) or (x>=123 and x<= 126 ) ) : 
            n = n and 0 
    return n


extensionFinal = maxLenExtension() and extensionVerfication() 


finalAnswer = localFinal and domainFinal and extensionFinal 

if(finalAnswer==True): 
    print("True")
else:
    print('False')


