
import numpy
import math
from operator import itemgetter

#prints state as a vector in normal basis
def PrettyPrintBinary(myState):
    new = sorted(myState, key = itemgetter(1)) #sort the basis vectors
    binary = '( '
    for coefficient, basis in new: #adds each vector to the string
        binary += str(coefficient)+' |'+basis+'> + '
    binary = binary[:-2] #take off final + sign
    binary += ')'
    print(binary)

#prints state as vector with integer representation for basis vectors. Examples are |00> = |0> and 
#|10> = |2>
def PrettyPrintInteger(myState):
    new = sorted(myState, key = itemgetter(1)) #sort vectors
    integer = '( '
    for coefficient, basis in new: #adding each vector to string
        integer += str(coefficient) + ' |'
        binary = int(basis, 2) #change vector to binary int
        integer += str(binary)
        integer += '> + '
    integer = integer[:-2] #take off final + sign
    integer += ')'
    print(integer)

#change the state into a vector representation
def StateToVec(myState):
    length = len(myState[0][1]) #length of vector array
    myVec = [0.0]*(2**length)

    for coefficient, basis in myState: #add given states into vector array
        myVec[int(basis, 2)] = coefficient

    return myVec

def VecToState(myState):
    mySt = []
    for coefficient in myState:
        if coefficient != 0.0:
            binary = str(bin(myState.index(coefficient)))
            binary  = binary[2:]
            bits = math.log(len(myState), 2)
            mySt.append((coefficient, binary.zfill(int(bits))))
    return mySt

myState2 = [(numpy.sqrt(0.1)*1.j, '101'), (numpy.sqrt(0.5), '000'), (numpy.sqrt(0.4), '010')]

PrettyPrintBinary(myState2)
PrettyPrintInteger(myState2)

print(StateToVec(myState2))
print(VecToState(StateToVec(myState2)))