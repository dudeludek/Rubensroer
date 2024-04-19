import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leser inn csv fil
csv = pd.read_csv('data/bodeplot_forsterker_log.csv')

# Ordner i lister
f = csv['Frequency (Hz)']
ch1 = csv['Channel 1 Magnitude (dB)']
ch2 = csv['Channel 2 Magnitude (dB)']
phase = csv['Channel 2 Phase (deg)']

# Plotter
fig, ax = plt.subplots(2, figsize=(10,6))
fig.suptitle('Bodeplot forsterker', fontsize=16)

# Forsterkning
ax[0].set_title('Forsterkning')
ax[0].set_ylabel('Forsterkning [dB]')
ax[0].set_xlabel('Frekvens [Hz]')

ax[0].plot(f, ch1, label='Forsterkning')
ax[0].plot(f, ch2, label='Referanse [$10 mV$]')

ax[0].set_xscale('log')
ax[0].set_xticks([50, 100, 250, 500, 1000, 2500, 5000, 10000, 16000])
ax[0].set_xticklabels(['50', '100', '250', '500', '1k', '2.5k', '5k', '10k', '16k'])
ax[0].set_xlim(50, 16000)
ax[0].set_ylim(-3, 40)
ax[0].grid()
ax[0].legend()


# Fase 
ax[1].set_title('Fase')
ax[1].set_ylabel('Fase [deg]')
ax[1].set_xlabel('Frekvens [Hz]')

ax[1].plot(f, phase, label='Fase')

ax[1].set_xscale('log')
ax[1].set_xticks([50, 100, 250, 500, 1000, 2500, 5000, 10000, 16000])
ax[1].set_xticklabels(['50', '100', '250', '500', '1k', '2.5k', '5k', '10k', '16k'])
ax[1].set_xlim(50, 16000)
ax[1].set_ylim(-180, 180)
ax[1].grid()
ax[1].legend()

plt.subplots_adjust(hspace=0.5)
plt.show()