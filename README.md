# Chow-FF-LP3

This repository demonstrates frequency analysis using frequency factors and the log-Pearson Type III distribution as described in [Chow et al. *Applied Hydrology* (1988)](http://ponce.sdsu.edu/Applied_Hydrology_Chow_1988.pdf).

Three analyses are performed using annual maximum discharges for the following:

1. Guadalupe River near Victoria, TX, from Table 12.1.1 in Chow (44 years)
2. Wabash River at Mt. Carmel, IL, from [USGS gage 03377500](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=03377500) (141 years)
3. Tennessee River at Whitesburg, AL, from [USGS gage 03575500](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=03575500) (81 years)

The method described by Chow is contained in the function ```chow_ff_lp3``` defined in ```chow_ff_lp3.py```. The 5- and 50-yr annual maximum discharges in cubic feet per second (cfs) for the three sample records using ```compute_samples.py```.

```
$ python compute_samples.py

```

The values returned for Victoria, TX, are within 1% of those reported in Chow Example 12.3.3.

The empirical plotting position can be computed using:

$$ T = \frac{n+1}{m}$$

The frequency factor method and plotting position for each record are plotted below.

