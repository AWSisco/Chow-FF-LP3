# Chow-FF-LP3

This repository demonstrates flood frequency analysis using frequency factors and the log-Pearson Type III distribution as described in Section 12.3 of [Chow et al. Applied Hydrology (1988)](http://ponce.sdsu.edu/Applied_Hydrology_Chow_1988.pdf).

Here, three analyses are performed using annual maximum discharges for the following:

1. Guadalupe River near Victoria, TX, from Table 12.1.1 in [Chow](http://ponce.sdsu.edu/Applied_Hydrology_Chow_1988.pdf) (44 years)
2. Wabash River at Mt. Carmel, IL, from [USGS gage 03377500](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=03377500) (141 years)
3. Tennessee River at Whitesburg, AL, from [USGS gage 03575500](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=03575500) (81 years)

The method described by Chow is defined in ```chow_ff_lp3.py``` and can be used by calling the fuction ```chow_ff_lp3```. To demonstrate, the 5- and 50-yr annual maximum discharges for the three sample records are estimated using ```compute_samples.py```.

```
$ python compute_samples.py
		5 years	50 years
Victoria, TX	41149	122143
Mt Carmel, IL	201426	298373
Whitesburg, AL	253013	313311
```

The values returned for Victoria, TX, are within 1% of those reported in [Chow]((http://ponce.sdsu.edu/Applied_Hydrology_Chow_1988.pdf) Example 12.3.3 (page 394).

The empirical plotting position can be computed using:

$$ T = \frac{n+1}{m}$$

where *n* is the number of years in the record and *m* is the rank of each value in a list ordered by descending magnitude.

For each site, discharges for a range of return periods are estimated using the frequency factor method. The plotting positions are shown for reference.

<p align="center">
  <img src="https://user-images.githubusercontent.com/37667176/210648428-578e8e02-4f2a-4864-a1cb-310390f222e1.png" width=65% height=65%>
</p>
