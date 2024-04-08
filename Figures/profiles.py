import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif', 'font.size': 12})

fig, ax = plt.subplots(figsize = (6., 6.))

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-4., 14.)
ax.set_xlabel(r'$\frac{r-R}{\delta R}$', fontsize = 18)
ax.set_ylabel(r'$\frac{\Delta(r)}{\delta}$', fontsize = 18)

ax.tick_params(which = 'both', direction = 'in')
secxax = ax.secondary_xaxis('top')
secxax.tick_params(which = 'both', direction = 'in')
plt.setp(secxax.get_xticklabels(), visible = False)
secxax.xaxis.set_minor_formatter(ticker.NullFormatter())
secyax = ax.secondary_yaxis('right')
secyax.tick_params(which = 'both', direction = 'in')
plt.setp(secyax.get_yticklabels(), visible = False)

data1 = np.loadtxt('../Computations/k30000_delta0.01.txt')
data2 = np.loadtxt('../Computations/k30000_delta0.001.txt')

ax.plot((data1[:,0] - 1) / 1e-2, data1[:,1] / 1e-2, color = 'forestgreen', label = r'$\delta=10^{-2}$')
ax.plot((data2[:,0] - 1) / 1e-3, data2[:,1] / 1e-3, color = 'darkviolet', label = r'$\delta=10^{-3}$')
ax.legend(fontsize = 14)

fig.tight_layout()
#fig.show()
fig.savefig('profiles.pdf')
