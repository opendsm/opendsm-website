---
date: 2018-04-17
description: CalTRACK working group finalizes building qualification recommendations based on use case, then pivots to hourly methods with an overview of the TOWT and ECAM models and key discussion topics for the coming weeks.
---

# Building Qualifications Results & Recommendations

**Week Ten CalTRACK Update**

The CalTRACK working group finalized discussions on Building Qualifications during the first half of Thursday's (4/12) meeting and dove into the hourly methods during the second half. Bill Koran from SBW consulting provided a helpful overview of hourly models and the [ECAM energy data analysis tool](http://www.sbwconsulting.com/ecam/). The major findings of this meeting are summarized below:

*Video of 4/12/2018 Meeting — Zoom recording no longer available.*

**Building Qualification Observations and Recommendations:**

Main observations that were driving the recommendations:

- Stricter building-level thresholds do not necessarily result in more confidence in portfolio savings.
- Thresholds would vary by data granularity. Distributions of building-level metrics also vary widely by building type, location and climate zone.
- Bias must be minimized for portfolio aggregation to work.

The building qualification recommendations are dependent on use case:

1. For use cases where **confidence in portfolio-level performance is required** (e.g. aggregator-driven pay-for-performance, non-wires alternatives (NWA) procurements), we recommend using a permissive building-level CVRMSE threshold (100% is recommended as a default), but requiring that a portfolio-level metric be respected (e.g. portfolio fractional savings uncertainty).

    The portfolio-level threshold will be a policy decision and may differ depending on the use case (e.g. NWA procurement may require less than 15% uncertainty, regular pay-for-performance program may require 25% etc.)

2. For use cases **where confidence in individual building results is required** (e.g. customer-facing performance based incentives), ASHRAE Guideline 14 thresholds may be used.

**Notes:**

- The FSU thresholds will be context-specific because the value of certainty is not uniform across projects and procurers. For example, a utility may be willing-to-accept a portfolio with 25% uncertainty in the context of a pay-for-performance program. The same utility may require 15% uncertainty for a non-wires alternative project.

CVRMSE and FSU are different metrics and are described in this paper: [A Comparison of Approaches to Estimating the Time-Aggregated Uncertainty of Savings Estimated from Meter Data](http://www.iepec.org/2017-proceedings/polopoly_fs/1.3718217.1502901133!/fileserver/file/796649/filename/024.pdf)

![CalTRACK building qualifications results](site:assets/images/community/blog/caltrack-week10-building-qualifications.png)

**Goals for Hourly Methods:**

Hourly models are necessary for estimating the load impact of energy efficiency. This makes hourly energy savings important information for aggregators and utilities in an energy efficiency marketplace.

Our goal is to establish suitable methods for calculating whole building hourly energy savings for residential and commercial buildings. Additionally, the methods will include guidelines for aggregating site-level savings.

**Discussion Topics:**

We have allotted three weeks to test and discuss hourly methods. Below are some important topics that will need to be addressed:

1. Data Requirements and Sufficiency:
    - Hourly weather data can be unreliable. We will need to establish guidelines for hourly weather data sufficiency and methods for accommodating missing weather values.
    - Data sufficiency requirements for hourly meter data are needed.
    - Hourly data cleaning methods must be defined.
2. Methods:
    - It may be beneficial to adjust our model selection criteria for hourly methods.
    - Aggregating many hourly models will result in high portfolio uncertainty. As a result, it may be necessary to reassess the calculation of portfolio uncertainty in hourly savings.
3. Models:
    - We will need to determine the most suitable hourly model for CalTRACK. Two open source models to begin the discussion are:
        1. The [TOWT model](https://github.com/LBNL-ETA/RMV2.0) (time-of-week and temperature) from Lawrence Berkeley National Lab
        2. [ECAM model](http://www.sbwconsulting.com/ecam/) from SBW consulting

We look forward to future discussions on [GitHub](https://github.com/CalTRACK-2/caltrack/issues/85) regarding these topics.

**Homework:**

1. Use Hourly Method Tools on test data
2. Report findings on [GitHub](https://github.com/CalTRACK-2/caltrack/issues)
3. Offer test criteria for hourly models
4. Watch Phil Price Video about energy modeling and hourly methods: [Everything I Know About Building Energy Modeling, But Never Told Anyone Before](https://vimeo.com/144156352)
