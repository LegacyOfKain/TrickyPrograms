l=list(map(int,input().split()))
def movetoend(arg,item ):
        try:
            # check to see if 'arg' contain any item
            # in the predefined list
            i = arg.index(item)

            # save the value of arg[i]
            j = arg[i]

            # remove "j" from "arg"
            arg.pop(i)

            # append item to end of "arg"
            arg.append(j)

            
        except ValueError:
            pass
        return arg

def printlist(arg ):
    print(*arg, sep = ", ")

def minimumgt(arg, greaterthan  ):
    mini = float('inf')
    #print ("len(arg)-1 = ",len(arg)-1)
    for i in range(len(arg)):
        
        #print("---------------------",greaterthan)
        #print("---------------------i = ",i)
        #print("---------------------arg[i] = ",arg[i])
        if arg[i]>greaterthan : 
            if mini > arg[i]:
                mini = arg[i]
                #print("--------------mini",mini)
    
    return mini

def minimum(arg   ):
    mini = arg[0]
    #print (mini)
    for i in range(len(arg)-1):
        #print(arg[i+1])

            if mini > arg[i+1]:
                mini = arg[i+1]
    
    return mini


def minimummoves(lists):
    pops=0
    if len(lists) == 0 or len(lists) ==1 :
        return 0
    if len(lists) == 2:
        if (lists[0] > lists[1]):
            return 1
        else:
            return 0

    a = minimum(lists)
    b = minimumgt(lists,a)
    c = minimumgt(lists,b)
    for i in range(len(lists)+2):
        #printlist(lists)
        #print(a )
        #print (b )
        #print ( c)
        if  b == float('inf'):
                break
        if lists.index(a)+1 == lists.index(b):
            a = b
            b = minimumgt(lists,a)
            c = minimumgt(lists,b)
        else:
            if lists.index(a) > lists.index(b):
                movetoend(lists,b)
                pops=pops+1
                #print(pops)
            else:
                if lists.index(c) != len(lists)-1:
                    movetoend(lists,c)
                    pops=pops+1
                c = minimumgt(lists,c)
                
                #print(pops)
    return pops
print(minimummoves(l))
