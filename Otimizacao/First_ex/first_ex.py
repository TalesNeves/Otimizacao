import numpy, math
import matplotlib.pyplot as plt


def sin_recursive(x,iteration):
    if iteration == 0:
        return x
    elif iteration % 2 == 0:
        flag = 1.0
    else:
        flag = -1.0
    powerx = numpy.power(x,((2*iteration)+1))
    factorial = numpy.math.factorial((2*iteration)+1)
    return (flag * powerx / factorial) + sin_recursive(x,iteration-1)


def cos_recursive(x,iteration):
    if iteration == 0:
        return 1
    elif iteration % 2 == 0:
        flag = 1.0
    else:
        flag = -1.0
    powerx = numpy.power(x,((2*iteration)))
    factorial = numpy.math.factorial((2*iteration))
    return (flag * powerx / factorial) + sin_recursive(x,iteration-1)

def discrete_derivative(samples,stepsize):
    size = len(samples)
    derivative = []
    for i in range(size-1):
        derivative.append((samples[i+1] - samples[i])/stepsize)
    derivative.append(derivative[-1])
    return derivative

def second_derivative(samples,stepsize):
    size = len(samples)
    derivative = []
    for i in range(size-2):
        derivative.append((samples[i+2] - (2*samples[i+1])+samples[i])/(stepsize**2))
    derivative.append(derivative[-1])
    derivative.append(derivative[-1])
    return derivative

numsamples = 100
h = 2*numpy.pi/numsamples
linspace = numpy.linspace(-numpy.pi,numpy.pi,num=numsamples)
sin_data = sin_recursive(linspace,15)
cos_data = cos_recursive(linspace,15)
sin_derivative = discrete_derivative(sin_data,h)
plt.plot(linspace,sin_data,'-')
plt.plot(linspace,sin_derivative,'b-')
plt.plot(linspace,cos_data,'r^',markersize=2)
plt.legend(['Discrete sine','Discrete sine derivative','Discrete cosine'])
plt.show()
plt.clf()


d2dx_cos = discrete_derivative(discrete_derivative(cos_data,h),h)
defd2dx_cos = second_derivative(cos_data,h)
plt.plot(linspace,cos_data,'r^',markersize=2)
plt.plot(linspace,d2dx_cos,'-')
plt.plot(linspace,defd2dx_cos,'^',markersize=2)
plt.legend(['Discrete cosine',' Second cosine derivative', 'Second derivative using definition'])
plt.show()

