---
date: 2018-07-23
description: The final CalTRACK 2.0 working group meeting recaps hourly methods updates including 3-month weighted baselines, reviews the four major tasks completed during CalTRACK 2.0, and previews the CalTRACK 3.0 sandbox on GitHub.
---

# Working Group Finalizes Hourly Method

**Week Twenty-Two CalTRACK Update**

Last week marked the final CalTRACK 2.0 working group meeting. In this meeting we discussed an update to hourly methods, an overview of our progress during CalTRACK 2.0, and suggestions for CalTRACK 3.0. You can view the final meeting at the following link:

*July 19, 2018 Working Group Meeting — Zoom recording no longer available.*

**Hourly Methods Update:**

Empirical testing has shown correlation between energy consumption and season in residential buildings, that can have an effect on the savings error. The CalTRACK 2.0 working group has proposed accounting for this seasonal effect by shortening the 12-month baseline period to 3-month weighted baseline periods. The figure below shows the effect of shortening baseline periods to 3-month on Normalized Mean Bias Error (NMBE) for residential buildings.

![NMBE seasonal effect chart](site:assets/images/community/blog/caltrack-week22-nmbe-seasonal.png)

However, shortening an annual baseline to 3-month weighted baselines may not be necessary for all building types. Notably, commercial buildings tend to have a smaller seasonal effect than residential buildings, and may not experience increased NMBE from using a 12-month baseline period.

The working group has established the following NMBE thresholds to define buildings that require 3-month weighted baselines and those where an annual baseline period is acceptable:

1. If there are 2 or more months that have an NMBE greater than 0.01, then 3-month weighted baselines are required.
2. If there are less than 2 months that have an NMBE greater than 0.01, then 3-month weighted baselines are optional.

**CalTRACK 2.0 Recap:**

Since February, the CalTRACK 2.0 process has tackled several major issues. Below is a quick synopsis of the major tasks addressed and outcomes for these topics.

**Task 1:** Updates to CalTRACK daily and billing methods based on feedback from CalTRACK 1.0 users. Some updates include:

![CalTRACK 2.0 Task 1 summary](site:assets/images/community/blog/caltrack-week22-task1-summary.png)

- Improved weather station mapping.
- Weighted regression for months in billing period methods.
- Expanded grid search range for variable balance points.
- Maximum lengths for baseline and reporting periods in billing period and daily methods.

**Task 2:** Assess the feasibility of a portfolio aggregation approach for calculating savings as well as any effects on savings uncertainty.

![CalTRACK 2.0 Task 2 portfolio uncertainty](site:assets/images/community/blog/caltrack-week22-task2-portfolio.png)

- For portfolio-based cases, buildings with a high uncertainty metric can still be included in a portfolio as long as the defined portfolio-level uncertainty threshold is not exceeded.
- For site-based applications, ASHRAE Guideline 14 thresholds were recommended.

**Task 3:** Develop a prototype method for calculating hourly savings.

- Lawrence Berkeley National Lab's Time-of-Week and Temperature model was used as a template for hourly methods.
- The aggregated hourly energy savings estimates were stable when considered at the portfolio-level for residential houses, which was an encouraging finding.

**Task 4:** Demonstrate how price signals can adjust the value of hourly load shapes to match procurement needs.

- When price signals are applied to hourly savings estimates, the temporal and locational value of energy efficiency projects can be calculated.
- Various price signals were analyzed and it was shown that they can provide different values to different types of load shapes based on priorities of the procurer.

![CalTRACK 2.0 Task 4 price signals](site:assets/images/community/blog/caltrack-week22-task4-price-signals.png)

**CalTRACK 3.0:**

The direction of CalTRACK 2.0 methods development was guided by feedback from use cases that required "payable savings". For example, PG&E's pay-for-performance energy efficiency program decided to increase compensation for energy savings during peak hours during the second iteration of their program. This required CalTRACK 2.0 to develop methods that generate savings estimates at the hourly level. Similarly, we expect CalTRACK 3.0's tasks will be guided by the demands of stakeholders that implement programs using CalTRACK 2.0 methods.

In addition, we have designed a [CalTRACK 3.0 sandbox](https://github.com/CalTRACK-2/caltrack/projects/2) on GitHub to document issues that require further investigation. We encourage working group members to continue adding ideas to the [CalTRACK 3.0 sandbox](https://github.com/CalTRACK-2/caltrack/projects/2) as they arise.

**Homework:**

- Use the CalTRACK 2.0 methods
- Contribute to the [CalTRACK 3.0 sandbox](https://github.com/CalTRACK-2/caltrack/projects/2)
- Keep an eye out for the open source CalTRACK-based engine release (eemeter 2.0)

Next Working Group Meeting is in 2019!
