from collections import deque
key = int(input("Key"))
type= int(input("Type"))
sample = input("Sample")
sampleList = list(sample)

smallLetters="abcdefghijklmnopqrstuvwxyz"
captialLetters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# print(list(smallLetters))
s1Dup = deque(list(smallLetters))

s2Dup=deque(list(captialLetters))

s2 = list("")


def position(x,s1Dup): 
        for i in range(26): 
            if(x==s1Dup[i]): 
                return  i 
        
        return -1 

# def changeSmall():
#     for i in range(len(sampleList)) : 
#         x = sampleList[i]
#         ctrl = 0 
#         j = 0 
#         if(x==" "): 
#             s2.append(" ")
#         else:
#             pos = position(x,s1Dup)
#             if(pos!=-1):
#                 # print(pos)
#                 s1Dup.rotate(-pos)
#                 s2.append(s1Dup[0+key])
#             else:
#                 s2.append(x)
            

        
#         # print(s1Dup)

#     # print(s2)


def changeSmall():
    for i in range(len(sampleList)) : 
        x = sampleList[i]
        ctrl = 0 
        j = 0 
        if(x==" "): 
            s2.append(" ")
        else:
            if(ord(x)>=97):
                pos = position(x,s1Dup)
                if(pos!=-1):
                    # print(pos)
                    s1Dup.rotate(-pos)
                    s2.append(s1Dup[0+key])
                else:
                    s2.append(x)
            else :
                pos = position(x,s2Dup)
                if(pos!=-1):
                    # print(pos)
                    s2Dup.rotate(-pos)
                    s2.append(s2Dup[0+key])
                else:
                    s2.append(x)

            

        
        # print(s1Dup)

    print("".join(s2))





def DecriptchangeSmall():
    for i in range(len(sampleList)) : 
        x = sampleList[i]
        ctrl = 0 
        j = 0 
        if(x==" "): 
            s2.append(" ")
        else:
            if(ord(x)>=97):
                pos = position(x,s1Dup)
                if(pos!=-1):
                    # print(pos)
                    s1Dup.rotate(-pos)
                    s2.append(s1Dup[0-key])
                else:
                    s2.append(x)
            else :
                pos = position(x,s2Dup)
                if(pos!=-1):
                    # print(pos)
                    s2Dup.rotate(-pos)
                    s2.append(s2Dup[0-key])
                else:
                    s2.append(x)

            

        
        # print(s1Dup)

    print("".join(s2))



if(type==1):
    DecriptchangeSmall()
else : 
    changeSmall()