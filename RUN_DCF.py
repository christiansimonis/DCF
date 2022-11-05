# Disclaimer: There have been several attempts to predict financial markets or enterprise value (EV) or stock prices using time series analysis. Many of them were not successful!
# Neither trading nor investment decisions should be influenced by this repository and the code, which is built only to introduce and demonstrate a methodology for time series analysis.
# No responsibility is taken for correctness or completeness of historic, current or future data, formulas, models and / or predictions!
#-----------------------------------------------------------------------------------------------------------------------------------
__author__ = "Christian Simonis"
__copyright__ = "Copyright 2022"
__version__ = "1.0"
__maintainer__ = "Christian Simonis"
__email__ = "christian.Simonis.1989@gmail.com"
__status__ = "work in progress"

# Discounted Cash Flow Analysis 
#-----------------------------------------------------------------------------------------------------------------------------------
# Name                                Version                      License  
# matplotlib                          3.4.2                        Python Software Foundation License,          Copyright (c) 2002 - 2012 John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team; 2012 - 2021 The Matplotlib development team: https://matplotlib.org/stable/users/license.html
# numpy                               1.19.5                       BSD,                                         Copyright (c) 2005-2020, NumPy Developers: https://numpy.org/doc/stable/license.html#:~:text=Copyright%20(c)%202005%2D2020%2C%20NumPy%20Developers.&text=THIS%20SOFTWARE%20IS%20PROVIDED%20BY,A%20PARTICULAR%20PURPOSE%20ARE%20DISCLAIMED.
# pandas                              1.2.4                        BSD 3-Clause License                         Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team: https://github.com/pandas-dev/pandas/blob/master/LICENSE
#-----------------------------------------------------------------------------------------------------------------------------------
from datetime import date       # https://docs.python.org/3/library/datetime.html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
#-----------------------------------------------------------------------------------------------------------------------------------


# Parameters for discounted cashflow analysis

# Cash Flow assumption
FCF_init = 20000                # inital cash flow, which will first grow w/ initial rate, then w/ terminal rate


# Phase 1 assumptions:
growth_rate_init = 0.09         # inital growth rate, e.g.: 0.05 =equals 5 %
growth_dur_init = 10            # years of initial growth

# Phase 2 assumptions:
growth_rate_term = 0.022        # terminal growth rate, usually 2 - 2.5 %
discount_rate = 0.10            # discount rate, e.g.: WACC


#-----------------------------------------------------------------------------------------------------------------------------------

#Initialize timeline
timeline_rel =  np.linspace(0,growth_dur_init,growth_dur_init+1)
timeline_abs = date.today().year + timeline_rel




#Calculate free cashflows with compounding w/ initial growth rate
FCF = np.zeros(growth_dur_init+1)
FCF[0] = FCF_init


for i in range(1,growth_dur_init+1):
    FCF[i] = FCF[i-1]*(1+growth_rate_init)
FCF_n = FCF[growth_dur_init]



# Time series for terminal growth
next_y = np.max(timeline_abs)
TCF = np.zeros(growth_dur_init+1)
timeline_term =  np.linspace(next_y+1,next_y+growth_dur_init+1,growth_dur_init+1)
TCF[0] = FCF_n*(1+growth_rate_term)

for i in range(1,growth_dur_init+1):
    TCF[i] = TCF[i-1]*(1+growth_rate_term)



# Calculation of terminal value
TV = FCF_n *(1 + growth_rate_term)/(discount_rate - growth_rate_term)




# Calculation of terminal value
TV =  np.zeros(growth_dur_init+1)
TV[-1] = FCF_n *(1 + growth_rate_term)/(discount_rate - growth_rate_term)



# DCF - initial phase
DCF_initial = np.zeros(growth_dur_init+1)
DCF_initial = FCF / (1 + discount_rate)**timeline_rel



# DCF Terminal Value
DCF_terminal = np.zeros(growth_dur_init+1)
DCF_terminal = TCF / (1 + discount_rate)**(timeline_rel + growth_dur_init + 1) # not till infinity - only the first couple of values
DTV = TV / (1 + discount_rate)**timeline_rel #Discounted Terminal Value

    

# All Cashflows
cashflows = FCF + TV


