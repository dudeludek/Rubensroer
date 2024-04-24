import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

# Noen konstanter
L = 1
c = 1
a = 1
b = 1

# Løsning til bølgelikningen
def u(x,t,n=1):
    w = (2*n-1)*np.pi/(2*L)
    return np.cos(w*x)*(a*np.sin(c*w*t)+b*np.cos(c*w*t))

x = np.linspace(0, L, 1000)


# Plotter
fig, ax = plt.subplots(figsize=(12,6))

# Animerer
# initialverdier
line1, = ax.plot(x, u(x,0,1))
line2, = ax.plot(x, u(x,0,2))
line3, = ax.plot(x, u(x,0,3))

# Oppdaterer neste tidssteg
def animate(t):
    line1.set_data(x,u(x,t,1))
    line2.set_data(x,u(x,t,2))
    line3.set_data(x,u(x,t,3))
    return line1,line2,line3

ani1 = ani.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi,100), interval=100)

ax.set_title("Første 3 stående bølger i rubensrør")
ax.set_xlabel("$x$")
ax.set_ylabel("$u(x,t)$")
ax.set_ylim(-2,2)
ax.set_xlim(0,L)
ax.set_xticks([0,0.5*L,L])
ax.set_xticklabels(["$0$", "$0.5L$", "$L$"])
ax.grid()
plt.show()

#Lagre
#ani1.save('rubensbølger.gif', writer="dudek", savefig_kwargs={"transparent": True})