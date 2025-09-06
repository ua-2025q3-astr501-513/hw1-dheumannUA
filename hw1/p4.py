#!/usr/bin/env python3
#
# Please look for "TODO" in the comments, which indicate where you
# need to write your code.
#
# Part 4: Solve the Coupled Simple Harmonic Oscillator Problem (1 point)
#
# * Objective:
#   Take the coupled harmonic oscillator problem we solved in class
#   and rewrite it using a well-structured Python class.
# * Details:
#   The description of the problem and the solution template can be
#   found in `hw1/p4.py`.
#
# From lecture `02w`, we solve systems of coupled harmonic oscillators
# semi-analytically by numerically solving eigenvalue problems.
# However, the code structure was not very clean, making the code hard
# to reuse.
# Although numerical analysis in general does not require
# object-oriented programming, it is sometime useful to package
# stateful caluation into classes.
# For this assignment, we will provide a template class.
# Your responsibility to implement the methods in the class.


import numpy as np


class CoupledOscillators:
    """A class to model a system of coupled harmonic oscillators.

    Attributes:
        Omega (np.ndarray): array of angular frequencies of the normal modes.
        V     (np.ndarray): matrix of eigenvectors representing normal modes.
        M0    (np.ndarray): initial amplitudes of the normal modes.

    """

    def __init__(self, X0=[-0.5, 0, 0.5], m=1.0, k=1.0):
        """Initialize the coupled harmonic oscillator system.

        Args:
            X0 (list or np.ndarray): initial displacements of the oscillators.
            m  (float):              mass of each oscillator (assumed identical for all oscillators).
            k  (float):              spring constant (assumed identical for all springs).

        """
        print("In CoupledOscillators __init__ routine")
        print(f"X0 = {X0}")
        # TODO: Construct the stiffness matrix K
        K=np.zeros((len(X0),len(X0)))
        for i in range(len(X0)):
            K[i,i]=2*k/m
        for i in range(len(X0)-1):
            K[i,i+1]=-k/m
            K[i+1,i]=-k/m
        print(f"K = {K}, K shape={K.shape}")
        # TODO: Solve the eigenvalue problem for K to find normal modes
        EW, EV = np.linalg.eig(K)
        print(f"Eigenvalues = {EW}")
        # TODO: Store angular frequencies and eigenvectors
        self.Omega = np.sqrt(EW)
        print(f"angular frequencies = {self.Omega}")
        self.V = EV
        print("self.V shape=",self.V.shape)
        print(f"Eigenvectors = {self.V}")
        # TODO: Compute initial modal amplitudes M0 (normal mode decomposition)
        self.M0 = np.dot(self.V.T, X0) # Self.V.T is the transpose of NxN matrix V, in each column of Self.V is an eigenvector, after transpose, in each row of Self.V.T is an eigenvector, the scalar product of each row of Self.V.T and X0 is the amplitude of each eigenvector in the initial displacement vector X0, the amplitude does not change with time
        print(f"Initial modal amplitudes = {self.M0}")


    def __call__(self, t):
        """Calculate the displacements of the oscillators at time t.

        Args:
            t (float): time at which to compute the displacements.

        Returns:
            np.ndarray: displacements of the oscillators at time t.

        """
        # TODO: Reconstruct the displacements from normal modes
        self.M=self.M0*np.cos(self.Omega*t) # M is the modal amplitude at time t
        X=np.dot(self.V, self.M) # X is the displacement at time t
        print(f"t={t}, displacements={X}")
        return X

if __name__ == "__main__":

    # Initialize the coupled oscillator system with default parameters
    co = CoupledOscillators()

    # Print displacements of the oscillators at each time step
    print("Time(s)  Displacements")
    print("----------------------")
    for t in np.linspace(0, 10, num=101):
        X = co(t)             # compute displacements at time t
        print(f"{t:.2f}", X)  # print values for reference
