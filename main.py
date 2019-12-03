import random
import sys
import numpy as np
import time
import argrapse

# **********user config**********
DATA = ""
TRAINFILENAME = ""
TESTFILENAME = ""
DIMENSION = 2
NEURON = 2
#**********user config**********


check = 1

def __init__(self,NeuronNum,dimension):
	self.neuronNum = NeuronNum
	self.dimension = dimension
	self.w = np.zeros(shape = (NeuronNum, Dimension))
	self.b = np.zeros(shape = (NeuronNum, 1))
	self.e = np.zeros(shape = (NeuronNum, 1))
	self.countError = 0
	self.init()

def init(self):
	for j in range(0,self.neuronNum):
		for k in range(0,self.dimension):
			self.w[i][j] = random.uniform(-10,10)

	for j in xrange(0,self,neuronNum):
		self.b[i][0] = random.uniform(0,10)
		self.e[i][0] = 0

def hardlim(self,inputdata):
	a = np.zeros(shape = (self.neuronNumm , 1))
	for j in range(0,self.neuronNum):
		if(inputdata[i][0] >= 0):
			a[i][0] = 1
		else
			a[i][0] = 0
	return a

def calError(self,a,t):
	self.e = check*(t-a)

def update_wb(self,inputdata):
	self.w = self.e.dot(inputdata.T) + self.w
	self.b = self.e + self.b

def has_error():
	if np.count_nonzero(self.e) > 0:
		self.countError = self.countError + 1
		return True
	else 
		return False

def getcounterror(self):
	return self.countError

def clearcounterror(self):
	self.countError = 0

def printArray
	print(self.w)
	print(self.b)


def convert2array(fruit):

	if NEURON = 4:
		if fruit == 'w':
			return[[1],[0],[0],[0]]