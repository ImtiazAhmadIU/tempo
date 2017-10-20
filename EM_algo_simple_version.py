import random
import math 
import matplotlib.pyplot as plt

def estimation(mean,var,prior,llist):

	pg0x=[]
	pg1x=[]
	pg2x=[]
	ll=[]
	ll0=ll1=ll2=0
	for xi in llist:

		pxg0= (math.exp(-(((xi-mean[0])*(xi-mean[0]))/2/var[0]/var[0])))/math.sqrt(2*3.14156)/var[0]
		pxg1= (math.exp(-(((xi-mean[1])*(xi-mean[1]))/2/var[1]/var[1])))/math.sqrt(2*3.14156)/var[1]
		pxg2= (math.exp(-(((xi-mean[2])*(xi-mean[2]))/2/var[2]/var[2])))/math.sqrt(2*3.14156)/var[2]


		ll0 = ll0 + pxg0
		ll1 = ll1 + pxg1
		ll2 = ll2 + pxg2

		numerator = pxg0 * prior[0]
		denominator = pxg0 * prior[0] + pxg1 * prior[1] + pxg2 * prior[2] 
		pg0x.append(numerator/denominator)

		numerator = pxg1 * prior[1]
		pg1x.append(numerator/denominator)

		numerator = pxg2 * prior[2]
		pg2x.append(numerator/denominator)

	ll.append(ll0)
	ll.append(ll1)
	ll.append(ll2)
	return pg0x,pg1x,pg2x,ll



def maximization(g0,g1,g2,nlist):

	n0=n1=n2=0.0
	nume0=nume1=nume2=0
	nume00=nume11=nume22=0
	m=[]
	v=[]
	p=[]

	for i0 in g0:
		n0 = n0 + i0
	for i1 in g1:
		n1 = n1 + i1
	for i2 in g2:
		n2 = n2 + i2

	'''print('NRWWE\n')
				print(n1)
				print('\n')'''
	for a0,b0 in zip(g0,nlist):
		nume0 = nume0 + a0*b0
		nume00 = nume00 + a0*b0*b0
	for a1,b1 in zip(g1,nlist):
		nume1 = nume1 + a1*b1
		nume11 = nume11 + a1*b1*b1
	for a2,b2 in zip(g2,nlist):
		nume2 = nume2 + a2*b2
		nume22 = nume22 + a2*b2*b2	

	try:
		m.append(nume0/n0)
		m.append(nume1/n1)
		m.append(nume2/n2)

		v.append(math.sqrt((nume00/n0)-(m[0]*m[0])))
		v.append(math.sqrt((nume11/n1)-(m[1]*m[1])))
		v.append(math.sqrt((nume22/n2)-(m[2]*m[2])))

		p.append(n0/(n0+n1+n2))
		p.append(n1/(n0+n1+n2))
		p.append(n2/(n0+n1+n2))
	except:
		print('division by zero')


	return m,v,p


def main():
	text_file = open("data1.txt","r")
	inputValues = text_file.read().split('\n')
	text_file.close()
	new_list=[]
	for i in inputValues:
		if(i!=''):
			new_list.append(float(i))

	#print(new_list)
	mean=[]
	var=[]
	#mean.append(random.random())
	mean.append(random.randint(-30,100))
	var.append(1002)

	#mean.append(random.random())
	mean.append(random.randint(-30,60))
	var.append(5005)

	#mean.append(random.random())
	mean.append(random.randint(-70,150))
	var.append(9009)

	prior = [.33,.33,.34]

	iteration = 0
	logLikelihood=0
	temp = logLikelihood
	dell=1
	llhood=[]
	
	pit=[]			
	while True:
		if(dell < .001):
			break
		else:
			g0,g1,g2,ll = estimation(mean,var,prior,new_list)
			logLikelihood = math.log(prior[0]*ll[0]+prior[1]*ll[1]+prior[2]*ll[2])
			mean,var,prior = maximization(g0,g1,g2,new_list)
			
			#print(logLikelihood)
			llhood.append(logLikelihood)
			pit.append(iteration)
			iteration = iteration + 1
			dell = abs(logLikelihood - temp)
			temp = logLikelihood
			
	
	plt.plot(pit,llhood)
	plt.ylabel('Log Likelihood')
	plt.xlabel('Training Time')
	plt.show()
main()

