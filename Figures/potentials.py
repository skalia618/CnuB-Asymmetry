import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
from scipy import special

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif', 'font.size': 12})

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (6., 7.5), height_ratios = (4., 1.))

jn = lambda n, z: special.spherical_jn(n, z)
jd = lambda n, z: special.spherical_jn(n, z, True)
yn = lambda n, z: special.spherical_yn(n, z)
yd = lambda n, z: special.spherical_yn(n, z, True)

xlim1 = 0.84
xlim2 = 1.16
ylim1 = 3e5
ylim2 = 6e5
ax1.set_xlim(xlim1, xlim2)
ax1.set_ylim(ylim1, ylim2)
ax1.set_xlabel(r'$r$', fontsize = 14)
ax1.set_ylabel(r'$V_\mathrm{eff}(r)$', fontsize = 14)

rs = np.linspace(xlim1, xlim2, 1000)[1:]
delta = 0.05
k = 1000
l1a = 900
r1a = np.sqrt(l1a * (l1a + 1) / (1 + 2 * delta) / k ** 2)
l1b = (np.sqrt(1 + 4 * (1 - 2 * delta) * k ** 2 * r1a ** 2) - 1) / 2
l2a = 1030
r2a = np.sqrt(l2a * (l2a + 1) / (1 + 2 * delta) / k ** 2)
l2b = (np.sqrt(1 + 4 * (1 - 2 * delta) * k ** 2 * r2a ** 2) - 1) / 2

ax1.axvline(1, color = '0.7', linestyle = ':')
ax1.plot(rs, l1a * (l1a + 1) / 2 / rs ** 2 - delta * k ** 2 * (rs < 1), color = 'crimson')
ax1.plot(rs, l1b * (l1b + 1) / 2 / rs ** 2 + delta * k ** 2 * (rs < 1), color = 'royalblue')
ax1.plot(rs, l2a * (l2a + 1) / 2 / rs ** 2 - delta * k ** 2 * (rs < 1), color = 'crimson')
ax1.plot(rs, l2b * (l2b + 1) / 2 / rs ** 2 + delta * k ** 2 * (rs < 1), color = 'royalblue')

ax1.axhline(k ** 2 / 2, color = 'k', linestyle = '--')
r0 = np.sqrt(l2a * (l2a + 1)) / k
ax1.axvline(r0, color = 'darkgoldenrod')

ax1.text(1.14, 3.04e5, r'1a', color = 'crimson', ha = 'center', va = 'center', size = 'large')
ax1.text(1.06, 3.04e5, r'1b', color = 'royalblue', ha = 'center', va = 'center', size = 'large')
ax1.text(1.15, 4.11e5, r'2a', color = 'crimson', ha = 'center', va = 'center', size = 'large')
ax1.text(1.15, 3.37e5, r'2b', color = 'royalblue', ha = 'center', va = 'center', size = 'large')
ax1.text(1.15, 5.13e5, r'$\frac{k^2}{2m}$', color = 'k', ha = 'center', va = 'center', size = 'x-large')
ax1.text(0.995, 5.84e5, r'$r=R$', color = '0.7', rotation = 90., ha = 'center', va = 'center', size = 'large')
ax1.text(1.025, 5.84e5, r'$r=r_+$', color = 'darkgoldenrod', rotation = 90., ha = 'center', va = 'center', size = 'large')

plt.setp(ax1.get_xticklabels(), visible = False)
plt.setp(ax1.get_yticklabels(), visible = False)
ax1.tick_params(left = False, bottom = False)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.plot(1., ylim1, linestyle = '', marker = '>', ms = 8, color = 'k', transform = ax1.get_yaxis_transform(), clip_on = False)
ax1.plot(xlim1, 1., linestyle = '', marker = '^', ms = 8, color = 'k', transform = ax1.get_xaxis_transform(), clip_on = False)

ylim3 = 3e-3
ax2.set_xlim(xlim1, xlim2)
ax2.set_ylim(-ylim3, ylim3)
ax2.set_ylabel(r'$\varphi_\ell(r)$', fontsize = 14)

ax2.axhline(0, color = 'k', linewidth = '0.8')
ax2.axvline(1, color = '0.7', linestyle = ':')
ax2.plot(rs, rs * jn(l2a, k * rs), color = 'forestgreen')
ax2.axvline(r0, color = 'darkgoldenrod')
dr = 0.016
ax2.plot([r0, r0 - dr], [0, 0], 'darkgoldenrod')
ax2.plot(r0 - dr, 0, linestyle = '', marker = '<', ms = 7, color = 'darkgoldenrod')
ax2.text(1.024, -1.5e-3, r'$L_\mathrm{tunnel}$', rotation = 90., color = 'darkgoldenrod', ha = 'center', va = 'center', size = 'large')

plt.setp(ax2.get_xticklabels(), visible = False)
plt.setp(ax2.get_yticklabels(), visible = False)
ax2.tick_params(left = False, bottom = False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.plot(1., 0., linestyle = '', marker = '>', ms = 8, color = 'k', transform = ax2.get_yaxis_transform(), clip_on = False)
ax2.plot(xlim1, 1., linestyle = '', marker = '^', ms = 8, color = 'k', transform = ax2.get_xaxis_transform(), clip_on = False)

fig.tight_layout()
#fig.show()
fig.savefig('potentials.pdf')
