import math
import numpy as np
import matplotlib.pyplot as plt

hbar = 6.626e-34/(2*math.pi)
elec = 1.6e-19
a = 20 #radius
ag_epsinf = 3.77
ag_omega_p = 9.15*elec/hbar
ag_gamma = 0.05*elec/hbar
ag_omega_sp = ag_omega_p/math.sqrt(ag_epsinf+2)
ag_OM = math.sqrt(ag_omega_sp**2 - (ag_gamma**2)/4.)

au_epsinf = 9.15
au_omega_p = 9*elec/hbar
au_gamma = 0.07*elec/hbar
au_omega_sp = au_omega_p/math.sqrt(au_epsinf+2)
au_OM = math.sqrt(au_omega_sp**2 - (au_gamma**2)/4.)

pt_epsinf = 1
pt_omega_p = 5.14*elec/hbar
pt_gamma = 0.07*elec/hbar
pt_omega_sp = pt_omega_p/math.sqrt(pt_epsinf+2)
pt_OM = math.sqrt(pt_omega_sp**2 - (pt_gamma**2)/4.)

al_epsinf = 1
al_omega_p = 12*elec/hbar
al_gamma = 0.13*elec/hbar
al_omega_sp = al_omega_p/math.sqrt(al_epsinf+2)
al_OM = math.sqrt(al_omega_sp**2 - (al_gamma**2)/4.)

t = np.linspace(0,100,1001)*1e-15
ag_alpha = (3./(ag_epsinf+2))*(ag_omega_sp**2)/(ag_OM)*np.exp(-ag_gamma*t/2.)*np.sin(ag_OM*t)
au_alpha = (3./(au_epsinf+2))*(au_omega_sp**2)/(au_OM)*np.exp(-au_gamma*t/2.)*np.sin(au_OM*t)
pt_alpha = (3./(pt_epsinf+2))*(pt_omega_sp**2)/(pt_OM)*np.exp(-pt_gamma*t/2.)*np.sin(pt_OM*t)
al_alpha = (3./(al_epsinf+2))*(al_omega_sp**2)/(al_OM)*np.exp(-al_gamma*t/2.)*np.sin(al_OM*t)

plt.figure()
plt.plot(t,ag_alpha,label='ag')
plt.plot(t,au_alpha,label='au')
plt.plot(t,pt_alpha,label='pt')
plt.plot(t,al_alpha,label='al')
plt.legend()
plt.savefig('all_alpha.pdf')
plt.show()

plt.subplot(4,1,1)
plt.plot(t,ag_alpha)
plt.legend(['ag'])
plt.subplot(4,1,2)
plt.plot(t,au_alpha)
plt.legend(['au'])
plt.subplot(4,1,3)
plt.plot(t,pt_alpha)
plt.legend(['pt'])
plt.subplot(4,1,4)
plt.plot(t,al_alpha)
plt.legend(['al'])
plt.savefig('alpha_subplot.pdf')
plt.show()