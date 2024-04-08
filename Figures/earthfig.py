import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

fig, ax = plt.subplots(figsize = (8., 4.))

plt.rcParams.update({'text.usetex': True, 'font.family': 'serif', 'font.size': '11'})

ax.add_artist(plt.Circle((0., 0.,), radius = 1., fc = 'white', ec = 'black'))
delta = 0.4
x0 = 0.
y0 = 1 / (1 + delta)
ax.add_artist(plt.Circle((x0, y0), radius = 0.022, color = 'black', zorder = 2))

slope = 0.5
x1 = (-slope * y0 - np.sqrt(1 + slope ** 2 - y0 ** 2)) / (1 + slope ** 2)
x2 = (-slope * y0 + np.sqrt(1 + slope ** 2 - y0 ** 2)) / (1 + slope ** 2)
y1 = (y0 - slope * np.sqrt(1 + slope ** 2 - y0 ** 2)) / (1 + slope ** 2)
y2 = (y0 + slope * np.sqrt(1 + slope ** 2 - y0 ** 2)) / (1 + slope ** 2)
ax.plot([x1, x2], [y1 - 0.01, y2 - 0.01], color = 'crimson')
ax.plot([x1, x2], [y1 + 0.01, y2 + 0.01], color = 'royalblue')
thetain1 = np.arctan(slope) + np.arctan(y1 / x1)
thetaout1_anti = np.arcsin((1 + delta) * np.sin(thetain1))
thetaout1_nu = np.arcsin((1 - delta) * np.sin(thetain1))
slopeout1_anti = np.tan(thetaout1_anti - np.arctan(y1 / x1))
slopeout1_nu = np.tan(thetaout1_nu - np.arctan(y1 / x1))
ax.plot([x1, x1 - 10], [y1 - 0.007, y1 - 10 * slopeout1_anti - 0.007], color = 'crimson')
ax.plot([x1, x1 - 10], [y1 + 0.007, y1 - 10 * slopeout1_nu + 0.007], color = 'royalblue')
thetain2 = np.arctan(slope) - np.arctan(y2 / x2)
thetaout2_anti = np.arcsin((1 + delta) * np.sin(thetain2))
thetaout2_nu = np.arcsin((1 - delta) * np.sin(thetain2))
slopeout2_anti = np.tan(thetaout2_anti + np.arctan(y2 / x2))
slopeout2_nu = np.tan(thetaout2_nu + np.arctan(y2 / x2))
ax.plot([x2, x2 + 10], [y2 - 0.007, y2 + 10 * slopeout2_anti - 0.007], color = 'crimson')
ax.plot([x2, x2 + 10], [y2 + 0.007, y2 + 10 * slopeout2_nu + 0.007], color = 'royalblue')

x3 = np.sqrt(1 - y0 ** 2)
ax.plot([-x3, x3], [y0 - 0.007, y0 - 0.007], color = 'crimson', linestyle = '--')
ax.plot([-x3, x3], [y0 + 0.007, y0 + 0.007], color = 'royalblue')
thetain3 = np.arctan(y0 / x3)
thetaout3_anti = np.arcsin((1 + delta) * np.sin(thetain3))
thetaout3_nu = np.arcsin((1 - delta) * np.sin(thetain3))
slopeout3_anti = np.tan(np.arctan(y0 / x3) - thetaout3_anti)
slopeout3_nu = np.tan(np.arctan(y0 / x3) - thetaout3_nu)
ax.plot([x3, x3 + 10], [y0 - 0.007, y0 + 10 * slopeout3_anti - 0.007], color = 'crimson', linestyle = '--')
ax.plot([x3, x3 + 10], [y0 + 0.007, y0 + 10 * slopeout3_nu + 0.007], color = 'royalblue')
ax.plot([-x3, -x3 - 10], [y0 - 0.007, y0 + 10 * slopeout3_anti - 0.007], color = 'crimson', linestyle = '--')
ax.plot([-x3, -x3 - 10], [y0 + 0.007, y0 + 10 * slopeout3_nu + 0.007], color = 'royalblue')
ax.plot([-10., 10.], [1.02, 1.02], color = 'crimson')

ax.text(x0 + 0.03, y0 - 0.07, r'$P$', color = 'black', ha = 'center', va = 'center', size = 'x-large')
ax.add_artist(Arc((-x3, y0), 0.2, 0.2, color = '0.5', theta1 = 0., theta2 = -np.arctan(slopeout3_anti) * 180 / np.pi))
ax.text(-x3 + 0.15, y0 + 0.05, r'$\theta_c$', color = '0.5', ha = 'center', va = 'center', size = 'x-large')
ax.add_artist(plt.arrow(0.5, 0.05, 0.5, 0., color = '0.5', head_width = 0.04, length_includes_head = True))
ax.add_artist(plt.arrow(0.5, 0.05, -0.5, 0., color = '0.5', head_width = 0.04, length_includes_head = True))
ax.text(0.5, 0.1, r'$R$', color = '0.5', ha = 'center', va = 'center', size = 'x-large')
ax.add_artist(plt.arrow(x0, (1 + y0) / 2, x0, (1 - y0) / 2, color = '0.5', head_width = 0.03, length_includes_head = True))
ax.add_artist(plt.arrow(x0, (1 + y0) / 2, x0, -(1 - y0) / 2, color = '0.5', head_width = 0.03, length_includes_head = True))
ax.text(-0.06, (1 + y0) / 2, r'$\delta R$', color = '0.5', ha = 'center', va = 'center', size = 'x-large')
ax.add_artist(plt.arrow(-0.3, 1.02, 0., -0.41, color = 'darkgoldenrod', head_width = 0.03, length_includes_head = True))
ax.text(-0.4, 0.83, r'$L_\mathrm{tunnel}$', color = 'darkgoldenrod', ha = 'center', va = 'center', size = 'x-large')

ax.text(-1.16, 0.05, r'1a', color = 'crimson', ha = 'center', va = 'center', size = 'large')
ax.text(-1.14, 0.21, r'1b', color = 'royalblue', ha = 'center', va = 'center', size = 'large')
ax.text(-1.16, 0.83, r'2b', color = 'royalblue', ha = 'center', va = 'center', size = 'large')
ax.text(-1.16, 1.07, r'2a', color = 'crimson', ha = 'center', va = 'center', size = 'large')

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(0., 1.2)
ax.axis('off')

fig.tight_layout()
#fig.show()
fig.savefig('earthfig.pdf')
