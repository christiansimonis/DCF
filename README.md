# Discounted Cash Flow Analysis (DCF)

The purpose of this repository is to enable a fast analysis and visualization of cashflows.




# Discount and visualize your cash flows

Following steps are conducted:

* Assumptions to be taken, such as initial and terminal growth characteristics

* Compounding of future cash flows:

![alt text](https://github.com/christiansimonis/DCF/blob/master/vis/CF.png)

* Discounting of cash flows

* Terminal value is predicted, considering future cash flows till infinity with terminal growth rate:

![alt text](https://github.com/christiansimonis/DCF/blob/master/vis/Sum.png)


 * The present values $PV(t)$ represent all discounted cash flows:  
    
![alt text](https://github.com/christiansimonis/DCF/blob/master/vis/PV.png)

 * Relevant information is provided in a [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html):
 
| t                         |     0 |       1 |     2 |       3 |       4 |       5 |       6 |       7 |       8 |       9 |       10 |
|:--------------------------|------:|--------:|------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|---------:|
| Years                     |  2022 |  2023   |  2024 |  2025   |  2026   |  2027   |  2028   |  2029   |  2030   |  2031   |   2032   |
| Free Cash Flow in $       | 20000 | 21800   | 23762 | 25900.6 | 28231.6 | 30772.5 | 33542   | 36560.8 | 39851.3 | 43437.9 |  47347.3 |
| Terminal Value in $       |     0 |     0   |     0 |     0   |     0   |     0   |     0   |     0   |     0   |     0   | 620371   |
| $PV(t)$ in $              | 20000 | 19818.2 | 19638 | 19459.5 | 19282.6 | 19107.3 | 18933.6 | 18761.5 | 18590.9 | 18421.9 | 257434   |

* The enterprise value is derived from adding the present values $PV(t_i)$ of all cash flows:

**Enterprise value** = $\displaystyle \sum \limits_{i=1}^{10}  PV(t_i)$ = 429448 $ 
 


# Acknowledgements and useful sources

More information and inspiration can be found here:
* [Quantic School of Business and Technolgy](https://quantic.edu/) (no promotion)
* [AlphaWaveData](https://github.com/AlphaWaveData/Jupyter-Notebooks/blob/master/AlphaWave%20Stock%20Valuation%20using%20Free%20Cash%20Flow%20to%20the%20Firm%20example.ipynb)
* [Investopedia](https://www.investopedia.com/terms/t/terminalvalue.asp)
* [Seekingalpha](https://seekingalpha.com/article/4027535-myth-5_5-terminal-value-ate-dcf)

Thanks and reference to:
(Name,                                 Version,                     License)  
* matplotlib                          3.4.2                        Python Software Foundation License,          Copyright (c) 2002 - 2012 John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team; 2012 - 2021 The Matplotlib development team:  [matplotlib license](https://matplotlib.org/stable/users/license.html)
* numpy                               1.19.5                       BSD,                                         Copyright (c) 2005-2020, NumPy Developers: [numpy license](https://numpy.org/doc/stable/license.html#:~:text=Copyright%20(c)%202005%2D2020%2C%20NumPy%20Developers.&text=THIS%20SOFTWARE%20IS%20PROVIDED%20BY,A%20PARTICULAR%20PURPOSE%20ARE%20DISCLAIMED)
* pandas                              1.2.4                        BSD 3-Clause License                         Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team: [pandas license](https://github.com/pandas-dev/pandas/blob/master/LICENSE)

# Time series modeling of financial markets

Are you interested in more time series modeling?
![alt text](https://github.com/christiansimonis/time-series-analysis/blob/master/vis/pred_eval.JPG)

Feel free to check out:
* [Time Series Analysis ](https://github.com/christiansimonis/time-series-analysis)
* [Forks](https://github.com/christiansimonis/time-series-analysis/network/members)
* [Stargazers](https://github.com/christiansimonis/time-series-analysis/stargazers)


# Contact
* [LinkedIn](https://www.linkedin.com/in/christiansimonis/)




# Disclaimer

There have been several attempts to predict enterprise values and stock prices using time series analysis. Many of them were not successful!
Neither trading nor investing decisions should be influenced by this repository or the code, which is built only to introduce and demonstrate a methodology for time series modeling.
No responsibility is taken for correctness or completeness of historic, current or future data, models, information and / or predictions!

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
