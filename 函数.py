import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)

def g(t):
    return np.exp(t)

def h(t):
    return np.exp(0*t)

def x(t):
    return np.sin(t+1)
def n(t):
    return np.exp(0.05*t)*np.sin(t)
def s(t):
    return np.exp(0.05*-t)*np.sin(t)

t1 = np.arange(-5.0, 5.0, 0.1)
t2 = np.arange(-5.0, 5.0, 0.1)
t3 = np.arange(-1000,1000,1)

plt.figure(2)           
plt.subplot(221)      

plt.plot(t1, f(t1), '-b',label='X(t)=e^-t')
plt.plot(t2, g(t2), '-r',label='X(t)=e^t')
plt.plot(t2, h(t2), 'g-',label='X(t)=e^0=1')
plt.legend(loc='best')
plt.xlim((-5, 5))
plt.ylim((-1,10))
plt.xlabel('t/s')
plt.ylabel('X(t)')
ax = plt.gca()                                            
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          
ax.spines['bottom'].set_position(('data', 0))   
ax.spines['left'].set_position(('data', 0))
plt.title("Functional Equation:e^-t,e^t,e^0=1")

plt.subplot(222)      

ax = plt.gca()

plt.plot(t2, x(t2), 'r-')

plt.xlim((-5, 5))
plt.ylim((-2, 2))

plt.xlabel('t/s')
plt.ylabel('X(t)')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')        
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          
ax.spines['bottom'].set_position(('data', 0))   
ax.spines['left'].set_position(('data', 0))
plt.title("Functional Equation:sin(x+1)")

plt.subplot(223)      

ax = plt.gca()
plt.plot(t3, n(t3), 'g-')

plt.xlim((-10, 100))
plt.ylim((-50, 50))

plt.xlabel('t/s')
plt.ylabel('X(t)')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.title("Functional Equation:e^(-0.05t)*sin(X)")



plt.subplot(224)

ax = plt.gca()
plt.plot(t3, s(t3), 'g-')

plt.xlim((-100, 10))
plt.ylim((-50, 50))

plt.xlabel('t/s')
plt.ylabel('X(t)')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.title("Functional Equation:e^(-0.05t)*sin(X)")
plt.show()