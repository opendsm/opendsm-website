---
date: 2018-04-09
description: CalTRACK working group continues building qualification criteria discussions and introduces hourly methods, highlighting the TOWT and ECAM models as starting points for empirical testing in CalTRACK 2.0.
---

# Building Qualification Criteria Discussions

**Week Nine CalTRACK Update**

During week nine of CalTRACK, there were continued discussions on building qualification criteria and some introductory comments on hourly methods. The working group meeting will be held on Thursday, April 12th at 12:00 (PST). We will discuss:

1. Final comments on [building qualification](https://github.com/CalTRACK-2/caltrack/issues/71)
2. Proposals for [hourly methods](https://github.com/CalTRACK-2/caltrack/issues/85) testing

**Hourly Methods Overview:**

Hourly methods are a new addition in CalTRACK 2.0 and were not in the first version of CalTRACK. This task involves testing various hourly modeling methods and recommending a standardized approach to hourly modeling, which can reveal the time value of energy efficiency.

**Importance of Hourly Methods:**

- Hourly methods are a more granular time interval than daily or billing period methods. These granular time intervals are valuable for determining the temporal value of energy savings, by associating savings with grid demand and energy price.

![CalTRACK hourly methods value diagram](/assets/images/community/blog/caltrack-week9-hourly-methods-value.png)

**Time Of Week and Temperature Models:**

To start the discussion of hourly methods, it is helpful to consider existing open source tools. Lawrence Berkeley National Lab has developed an open source time of the week and temperature (TOWT) model to calculate hourly energy savings and is part of the [RMV2.0 - LBNL M&V2.0 Tool](https://github.com/LBNL-ETA/RMV2.0). A TOWT model predicts hourly energy savings by utilizing hourly temperature data instead of daily or billing period HDD and CDD. Another is [ECAM (ENERGY CHARTING & METRICS)](http://www.sbwconsulting.com/ecam/) developed by Bill Koran at SBW consulting.

We look forward to discussion on the working group call about these approaches, and more to frame the approach to empirical tests for the CalTRACK 2.0 hourly methods.

**Final Note:**

It is important to remember that CalTRACK methods development is an iterative process. The finalized methods for CalTRACK 2.0, just like v. 1.0, will benefit from field deployment and may need to be revised in future years. We expect this process to result in improved and refined methods with successive iterations.

**Homework:**

1. Review final results for building qualifications and provide final edits
2. Review existing tools, practice and concepts for hourly methods
3. Discuss and provide suggestions for hourly methods on [GitHub](https://github.com/CalTRACK-2/caltrack/issues/85)
4. Attend the bi-weekly meeting on Thursday April 12th at 12:00 (PST)
