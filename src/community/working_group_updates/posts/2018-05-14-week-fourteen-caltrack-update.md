---
date: 2018-05-14
description: CalTRACK working group reviews the Time-of-Week and Temperature (TOWT) model from Lawrence Berkeley National Lab as the specification for CalTRACK 2.0 hourly methods, covering its strengths, weaknesses, and application to site-specific hourly savings.
---

# Time of Week and Temperature Model CalTRACK Application for Site Specific Hourly Savings

**Week Fourteen & Fifteen CalTRACK Update**

Review of hourly method proposals continued in week fourteen of CalTRACK 2.0 and will be finalized at the 5/24 working group meeting. Lawrence Berkeley National Lab's Time-of-Week Temperature (TOWT) model is the specification to be used in CalTRACK 2.0. Mathieu et al. describe the application of TOWT models in [Quantifying Changes in Building Electricity Use, with Application to Demand Response](http://eta-publications.lbl.gov/sites/default/files/LBNL-4944E.pdf).

**Overview of TOWT models:**
As energy efficiency finds its legs as a grid resource, time dependent savings will be essential to the value proposition. Pay-for-performance programs can leverage this value with accurate building-level energy savings calculations at granular time intervals. TOWT models are one method for calculating energy savings at the hourly level.

**Strengths:**

1. Aggregated portfolios for pay-for-performance programs may have high variability in hourly energy consumption due to its nature. This variation is evident in figure 1, which shows load patterns over time for an office building, furniture store, and a bakery. The TOWT model addresses this variability in the following manner:
2. An "occupancy" proxy is determined using a linear regression model and allows for the hourly data to be segmented based on a building's occupancy status.
3. Several "time-of-week" independent variables (one for each hour of the week) are included in the main linear regression model to capture hourly load variation. For example, a restaurant may regularly consume more energy on Friday nights because the restaurant has more customers on Friday nights. This type of variation will be controlled for by the "time-of-week" covariate.
4. The temperature covariate uses 7 bins of fixed temperature ranges instead of employing a grid search to find the balance points. Due to higher amounts of data in hourly methods, the fixed temperature ranges provide a simpler solution without significant drawbacks.

![TOWT load patterns for different building types](site:assets/images/community/blog/caltrack-week14-towt-load-patterns.png)

**Weaknesses:**

1. By nature, calculating hourly energy savings requires more granular data. This can make data sufficiency problematic.
2. Similar to daily methods, energy consumption on weekends or holidays may be different than typical days.
3. There is autocorrelation in the errors of parameter estimates, which complicates uncertainty calculations.

**Homework:**

1. Review draft of billing and daily methods [write-up](https://docs.google.com/document/d/1jquLvk87JcR1NUJGBTvgoNzjEr_UML7MlgjevFejwvA/edit?usp=sharing)
2. Review proposals for hourly guidelines on [GitHub](https://github.com/CalTRACK-2/caltrack/issues/85)
3. The next working group meeting is on Thursday, 5/24
