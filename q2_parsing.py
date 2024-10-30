ppTable = {
    'E': {
        'i':'TQ',
        '+':None,
        '-':None,
        '*':None,
        '/':None,
        '(':'TQ',
        ')':None,
        '$':None
    },
    'Q':{
        'i':None,
        '+':'+TQ',
        '-':'-TQ',
        '*':None,
        '/':None,
        '(':None,
        ')':'lambda',
        '$':'lambda'
    },
    'T':{
        'i':'FR',
        '+':None,
        '-':None,
        '*':None,
        '/':None,
        '(':'FR',
        ')':None,
        '$':None
    },
    'R':{
        'i':None,
        '+':'lambda',
        '-':'lambda',
        '*':'*FR',
        '/':'/FR',
        '(':None,
        ')':'lambda',
        '$':'lambda'
    },
    'F': {
        'i':'i',
        '+':None,
        '-':None,
        '*':None,
        '/':None,
        '(':'(E)',
        ')':None,
        '$':None
    }
}

# List for grammer, stack, and reading
stack = []
grammer = []

grammerInput = input("Enter your grammer: ")
print()

# Easier to place grammer in list
for i in reversed(grammerInput):
    grammer.append(i)

# Variables for looking in table and getting value
pop = None
read = None
entry = None
valid = True

# Stack $ and starting non-terminal
stack.append('$')
stack.append('E')
print("Starting Stack: ", stack)

def findRead(pop, read):
    while pop != read:
        entry = ppTable[pop][read]

        # Pop lambda but break if read found
        while(entry == "lambda"):
            pop = stack.pop()
            if(pop == read):
                break
            entry = ppTable[pop][read]

        # Break if read found or add to stack
        if(pop == read):
            break
        elif(entry == None):
            return False
            break
        else:
            for i in reversed(entry):
                stack.append(i)
        
            pop = stack.pop()

    return True

while(stack):
    pop = stack.pop()
    read = grammer.pop()

    # Loop until 
    valid = findRead(pop = pop, read = read)

    if valid == False:
        break
    print(read, " matched!")
    print("Current Stack: ", stack)

if valid == False:
    print("Rejected!")
if valid == True:
    print("Accepted!")

