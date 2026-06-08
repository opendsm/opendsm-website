---
date: 2018-05-07
description: CalTRACK working group discusses hourly methods proposals covering data sufficiency, the TOWT modeling approach with occupancy and temperature covariates, use case uncertainty, and a restructured documentation plan for CalTRACK 2.0.
---

# Considering Hourly Methods: Data & Use Cases

**Week Thirteen Update for CalTRACK**

During week thirteen, the CalTRACK working group discussed proposals for hourly methods in the standing meeting. The discussions included helpful suggestions of other reference materials as well as variations that may be appropriate for different applications of hourly methods and suggested improvements in CalTRACK 2.0's documentation. The video from May 3, 2018 is provided at the end of this post.

![CalTRACK TOWT modeling approach](site:assets/images/community/blog/caltrack-week13-towt-approach.png)

## Hourly Methods

In the development of hourly methods, the goal is to establish guidelines that mirror the methodology in billing period and daily methods. However, hourly methods have unique complexities that require departures from billing period and daily methods. These complexities are identified and discussed below:

## Data Management

When compared to hourly data, daily and billing period savings calculations have higher data sufficiency requirements because hourly data contains more information per time period. This characteristic of hourly data supports the two adjustments to hourly data sufficiency requirements listed below:

**1. Usage data sufficiency** will be specified in terms of data coverage (or common support) instead of a minimum time period:

Daily and billing period data sufficiency requirements impose a minimum quantity of time observed from a year of data. In hourly methods, usage data sufficiency will be specified in terms of data coverage in the independent variables. In Time of Week and Temperature (TOWT) models, the independent variables are temperature and occupancy. Data sufficiency requirements will be based on LBNL recommendations for data coverage.

**2. Missing Data**

Temperature has less variation between hours than days or billing periods. Smaller temperature variation between hours increases the likelihood that interpolated temperature values are accurate. For this reason, interpolated temperature values will be allowed in the reporting period for hourly methods. The threshold of allowable interpolated hours will be determined through empirical testing.

**Recommendation for Pay-for-Performance Use Case:**

- In the baseline period, it is recommended to drop hours with missing temperature and usage data.
- In the reporting period, a maximum of 6 missing values per day can be interpolated while maintaining minimum data sufficiency requirements.

## Time Of Week Temperature (TOWT) Modeling Approach

The TOWT model, originally by Lawrence Berkeley Lab, contains two covariates:

**Occupancy:**

Occupancy is an indicator variable that takes the value of 1 if the building is occupied in the hour and 0 otherwise. In LBNL's model, occupancy of a building is defined by:

1. Using ordinary least squares regression to establish a regression model for a building.
2. Grouping all observations at each hour. If 65% of the observations for an hour are above the established regression line, that hour is designated as occupied.
3. If the condition in (2) is not met, then the hour is defined as unoccupied.

**Temperature:**

The TOWT model allows user-defined temperature bins for modeling a building's weather dependence. We are recommending setting 7 fixed bins with endpoints at 30, 45, 55, 65, 75, 90, in order to cover a wide variety of climate conditions.

## Use Case and Uncertainty

**Time-aggregated Uncertainty:**

In the program evaluation use case, an analyst may be interested in obtaining time-aggregated savings and uncertainty. Due to residual autocorrelation at the hourly level, aggregating hourly uncertainty for larger time intervals creates imprecise standard errors and uncertainty calculations. Instead, we recommend using daily methods with improved ASHRAE or Ordinary Least Squares (OLS) formulations of Fractional Savings Uncertainty (see [Koran 2017](http://www.iepec.org/2017-proceedings/polopoly_fs/1.3718217.1502901133!/fileserver/file/796649/filename/024.pdf)) for aggregating uncertainty over time periods.

**Hour-level Uncertainty Estimates:**

For the procurement and pay-for-performance use cases, regression analysis is an effective tool for acquiring point estimates of savings and uncertainty at each hour. If each building is assumed to have independent errors, the uncertainty at each hour for all buildings in the portfolio can be aggregated without an autocorrelation problem.

## Methods Documentation

Currently, the documentation for CalTRACK 2.0 is being updated. The first half of CalTRACK 2.0's documentation will be posted on [GitHub](https://github.com/CalTRACK-2/caltrack/issues) to allow the working group to review and comment on the changes in documentation.

Similar to the methods, the development of effective documentation is an iterative process. The documentation for CalTRACK 2.0 will improve by dividing into three distinct documents:

**1. Methods**

This document outlines the methodology for quantifying billing period, daily, and hourly energy savings while maintaining CalTRACK-compliancy. In CalTRACK 2.0, the Methods will be organized with a numbering system that corresponds to the Methodological Appendix. This will make referencing and accessing the appendix easier.

**2. Methodological Appendix**

The Methodological Appendix summarizes discussions and empirical testing that justify methodological decisions. The Methods will reference sections in the Methodological Appendix for readers to easily access empirical support for methodological decisions.

**3. Field Guide**

A document with minimum requirements for an implementation to maintain CalTRACK-compliancy. This is designed to be a practical and accessible checklist for analysts and other implementers of CalTRACK.

## Ideas for Future CalTRACK Work

A [sandbox](https://github.com/CalTRACK-2/caltrack/projects/2) has been added to the [GitHub](https://github.com/CalTRACK-2/caltrack/issues) site to document proposals for participants to add ideas for future CalTRACK iterations. If you have an idea for CalTRACK 3.0, or beyond that cannot be addressed this year, please add it to the [sandbox](https://github.com/CalTRACK-2/caltrack/projects/2).

## Additional Hourly Methods Resources

1. [LBNL R Code on Time of Week and Temperature (TOWT)](https://bitbucket.org/berkeleylab/eetd-loadshape)
2. [2002 ASHRAE Guideline 14](http://www.eeperformance.org/uploads/8/6/5/0/8650231/ashrae_guideline_14-2002_measurement_of_energy_and_demand_saving.pdf): Section 5 is relevant for data sufficiency requirements.
3. Uniform Methods Project – US Department of Energy
    1. [Peak Demand and Time-Differentiated Energy Savings Cross-Cutting Protocol](https://www.nrel.gov/docs/fy17osti/68566.pdf)
    2. [Whole-Building Retrofit with Consumption Data Analysis Evaluation Protocol](https://www.nrel.gov/docs/fy17osti/68564.pdf)

## Homework

1. Review draft of billing and daily methods [write-up](https://docs.google.com/document/d/1jquLvk87JcR1NUJGBTvgoNzjEr_UML7MlgjevFejwvA/edit?usp=sharing)
2. Review proposals for hourly guidelines on [GitHub](https://github.com/CalTRACK-2/caltrack/issues/85)
3. The next working meeting is after 3 weeks on 5/23

!!! info "Video Recording"
    The video recording for this meeting is not available online. Original filename: `caltrackmay3-2018.mp4`
