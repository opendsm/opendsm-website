---
date: 2018-07-09
description: CalTRACK working group explores how hourly savings can be valued using constant, step, avoided cost, and avoided energy valuation methods, and compares outcomes across home performance, lighting, and load shifting scenarios.
---

# Valuation Approaches in the CalTRACK Methods

**Week Twenty-One CalTRACK Update**

![CalTRACK hourly load shape analysis](site:assets/images/community/blog/caltrack-week21-load-shape.png)

Energy efficiency and other distributed energy resources have the potential to bring value to the grid. The value of energy efficiency in particular has been calculated with averaged assumptions about avoided costs of producing, procuring and distributing energy from fossil fuel infrastructure, as well as other factors in some cases (e.g. avoided emissions, societal benefits etc.).

This valuation is estimated at the regulatory level, when assessing the cost-effectiveness of energy efficiency, but it is usually sequestered from market actors, who have the most control over actual generated energy savings. While pay-for-performance is a key step to aligning the value of energy efficiency with the market actors responsible for it, using total annual savings as the performance metric conceals the time- and location-based value of energy efficiency which can vary significantly.

This current disconnect of energy efficiency savings to its actual value to the grid or emissions avoided is an area ripe for improvements in modeling and understanding the real value of delivered energy savings. Furthermore, it is critical if energy efficiency wants to have a place at the integrated resource planning table. The availability of both hourly savings AND hourly valuations for those savings (e.g. avoided costs or emissions) allows program administrators to estimate, to a much better degree of accuracy, the value of energy efficiency to the grid.

In last week's working group discussion we covered the topic of valuation in the context of hourly load shape analysis conducted through CalTRACK 2.0.

## Introduction

[Portfolio load shapes](https://github.com/CalTRACK-2/caltrack/issues/97) can be used by programs that compensate for hourly energy savings and whose intention is to align the incentives with savings that are valuable to the grid when it is needed. The construction of portfolio load shapes requires:

1. A model for calculating hourly energy savings
2. A method for valuing energy savings

To calculate [hourly energy savings](https://github.com/CalTRACK-2/caltrack/issues/85), CalTRACK methods utilize a time-of-week and temperature model.

To value the energy savings, a valuation method must be applied to the hourly savings calculations.

## Overview of Valuation Methods

There are a range of valuation strategies one can consider; which may have different effects on the outcomes.

**1. Constant Valuation**
Energy savings are valued at a constant price across all hours of the year.

**2. Step Valuation During Peak**
Energy savings are valued higher during peak hours of day. This valuation method assumes the peak period is the same across all days. For example, a step valuation may value energy savings from 5–8 PM 3 times more than non-peak hours of the day.

**3. Avoided Cost Valuation**
Energy savings are valued based on their hourly avoided costs, which provides a unique value for each hour of the year. The total avoided costs include costs associated with transmission, distribution, resource portfolios, carbon and more.

**4. Avoided Energy Valuation**
Energy savings are valued based on the cost of generating a unit of energy at the given time and location. This is similar to Avoided Cost Valuation, but only costs of generating energy are considered.

## Overview of Examined Scenarios

Different programs and even different measures within a program will deliver different types of time-based value even if their annual savings seem similar. Here are three fairly common cases to consider for this example:

**1. Home Performance Scenario**
Home performance improvements, which are primarily focused on weatherization and HVAC, have concentrated energy savings during periods of high and low temperatures, with little to no savings in the shoulder seasons. For example, insulated windows will generate energy savings from reduced heating during the winter and air conditioning during the summer.

**2. Lighting Scenario**
Lighting improvements provide consistent savings year round, during hours when lighting is required.

**3. Load Shifting Scenario**
Load shifting equipment moves energy load from high demand periods to lower demand periods. An example is an air conditioning demand response program that reduces electricity demand during peak hours. Net energy savings from load shifting programs are typically low or neutral because they cause increased energy consumption before and after the high demand period.

## Scenario Load Shape Analysis

In the table below, the home performance, lighting, and load shifting scenarios were compared with different valuation methods. The numbers in this table represent relative value across programs (i.e. they are unit-less), making the comparison of the different methods for a particular measure/program not very meaningful. However, when each row in the table is examined separately, the type of savings that are encouraged by each valuation scheme becomes apparent.

![Matrix of valuation methods vs. scenarios](site:assets/images/community/blog/caltrack-week21-valuation-matrix.png)

The valuation scheme will usually be a policy, market or procurement decision that should consider the ultimate outcomes intended — to ensure incentives and motivation can be aligned.

For example, if a program aims to reduce electricity grid operating costs, then an avoided cost is the most appropriate valuation method. Under this valuation method, the load shifting program is most effective.

However, if a program aims to reduce net energy use, avoided energy valuation may be the most appropriate method. In this context, a market actor may decide that a lighting program is their best option.

**Homework:**

- Review final methods documentation and provide comments on pull request on [GitHub](https://github.com/CalTRACK-2/caltrack/issues/101)
- Review final hourly methods on [GitHub](https://github.com/CalTRACK-2/caltrack/issues/85)
- Provide feedback on portfolio load shape results on [GitHub](https://github.com/CalTRACK-2/caltrack/issues/97)
- Contribute to the [Sand Box](https://github.com/CalTRACK-2/caltrack/projects/2) of future issues

The next working group meeting is in 2 weeks on July 19, 2018.
