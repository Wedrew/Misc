import numpy

def NN(m1, m2, w1, w2, b):
	z = m1 * w1 + m2 * w2 + b
	return sigmoid(z)

def sigmoid(x):
	return 1/(1 + numpy.exp(-x))

def error(pred, target):
	return (pred-target)**2

def num_slope(b):
	h = 0.0001
	return (cost(b+h) - cost(b))/h

def slope(b):
	return 2*(b-4)

w1 = numpy.random.randn()
w2 = numpy.random.randn()
b = numpy.random.randn()