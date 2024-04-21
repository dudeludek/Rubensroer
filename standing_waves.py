import numpy as np
import matplotlib.pyplot as plt

L = 1.5
c = 290
x = np.linspace(0, L, 1000)

def frekvens(n):
    return (2*n-1)*c/(4*L)

colors = ['brown', 'red', 'orange', 'yellow']
fig, ax = plt.subplots(figsize=(12, 6))
for n in range(1, 5):
    f = frekvens(n)
    print(f'Frekvens: {f:.3f} \t Bølgelengde: {c/f:.3f}')
    ax.plot(x, np.cos(2*np.pi*f/c*x), label=f'n={n}', color=colors[n-1])

fig.set_facecolor("hotpink")
ax.set_title('Stående bølger i rubensrør')
ax.set_xlabel('x [m]')
ax.set_ylabel('Amplitude')
ax.set_xlim(0, L)
ax.set_facecolor('pink')
x_ticks = np.linspace(0, L, 5)
ax.set_xticks(x_ticks)
ax.set_xticklabels([f'${i/L:.2f}L$' for i in x_ticks])

ax.legend()
ax.grid()
plt.show()

# Bølgefart:
n=3
f=363
b = 0.80
c = b*f

print("Bølgefart: ", c)