#Discounted Cash Flows
DCF =  np.zeros(growth_dur_init+1)
DCF = cashflows / (1 + discount_rate)**timeline_rel
  


# Calculation of Enterprise Value
EV = np.sum(DCF[1:]) # using DCFs from next year on. # Note: --> Equity value can be calculated easily: Equity = EV + cash - total debt



# Dataframe
df = pd.DataFrame(data=np.array([timeline_abs, FCF, TV, cashflows, DCF]), index=["Years", "Free Cash Flow in $", "Terminal Value in $", "Sum of Cash Flows in $", "Present value in $"])


#-----------------------------------------------------------------------------------------------------------------------------------

# Visualization of time series
plt.plot(timeline_abs ,FCF,"bx-", linewidth=2, label = 'Cash Flows (w/ initial growth)')
plt.plot([timeline_abs[-1] ,timeline_term[0]],[FCF[-1], TCF[0]],'g',linewidth=2)
plt.plot(timeline_term ,TCF,"gx-", linewidth=2, label = 'Cash Flows (w/ terminal growth till inf)')
#plt.fill(np.concatenate([timeline_term, timeline_term[::-1]]),np.concatenate([0*TCF,TCF[::-1]]), alpha=0.1, fc='g', ec='None', label='Terminal Value ... (till inf)')
plt.xlabel('Time', fontsize=16)
plt.ylabel('Cash Flows (CFs)', fontsize=16)
plt.legend()
plt.title(' Cash Flows for the next years ', fontsize=16)
plt.show()



# Visualization of converging terminal value
fig = plt.figure()
ax = fig.add_subplot()
plt.plot(timeline_abs ,DCF_initial,"bx-", linewidth=2, label = 'D(t): Discounted Cash Flows (w/ initial growth)')
plt.plot([timeline_abs[-1] ,timeline_term[0]],[DCF_initial[-1], DCF_terminal[0]],'g',linewidth=2)
plt.plot(timeline_term ,DCF_terminal,"gx-", linewidth=2, label = 'T(t): Discounted Cash Flows (w/ terminal growth till inf)')
plt.fill(np.concatenate([timeline_term, timeline_term[::-1]]),np.concatenate([0*DCF_terminal,DCF_terminal[::-1]]), alpha=0.1, fc='g', ec='None', label='Terminal Value ')
ax.text(np.max(timeline_abs)  + 1, DCF_terminal[-1]*0.8, r'$ \sum_{t_i = start}^\infty T(t_i) = E $'.replace('start', str(int(np.max(timeline_abs)  + 1))).replace('E', str(int(DTV[-1]) )+" ..."), fontsize=14)
plt.xlabel('Time', fontsize=16)
plt.ylabel('Present Value of CFs', fontsize=16)
plt.legend()
plt.title('DCFs for the next couple of years ', fontsize=16)
plt.show()




# Visualization of all DCFs
fig = plt.figure()
ax = fig.add_subplot()
plt.plot(timeline_abs ,DCF_initial,"bx-.", linewidth=1, label = 'D(t): Discounted Cash Flows (w/ initial growth)')
plt.plot(timeline_abs ,DTV,"gx-.", linewidth=1, label = 'T(t): Discounted Cash Flows (w/ terminal growth)')
plt.plot(timeline_abs ,DCF,"kx-.", linewidth=5, markersize=15, label = 'PV(t): All Discounted Cash Flows | PV(t) = D(t) + T(t)')
plt.xlabel('Time', fontsize=16)
plt.ylabel('Present Value of CFs', fontsize=16)
plt.legend()
plt.title('Present Values of Cash Flows', fontsize=16)
plt.show()


#-----------------------------------------------------------------------------------------------------------------------------------

# Plausibility check
if np.max(abs(DCF_initial + DTV - DCF)) < np.finfo(np.float32).eps: # Check of correctness: Array of discounted cashdlows equaly discounted cashflows from initial growth + discounted cash flows of terminal growth
    print("Plausibility check OK")
else:
    print("NOT PLAUSIBLE")
    
#-----------------------------------------------------------------------------------------------------------------------------------

# Result
print(df.head())
print("Enterprise Value: {} $".format(round(EV))) 