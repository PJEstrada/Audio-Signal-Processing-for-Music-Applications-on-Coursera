import matplotlib.pyplot as plt
import numpy as np
# import test_sinusoids
import A4Part1, A4Part2

from loadTestCases import load

#fs = 1000
#f = 100
#A0 = 10
#M = 25

testCase = load(2,1)

result = A4Part2.computeSNR(**testCase['input'])
print result
print testCase['output']

#x = A0 * np.cos(2 * np.pi * f * np.arange(M) / fs)
#x = np.array([1, 2, 3, 4, 1, 2, 3])
#(isRealEven, dftbuffer, X) = A3Part3.testRealEven(x)

#print (isRealEven, dftbuffer, X)

