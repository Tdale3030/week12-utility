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
