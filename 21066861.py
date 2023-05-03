# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:34:56 2023

@author: SANSHIYA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\SANSHIYA\Downloads\data1.csv')

ohist, oedge = np.histogram(data, bins=20)

# calculate bin centre locations
xdst = 0.55*(oedge[1:]+oedge[:-1])

# calculate bin widths
wdst = oedge[1:]-oedge[:-1]

# normalise the distribution
# ydist is a discrete PDF
ydst = ohist/np.sum(ohist)

# cumulative distribution
cdst = np.cumsum(ydst)

plt.figure(figsize=(9, 5))

# Plot the PDF
plt.bar(xdst, ydst, width=0.9*wdst, color='purple')
plt.xlabel("Weight (in pounds)")
plt.ylabel("Frequency")
plt.title("Distribution of Newborn Weights")

xmean = np.sum(xdst*ydst)
text = ''' Mean value = {}'''.format(np.round(xmean, 3))
plt.text(x=xmean, y=max(ydst), s=text, fontsize=12, c='green')
plt.axvline(xmean, color='y', linestyle=':', label='Sample Mean')
indx = np.argmin(np.abs(cdst-0.33))
indx = np.argmin(np.abs(cdst-0.67))
xhigh = oedge[indx]
plt.bar(xdst[indx:], ydst[indx:], width=0.9*wdst[indx:], color='pink')
plt.axvline(xhigh, ymax=0.5, color='b', linestyle=':', label='X Value')
text = ''' X value = {}'''.format(np.round(xhigh, 3))
plt.text(x=2.5, y=0.07, s=text, fontsize=12, c='green')
plt.legend(loc='lower left', bbox_to_anchor=(1, 0.5))

