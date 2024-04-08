import matplotlib.pyplot as plt
from matplotlib import colors, ticker
import numpy as np

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif', 'font.size': 12})

fig, ax = plt.subplots(figsize = (7.5, 6.))

ax.set_xlim(10 ** 3.5, 1e5)
ax.set_ylim(1e-3, 1e-2)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel(r'$kR$', fontsize = 14)
ax.set_ylabel(r'$\delta$', fontsize = 14)

ax.tick_params(which = 'both', direction = 'in', size = 5)
secxax = ax.secondary_xaxis('top', zorder = 1)
secxax.tick_params(which = 'both', direction = 'in', size = 5)
plt.setp(secxax.get_xticklabels(), visible = False)
secxax.xaxis.set_minor_formatter(ticker.NullFormatter())
secyax = ax.secondary_yaxis('right', zorder = 1)
secyax.tick_params(which = 'both', direction = 'in', size = 5)
plt.setp(secyax.get_yticklabels(which = 'both'), visible = False)

data = np.loadtxt('../Computations/origin.txt')
ks = data[:,0].reshape(50, 50)
deltas = data[:,1].reshape(50, 50)
vals = data[:,2].reshape(50, 50) / deltas

levels = np.concatenate((-np.logspace(2.5, 0.25, 10), [0], np.logspace(0.25, 2.5, 10)))
cntr = ax.contourf(ks, deltas, vals, levels, cmap = 'coolwarm_r', norm = colors.SymLogNorm(linthresh = 10 ** 0.25, base = 10))
ax.plot(ks[:,0], (4 / ks[:,0]) ** (2 / 3), color = 'k', linestyle = '--')
ax.plot(3e4, 9.5e-3, marker = '*', ms = 15, color = 'forestgreen', zorder = 1)
ax.plot(3e4, 1.04e-3, marker = '*', ms = 15, color = 'darkviolet', zorder = 1)

cbar = fig.colorbar(cntr, ticks = [-10 ** 2.5, -10 ** 2, -10 ** 1.5, -10, -10 ** 0.5, 0., 10 ** 0.5, 10, 10 ** 1.5, 10 ** 2, 10 ** 2.5])
cbar.ax.set_yticklabels([r'$-10^{2.5}$', r'$-10^2$', r'$-10^{1.5}$', r'$-10$', r'$-10^{0.5}$', r'$0$', r'$10^{0.5}$', r'$10$', r'$10^{1.5}$', r'$10^2$', r'$10^{2.5}$'])
cbar.set_label(r'$\frac{\Delta(R)}{\delta}$', fontsize = 18, rotation = 0, y = 0.54)

fig.tight_layout()
#fig.show()
fig.savefig('contour.pdf')
