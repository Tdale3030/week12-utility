#Tyner Dale
#CSCI 102-section A

def PrintOutput(a):
    print('OUTPUT',a)
def LoadFile(file):
    list=[]
    with open(file,'r') as f:
        for i in f:
            list.append(i)
    return list
def UpdateString(a,b,c):
 
    string=(a.replace(a[c],b))
    print('OUTPUT',string)
 def FindWordCount(list,str):
    a=0
    
    for i in list:
        for word in i.split():
            if word==str:
                a+=1

    return a

def ScoreFinder(list1,list2,str):
    for i in list1:
        if list1[i]==str:
            print('OUTPUT', list1[i],'got a score of',list2[i])
        else:
            print('OUTPUT Player not found')


