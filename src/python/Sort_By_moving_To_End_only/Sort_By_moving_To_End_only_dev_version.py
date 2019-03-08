

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


def minimummoves(arg):
    pops=0
    if len(arg) == 0 or len(arg) ==1 :
        return 0
    if len(arg) == 2:
        if (arg[0] > arg[1]):
            return 1
        else:
            return 0

    a = minimum(arg)
    b = minimumgt(arg,a)
    c = minimumgt(arg,b)
    for i in range(len(arg)+2):
        printlist(arg)
        print(a )
        print (b )
        print ( c)
        if  b == float('inf'):
                break
        if arg.index(a)+1 == arg.index(b):
            a = b
            b = minimumgt(arg,a)
            c = minimumgt(arg,b)
        else:
            
            if arg.index(a) > arg.index(b):
                movetoend(arg,b)
                pops=pops+1
                #print(pops)
            else:
                if arg.index(c) != len(arg)-1:
                    movetoend(arg,c)
                    pops=pops+1
                c = minimumgt(arg,c)
                
                #print(pops)
    return pops


#lists = [ 1,3,2,4,5]
#lists = [ 5,3,4,1,2]
lists = [1,3,5,2,6]
#lists = [5,4,3,2,1]
#lists = [ 1,2,3,4,5]
printlist(lists)
#movetoend(lists,5) 
#printlist(lists)

#print(minimum(lists))
#print(minimumgt(lists,3))

print("-------------------")
print (minimummoves(lists))


