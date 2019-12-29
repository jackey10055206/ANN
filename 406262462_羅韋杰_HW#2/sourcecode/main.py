import numpy as np
import math
import random
import time

trainfile = open("iris_training_data.txt" , "r")
testfile = open("iris_testing_data.txt" , "r")
outputfile = open("Output.txt" , "w")
recoedfile = open("Record.txt" , "w")

global TrainData
global TestData

TrainData = []
TestData = []

hidden_list = [5,10,15,30]
LEARNRATE_list = [1.0,0.5,0.1]

#------------user_config-----------
epoch_limit = 50000
hidden = 5
LEARNRATE = 1.0
#------------user_config-----------



def readfile():
	for i in trainfile.readlines():
		A,B,C,D,fruit = i .split()
		data = ((float(A) , float(B) , float(C) , float(D)),checkfruit(fruit))
		TrainData.append(data)

	for i in testfile.readlines():
		A,B,C,D,fruit = i .split()
		data = ((float(A) , float(B) , float(C) , float(D)),checkfruit(fruit))
		TestData.append(data)


def checkfruit(fruit):
	if fruit == "versicolor":
		return [0.9,0.1,0.1]
	if fruit == "virginica":
		return [0.1,0.9,0.1]
	if fruit == "setosa":
		return [0.1,0.1,0.9]

#基礎神經源
class Neuron():

	#初始化
	def __init__(self,weight):
		self.input = []
		self.weights = []
		self.bias = random.uniform(0.0,1.0)
		self.output = 0.0
		self.delta = 0.0
		for i in range(weight):
			self.weights.append(self.bias)

	#那個e的公式
	def sigmoid(self,x):
		return 1/(1+math.exp(-x))		

	#算output
	def caloutput(self,inputs):
		self.output = 0.0
		self.inputs = inputs
		for i in range(len(self.weights)):
			self.output = self.output + self.weights[i] * inputs[i]
		self.output = self.sigmoid(self.output+self.bias)
		return self.output

	def caldeltas(self,error):
		self.delta = error * self.output * (1-self.output)


	#更新weight和bias，code有錯肯定錯在這裡
	def update (self,learningrate):
		for i in range (len(self.weights)):
			self.weights[i] -= (learningrate * self.inputs[i] * self.delta)
		self.bias -= learningrate * self.delta


#要搞定hidden layer 好難哦= =
class Neuronlayer():

	def __init__(self,inputnum,neuronnum):
		self.neurons = []
		for i in range(neuronnum):
			n = Neuron(inputnum)
			self.neurons.append(n)

	#找所有的output
	def forward(self,inputs):
		outputs = []
		for n in self.neurons:
			outputs.append(n.caloutput(inputs))
		return outputs

	#找誤差
	def finddelta(self):
		return [n.delta for n in self.neurons]

	#更新一下neuron
	def update(self,learningrate):
		for n in self.neurons:
			n.update(learningrate)


class Neuralnetwork():

	def __init__(self,learningrate = 1):
		self.neuronlayer = []
		self.learningrate = learningrate

	def addlayer(self,neuronlayer):
		self.neuronlayer.append(neuronlayer)

	def forward(self,inputs):
		for i in self.neuronlayer:
			inputs = i.forward(inputs)
		return inputs

	#這回推也太複雜了 錯了找這邊
	def back(self,outputs):
		temp = len(self.neuronlayer)
		check = []
		while temp:
			thislayer = self.neuronlayer[temp-1]
			if len(check) == 0:
				for i in range(len(thislayer.neurons)):
					error = (-1) * (outputs[i] - thislayer.neurons[i].output)
					thislayer.neurons[i].caldeltas(error)
			else:
				lastlayer = self.neuronlayer[temp]
				for i in range(len(thislayer.neurons)):
					error = 0
					for j in range(len(check)):
						error = error + check[j] * lastlayer.neurons[j].weights[i]
					thislayer.neurons[i].caldeltas(error)
			check = thislayer.finddelta()
			temp = temp - 1  #哭啊 寫了老半天 忘記加這個

	#這更新 不多說
	def update (self,learningrate):
		for A in self.neuronlayer:
			A.update(learningrate)

	def train(self,data):
		for inputs,outputs in data:
			self.forward(inputs)
			self.back(outputs)
			self.update(self.learningrate)

	def errorRMSE(self,data):
		totalError = 0
		for inputs,outputs in data:
			thisoutput = self.forward(inputs)
			for i in range(len(outputs)):
				totalError = totalError + (outputs[i] - thisoutput[i])**2 
		temp1 = math.sqrt(totalError/len(data))
		return temp1

	#按照pdf決定陣列
	def checkoutput(self,x):
		if x[0] > x[1] and x[0] > x[2]:
			return [0.9,0.1,0.1]
		if x[0] < x[1] and x[1] > x[2]:
			return [0.1,0.9,0.1]
		if x[0] < x[2] and x[1] < x[2]:
			return[0.1,0.1,0.9]


	def finaloutput(self,inputs):
		answer = self.forward(inputs)
		answer = self.checkoutput(answer)
		return answer



def main(hidden,LEARNRATE):

	Network = Neuralnetwork(LEARNRATE)

	hiddenlayer = Neuronlayer(4,hidden)
	Network.addlayer(hiddenlayer)

	outputlayer = Neuronlayer(hidden,3)
	Network.addlayer(outputlayer)

	epoch = 1

	while epoch < epoch_limit and Network.errorRMSE(TrainData) > 0.01:
		Network.train(TrainData)
		print("For HiddenNumer {}, LearningRate {} : Epoch {}, ErrNum {}".format(hidden,LEARNRATE,epoch,Network.errorRMSE(TrainData)))
		print("For HiddenNumer {}, LearningRate {} : Epoch {}, ErrNum {}".format(hidden,LEARNRATE,epoch,Network.errorRMSE(TrainData)) ,file = recoedfile)
		epoch = epoch + 1

	print("Number of hidden neurons = {}".format(hidden),file = outputfile)
	print("Learning rate = {}".format(LEARNRATE) , file=outputfile)

	#處理Train準確度
	trainacc = 0
	for inputs,outputs in TrainData:
		if Network.finaloutput(inputs) == outputs:
			trainacc = trainacc + 1

	trainacc = (trainacc/len(TrainData)*100)
	print("training accuracies = {}%".format(trainacc),file = outputfile)

	#處理Test準確度
	testacc = 0
	for inputs,outputs in TestData:
		if Network.finaloutput(inputs) == outputs:
			testacc = testacc + 1

	testacc = (testacc/len(TestData)*100)
	print("testing accuracies = {}%".format(testacc),file = outputfile)
	print("epochs = {}".format(epoch),file=outputfile)

if __name__ == "__main__":
	
	readfile()
	#main(hidden,LEARNRATE)
	
	outputfile = open("Output.txt" , "w")
	recoedfile = open("Record.txt" , "w")

	time0 = time.time()
	main(hidden,LEARNRATE)
	timestop = time.time()
	
	print("Speed time : {}".format(timestop - time0),file=recoedfile)

