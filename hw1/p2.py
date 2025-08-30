# Part 2: Integer Negation and Subtraction Using NAND Gates (1 point)
# Objective:   Implement a function that performs integer negation using only NAND gates and use it to implement subtraction

#!/usr/bin/env python3
#
# Please look for "TODO" in the comments, which indicate where you
# need to write your code.
#
# Part 2: Integer Negation and Subtraction Using NAND Gates (1 point)
#
# * Objective:
#   Implement a function that performs integer negation using only NAND
#   gates and use it to implement subtraction.
# * Details:
#   The description of the problem and the solution template can be
#   found in `hw1/p2.py`.
#
# From lecture `01w`, we learned that NAND is a universal gate, that
# any binary operations can be built by using only NAND gates.
# Following the lecture notes, we define the "NAND gate" as

def NAND(a, b):
    return 1 - (a & b)  # NOT (a AND b)

# Following the notes again, we define also other basic operations:

def NOT(a):
    return NAND(a, a)

def AND(a, b):
    return NOT(NAND(a, b))

def OR(a, b):
    return NAND(NOT(a), NOT(b))

def XOR(a, b):
    return NAND(NAND(a, NAND(a, b)), NAND(b, NAND(a, b)))

# We also implemented the half, full, and multi-bit adders:

def half_adder(A, B):
    S = XOR(A, B)  # Sum using XOR
    C = AND(A, B)  # Carry using AND
    return S, C

def full_adder(A, B, Cin):
    s, c = half_adder(A,   B)
    S, C = half_adder(Cin, s)
    Cout = OR(c, C)
    return S, Cout

def multibit_adder(A, B):
    assert(len(A) == len(B))

    n = len(A)
    c = 0
    S = []
    for i in range(n):
        s, c = full_adder(A[i], B[i], c)
        S.append(s)
    S.append(c)  # add the final carry
    return S

# Now, getting into the assignment, we would like to first implement a
# negative function.
#
# Please keep the following function prototype, otherwise the
# auto-tester would fail, and you will not obtain point for this
# assigment.

def multibit_negative(A):
#        """Multi-bit integer negative operator
#   This function take the binary number A and return negative A using
#    two's complement.
#    In other words, if the input
#        A = 3 = 0b011,
#    then the output is
#        -A = -3 = 0b101.

#    Args:
#        A: input number in binary represented as a python list, with
#           the least significant digit be the first.
#           That is, the binary 0b011 should be given by [1,1,0].

#    Returns:
#        Negative A using two's complement represented as a python
#        list, with the least significant digit be the first.

    
#   TODO: implement the function here
    print("Computing -B")

    notA, negA = [0] * len(A), [0] * len(A) # need to define Abar before using it, Abar = list filled with zeros
    for i in range(len(A)):
        notA[i] = NOT(A[i])
    One = [1] + [0] * (len(A) - 1) # One = 1 followed by zeros, e.g., for 8 bits, One = [1,0,0,0,0,0,0,0] for 8 bits
    negA = multibit_adder(notA, One) # multibit_adder already starts with LSB left, no need to reverse input A
    negA.pop()  # Remove the last = rightmost element of a list
    # print(f"negA after ={negA}")
    return negA

# We are now ready to implement subtraction using multibit_adder() and
# multibit_negative().

def multibit_subtractor(A, B):
    """Multi-bit integer subtraction operator

    This function take the binary numbers A and B, and return A - B.
    Be careful on how the carrying bit is handled in multibit_adder().
    Make sure that when A == B, the result A - B should be zero.

    Args:
        A, B: input number in binary represented as a python list,
           with the least significant digit be the first.
           That is, the binary 0b011 should be given by [1,1,0].

    Returns:
        A - B represented as a python list, with the least significant
        digit be the first.

    """
    # TODO: implement the function here
    print("Computing A-B")
    multibit_sub = multibit_adder(A, multibit_negative(B))
    multibit_sub.pop()  # Remove the last = rightmost element of a list
    return multibit_sub

NUMBEROFBITS = 8
nA, nB= 3, 5

A = [int(a) for a in format(nA, f'0{NUMBEROFBITS}b')]          # generates list for Ap with MSB left, LSB right
A.reverse() 
B = [int(a) for a in format(nB, f'0{NUMBEROFBITS}b')]          # generates list for Ap with MSB left, LSB right
B.reverse()                         # order reversed, now LSB left, MSB right as expected by multibit_adder (used in multibit_negative)
print(f"A={A}, B={B}, multibit_negative(B)={multibit_negative(B)}")
print(f"multibit_subtractor(A, B)={multibit_subtractor(A, B)}") 