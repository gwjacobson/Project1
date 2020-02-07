
import numpy
from operator import itemgetter

#prints state as a vector in normal basis
def PrettyPrintBinary(myState):
    new = sorted(myState, key = itemgetter(1)) #sort the basis vectors
    binary = '( '
    for k, v in new: #adds each vector to the string
        binary += str(k)+' |'+v+'> + '
    binary = binary[:-2] #take off final + sign
    binary += ')'
    print(binary)

#prints state as vector with integer representation for basis vectors. Examples are |00> = |0> and 
#|10> = |2>
def PrettyPrintInteger(myState):
    new = sorted(myState, key = itemgetter(1)) #sort vectors
    integer = '( '
    for k, v in new: #adding each vector to string
        integer += str(k) + ' |'
        binary = int(v, 2) #change vector to binary int
        integer += str(binary)
        integer += '> + '
    integer = integer[:-2] #take off final + sign
    integer += ')'
    print(integer)

#change the state into a vector representation
def StateToVec(myState):
    new = sorted(myState, key = itemgetter(1)) #sort vectors
    myVec = []
    length = len(new[0][1])
    i = 0
    while i <= 2**length:
        for k, v in new:
            if str(i) == v:
                myVec.append(k)
            else:
                myVec.append(0.0)
            i += 1
    return myVec

def VecToState(myState):
    return 0

myState2 = [(numpy.sqrt(0.1)*1.j, '101'), (numpy.sqrt(0.5), '000'), (numpy.sqrt(0.4), '010')]

PrettyPrintBinary(myState2)
PrettyPrintInteger(myState2)

print(StateToVec(myState2))
print(VecToState(StateToVec(myState2)))