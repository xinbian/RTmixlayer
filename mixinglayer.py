# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:19:02 2016

@author: Xin
"""

import h5py
import numpy as np
import pylab
import matplotlib.pyplot as plt
import os

gamma=0.8
totalsteps=839625;
specout=1000;
variable = ['Prho']
h5file = h5py.File('tests_single_new.h5','r+')

rho_avr=np.zeros(nz, dtype=np.float64)       
#os.remove("rho1d.txt")
step=[]
for i in range(totalsteps/specout+1):
    step.append(str((i+1)*specout).zfill(6))
f=open('rho1d.txt','w')





for ii in range(1,totalsteps+1):
    f.write("%i \n" % ii)
    if ii==1:
        rho_avr[0:nz/2-1]=1
        rho_avr[nz/2:]=1.0833
        np.savetxt(f,rho_avr)
    if ii%specout==0:            
                  rho_avr=np.zeros(nz, dtype=np.float64)       
                  delimiter = ''
                  mylist = ['Fields/',variable[0],'/',step[ii/specout-1]]
                  filepath = delimiter.join(mylist)
                  databk = h5file.get(filepath)
                  np_data = np.array(databk)
                  m1=np_data
                  for i in range(nz):
                      rho_avr[i]=np.mean(m1[i,:,:])
                  
           
                  np.savetxt(f,rho_avr)
               #   plt.plot(rho_avr, label='density')
               #   pylab.legend(loc='best')
               #   istep=str(ii)
               #   titlelist = ['1d profile at ',istep, ' step']
               #   title = delimiter.join(titlelist)
               #   plt.title(title)
               #   plt.xlabel('z-axis grid point')
               #   titlelist = [istep, '.pdf']
               #   title=delimiter.join(titlelist)
               #   plt.savefig(title, format='pdf', dpi=1200)
               #   plt.show()
f.close()
#f = open('output.d','w')
#for zz_ref in range(nz):
# f.write("%4s\t%10s\n" % (zz_ref, np.mean(m1[zz_ref,:,:])))
#f.close()
    
    
    
