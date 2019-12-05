import random
import sys
import numpy as np
import time
import argparse


# **********user config**********
DATA = ""
TRAINFILENAME = "DATA/"
TESTFILENAME = "DATA/"
DIMENSION = 2
NEURON = 2
#**********user config**********

p = []
epoch = 0
check = 1
output = None


class Neuron():
	
	def __init__(self,NeuronNum,dimension):
		self.neuronNum = NeuronNum
		self.dimension = dimension
		self.w = np.zeros(shape = (NeuronNum, dimension))
		self.b = np.zeros(shape = (NeuronNum, 1))
		self.e = np.zeros(shape = (NeuronNum, 1))
		self.countError = 0
		self.init()
#------------------------------------------------------
	def init(self):
		for j in range(0, self.neuronNum):
			for k in range(0,self.dimension):
				self.w[j][k] = random.uniform(-10,10)

		for j in range(0, self.neuronNum):
				self.b[j][0] = random.uniform(0,10)
				self.e[j][0] = 0
#------------------------------------------------------
	def hardlim(self,inputdata):
		a = np.zeros(shape = (self.neuronNum , 1))
		for j in range(0,self.neuronNum):
			if(inputdata[j][0] >= 0):
				a[j][0] = 1
			else:
				a[j][0] = 0
		return a
#------------------------------------------------------
	def calError(self,a,t):
		self.e = check*(t-a)
#--------------------------------------------------------
	def update_wb(self,inputdata):
		self.w = self.e.dot(inputdata.T) + self.w
		self.b = self.e + self.b
#----------------------------------------------------------
	def has_error(self):
		if np.count_nonzero(self.e) > 0:
			self.countError = self.countError + 1
			return True
		else:
			return False
#----------------------------------------------------------
	def getcounterror(self):
		return self.countError
#-----------------------------------------------------------
	def clearcounterror(self):
		self.countError = 0
#------------------------------------------------------------
	def printArray(self):
		print(self.w)
		print(self.b)
#----------------------------------------------------------
#----------------------------------------------------------


def convert2array(fruit):

	if NEURON == 4:
		if fruit == 'W':
			return[[1],[0],[0],[0]]
		if fruit == 'B':
			return[[0],[1],[0],[0]]
		if fruit == 'P':
			return[[0],[0],[1],[0]]
		if fruit == 'O':
			return[[0],[0],[0],[1]]
	else:
		if DATA == "Data1":
			if fruit == 'W':
				return[[0],[0]]
			if fruit == 'B':
				return[[0],[1]]
			if fruit == 'P':
				return[[1],[0]]
			if fruit == 'O':
				return[[1],[1]]

		if DATA == "Data2":
			if fruit == 'W':
				return[[1],[1]]
			if fruit == 'B':
				return[[0],[1]]				
			if fruit == 'P':
				return[[0],[0]]
			if fruit == 'O':
				return[[1],[0]]

def convert2char(a):

	if NEURON == 4:
		if np.array_equal(a,[[1],[0],[0],[0]]):
			return 'W'
		elif np.array_equal(a,[[0],[1],[0],[0]]):
			return 'B'
		elif np.array_equal(a,[[0],[0],[1],[0]]):
			return 'P'
		elif np.array_equal(a,[[0],[0],[0],[1]]):
			return 'O'
		else:
			return 'ERROR'

	else:
		if DATA == "Data1":
			if np.array_equal(a,[[0],[0]]):
				return 'W'
			if np.array_equal(a,[[0],[1]]):
				return 'B'
			if	np.array_equal(a,[[1],[0]]):
				return 'P'
			if np.array_equal(a,[[1],[1]]):		
				return 'O'
		elif DATA == "Data2":
			if np.array_equal(a,[[1],[1]]):	
				return 'W'
			if np.array_equal(a,[[0],[1]]):
				return "B"
			if np.array_equal(a,[[0],[0]]):
				return "P"
			if np.array_equal(a,[[1],[0]]):
				return "O"

def print2file(out): 
	print(out)
	print(out,file=output)

def commandline():
	parser = argparse.ArgumentParser()
	parser.add_argument('Data',choices=['Data1','Data2'])
	parser.add_argument('NeuronNum',choices=['2','4'])
	parser.add_argument('Dimension',choices=['2','3'])

	return parser.parse_args()

def usage(args):

	global output
	global DATA
	global NEURON
	global DIMENSION
	global TRAINFILENAME
	global TESTFILENAME

	if(args.Data == 'Data1'):
		DATA = args.Data
		NEURON = int(args.NeuronNum)
		DIMENSION = 2
		TRAINFILENAME = TRAINFILENAME + "training_data1.txt"
		TESTFILENAME = TESTFILENAME + "testing_data1.txt"
		output = open("Data1_output_{}N_2A.txt".format(NEURON),"w")
	if(args.Data == 'Data2'):
		DATA = args.Data
		NEURON = int(args.NeuronNum)
		DIMENSION = int(args.Dimension)
		TRAINFILENAME = TRAINFILENAME + "training_data2.txt"
		TESTFILENAME = TESTFILENAME + "testing_data2.txt"
		output = open("DATA2_output_{}N_{}A.txt".format(NEURON,DIMENSION),"w")	

	print2file('Using {}\nThe weight will be set to {} x {}'.format(DATA,NEURON,DIMENSION))




if __name__ == "__main__":

	args = commandline()
	usage(args)

	neuron = Neuron(NEURON,DIMENSION)

	if(args.Data == 'Data1'):
		if NEURON == 2:
			neuron.w = np.array([[1,0], [0,1]])
			neuron.b = np.array([[1], [1]])

	temp = open(TRAINFILENAME,"r")
	trainData = temp.readlines()

	print2file("{}-Dimension perception\n".format(NEURON))
	print2file("W: {}\n".format(neuron.w))
	print2file("B: {}\n".format(neuron.b))

	while True:

		neuron.clearcounterror()
		for data in trainData:
			
			shape, texture, weight, fruit = data.split()
			print(shape)
			print(texture)
			print(weight)
			print(fruit)
			
			if DIMENSION == 3:
				p = np.array([[float(shape)], [float(texture)], [float(weight)]])
			if DIMENSION == 2:
				p = np.array([[float(shape)],[float(texture)]])

			a = neuron.hardlim(neuron.w.dot(p)+neuron.b)
			neuron.calError(a,convert2array(fruit))

			if neuron.has_error():
				neuron.update_wb(p)

		epoch = epoch + 1
		print2file("epoch {} has {} errors".format(epoch,neuron.getcounterror()))
		if neuron.getcounterror() == 0:
			break
		if epoch > 100000:
			print2file("Data is too large.  Failed")
			break

	print2file("Total epoch: {}\n".format(epoch))		
	print2file("W: {}\n".format(neuron.w))
	print2file("B: {}\n".format(neuron.b))
	print2file("Result: ")

	temp2 = open(TESTFILENAME,"r")
	testData = temp2.readlines()

	count = 1

	for data in testData:
		
		shape, texture, weight = data.split()

		if DIMENSION == 3:
			p = np.array([[float(shape)],[float(texture)],[float(weight)]])
		if DIMENSION == 2:				
			p = np.array([[float(shape)],[float(texture)]])

		a = neuron.hardlim(neuron.w.dot(p)+neuron.b)

		if DATA == "Data1":
			print2file(str(count) + ":\n" + str(a))
		else:
			print2file(str(count) + " " + convert2char(a))

		count = count + 1
















