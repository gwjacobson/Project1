import Dirac
import numpy
import math
import cmath


#multiplying a list of matrices
def tensorMe(matrices, size):
    i = 0
    matrix = numpy.zeros((size, size))
    while i <= len(matrices)-2:
        matrix = numpy.kron(matrices[i], matrices[i+1])
        i += 1
    return matrix

#applying the hadamard gate to a certain qubit(wire) out of all the qubits(wires)
def Hadamard(wire, wires):
    size = 2**wires
    myMatrix = numpy.zeros((size,size)) #the return unitary matrix after operation
    
    coeff = 1/(numpy.sqrt(2))
    h = [[coeff, coeff],
         [coeff, -coeff]]  #hadamard gate
    i = numpy.identity(wires) #identity matrix

    myArray = [] #array of matrices to tensor product
    for j in range(wires): #adding the matrices to the array including the hadamard and indentity
        if j == wire:
            myArray.append(h)
        else:
            myArray.append(i)

    myMatrix = tensorMe(myArray, size) #taking the full tensor product to give the unitary matrix

    return myMatrix

print(Hadamard(1, 2)) 

def Phase(wire, wires, theta):
    size = 2**wires
    myMatrix = numpy.zeros((size,size)) #the return unitary matrix after operation
    
    p = [[1, 0],
         [0, cmath.exp(theta)]] #phase gate
    i = numpy.identity(wires) #identity matrix

    myArray = [] #array of matrices to tensor product
    for j in range(wires): #adding the matrices to the array including the hadamard and indentity
        if j == wire:
            myArray.append(p)
        else:
            myArray.append(i)

    myMatrix = tensorMe(myArray, size) #taking the full tensor product to give the unitary matrix

    return myMatrix

print(Phase(1,2,3.14))

def CNOT(controlWire, otherWire, wires):
    size = 2**wires
    myMatrix = numpy.zeros((size,size))
    c = numpy.zeros((4,4)) #CNOT gate
    i = numpy.identity(wires) #identity matrix

    myArray = []

    if(controlWire < otherWire): #right side up CNOT
        c = [[1,0,0,0],
             [0,1,0,0],
             [0,0,0,1],
             [0,0,1,0]]

        for j in range(wires):
            if j == controlWire:
                myArray.append(c)

            elif j == otherWire:
                continue

            else:
                myArray.append(i)

    else:                       #upside down CNOT
        c = [[1,0,0,0],
             [0,0,0,1],
             [0,0,1,0],
             [0,1,0,0]]

        for j in range(wires):
            if j == otherWire:
                myArray.append(c)

            elif j == controlWire:
                continue

            else:
                myArray.append(i)

    myMatrix = tensorMe(myArray, size) #making the unitary matrix
    return myMatrix

print(CNOT(2,3,4))

#given function for parsing a circuit description
def ReadInput(fileName):
        myInput_lines=open(fileName).readlines()
        myInput=[]
        numberOfWires=int(myInput_lines[0])
        for line in myInput_lines[1:]:
            myInput.append(line.split())
        return (numberOfWires,myInput)

#Creates the Unitary matrix of an entire circuit description
def unitary(fileName):
    number, myInput = ReadInput(fileName) #get the circuit description
    size = 2**number
    myMatrix = numpy.identity(size) #initializing unitary matrix
    
    for gate, wire in myInput:
        if gate == "H": #apply hadamard
            numpy.kron(myMatrix, Hadamard(wire, number))

        elif gate == "P": #apply phase
            numpy.kron(myMatrix, Phase(wire[0], number, wire[1]))

        elif gate == "CNOT": #apply cnot
            numpy.kron(myMatrix, CNOT(wire[0], wire[1], number))

        elif gate == "MEASURE": #to measure the state the system is in
            continue

        else:
            continue

    return myMatrix