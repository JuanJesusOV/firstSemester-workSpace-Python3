numIterations = 100

#ask iterations numbers for

x1=0
x2=0
x3=0

for i in range(numIterations):
    print("\n---Iteration {}---".format(i+1))
    x1 = (12+x2-(2*x3))/5
    x2 = (-25-(3*x1)+(2*x3))/8
    x3 = (6-x1-x2)/4
    
    print("x1: {}\nx2: {}\nx3: {}".format(x1,x2,x3)) 