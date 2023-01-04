import numpy as np
import math
from scipy.stats import skew

#INPUT PARAMETERS
#qout_ann_max: A numpy array containing the annual maximum discharges for the location of interest
#return_period: The desired return period in years (e.g., 100 for the 100-yr flood)

def chow_ff_lp3(qout_ann_max, return_period):
    ymax_log10 = np.log10(qout_ann_max.astype('float64')) #Cast to float64 and take log
    
    ymax_mean  = ymax_log10.mean() #Mean
    ymax_stdv  = ymax_log10.std(ddof=1) #Sample standard deviation (N-1)
    ymax_skew  = skew(ymax_log10, bias=False) #Sample skewness

    p          = 1 / return_period
    w          = pow(math.log(1 / p**2), 1/2)

    z_top      = 2.515517 + 0.802853 * w + 0.010328 * w**2
    z_btm      = 1 + 1.432788 * w + 0.189269 * w**2 + 0.001308 * w**3
    z          = w - (z_top / z_btm)

    #Kite 1977 approximation for K_T
    k          = ymax_skew / 6

    k_1        = z + (z**2 - 1) * k
    k_2        = 1/3 * (z**3 - 6 * z) * k**2
    k_3        = -(z**2 - 1) * k**3
    k_4        = z * k**4
    k_5        = (1/3) * k**5

    k_t        = k_1 + k_2 + k_3 + k_4 + k_5

    #Calculate y_T value for return period T
    y_t        = ymax_mean + k_t * ymax_stdv

    #Generate discharge Q_t for return period T using (10)**y_T
    Q_t = 10**y_t

    return(Q_t)

