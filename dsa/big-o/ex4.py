import numpy as np 
import matplotlib.pyplot as plt 
def complexity_plot():
    plt.style.use('dark_background')
    n = np.linspace(0,10,100)
    y_log = np.log(1+n)
    y_lin = 1.5*n
    y_logLin = n*np.log(1+n)
    qdr = n**2 
    cub = 2*n**3
    exp = 5**n
    plt.figure(figsize=(10, 10))
    plt.plot(n,y_log,'red')
    plt.plot(n,y_lin,'yellow')
    plt.plot(n,y_logLin,'pink')
    plt.plot(n,qdr,'blue')
    plt.plot(n,cub,'green')
    plt.plot(n,exp,'violet')
    plt.ylim([0,100])
    plt.legend(['log','linear','log-linear','quadratic','cubic','exponential'])
    plt.show()

def main():
    complexity_plot()

if __name__ == "__main__":
    main()

