---
date: 2018-03-19
description: Week six CalTRACK update covering building qualification metrics, including analysis of intercept-only models and comparison of CVRMSE and MAPE as candidate metrics.
---

# Considering Metrics for Building Qualifications

## Week Six CalTRACK Update

Week six was primarily focused on the building qualification discussions and will continue to be the focus of testing and experimentation this week; this was coming off of an exciting working group meeting on March 15, 2018 linked below.

[Recording: March 15, 2018 Working Group Meeting](https://zoom.us/recording/play/f-HBRyevo26729eJEpuQqFjohJt8ByT9CAYuPS1VTI7SjuAlgpyaqGrYeMKGCUKC)

*Note: Zoom recording links may no longer be accessible.*

![Four types of models for CalTRACK](site:assets/images/community/blog/caltrack-week6-four-types-of-models.png){ align=right width=350 style="margin: 10px 0 10px 20px" }

**Review of properties of intercept-only models in PRISM:**<br>
As we analyze building qualifications, it is useful to review the properties of PRISM intercept-only models to ensure they are properly treated. Here are a few characteristics of intercept-only models:

**Properties:**

- Intercept-only models imply no significant effect of HDD or CDD on energy consumption was detected. Generally, this means that weather did not have a significant effect on the site's energy consumption
- In intercept-only models, predicted energy savings are the difference between the current year's energy consumption and the previous year's consumption
- Significant temperature-related energy savings are not expected at sites with intercept-only models

**Weaknesses:**

- These models are susceptible to poor savings estimates if the previous year was atypical. For example, if a resident did not live in their house for a majority of the previous year, then it may not be a good predictor of energy consumption in the current year
- Intercept-only models impose an average energy consumption over the entire year. This yearly average may be inappropriate when estimating more granular fluctuations, such as daily or hourly energy consumption

![CalTRACK building qualification metrics table](site:assets/images/community/blog/caltrack-week6-metrics-table.png)

**Description of Each Proposed Metric:**<br>
During the upcoming week, we will use empirical testing to establish the preferred metric and threshold to determine a building's suitability for CalTrack methods. The two proposed metrics are described below:

![CVRMSE and MAPE formula reference](site:assets/images/community/blog/caltrack-week6-cvrmse-mape-formulas.png){ align=right width=300 style="margin: 10px 0 10px 20px" }

**Coefficient of Variation Root-Mean-Square-Error (CVRMSE)**<br>
The CVRMSE is calculated by:

1. Measuring the distance between each predicted value and actual value
2. Squaring each of these distances
3. Averaging all of these squared distances from (2)
4. Taking the square root of the average

Because the distances are squared in the CVRSME before they are averaged, outliers can have a large effect on this metric. In the context of pay-for performance, we are uncertain if it is advantageous to choose a metric that is sensitive to outliers or not. We look forward to seeing test results on this issue.

**Mean Absolute Percent Error (MAPE)**<br>
The MAPE is calculated by:

1. Subtracting each observation's actual value from their predicted value
2. Dividing by that observation's actual value
3. Taking the average of the value in (2) for all observations
4. Multiplying by 100 to give the result in a percentage

The MAPE is another appealing metric. It is worth noting that with a MAPE calculation, it is problematic if the actual values are zero for observations because this would require dividing by zero, which is a mathematical problem.

**Other Reference Materials on Baseline Models that inform the discussion:**<br>
In the Granderson, et. al. study cited below, one key question it tackled was: "How can buildings be pre-screened to identify those that are highly model predictable and those that are not, in order to identify estimates of building energy savings that have small errors/uncertainty?"

- Granderson, J., Price, P., Jump, D., Addy, N., Sohn, M. 2015. [Automated Measurement and Verification: Performance of Public Domain Whole-Building Electric Baseline Models.](https://eta.lbl.gov/sites/all/files/publications/lbnl-187596.pdf) Applied Energy 144:106-133.

In the Southern California Edison study, buildings were sorted into four categories to identify applicability of the analytical method.

- Southern California Edison with FirstFuel. February 2016. [Energy Efficiency Impact Study for the Preferred Resources Pilot](https://www.sce.com/wps/wcm/connect/5b0de293-4a61-472b-a32b-ed9c2cd6aea2/EEImpactStudy_SCEWhitePaper.pdf?MOD=AJPERES)

**Suggestions on Testing These Metrics**<br>
Remember, our goal for testing is to establish our preferred metric and threshold for building qualification. When testing the CVRMSE and MAPE metrics, we have some suggestions to yield the most informative results:

1. Test residential, commercial, and industrial buildings separately. This provides information on CalTrack's performance across different building types
2. Test intercept-only model performance. This will inform model usage decisions in the future

**Non-Routine Adjustments:**<br>
Some discussion arose regarding the possibility of making non-routine adjustments for sites that are outliers. CalTRACK 1.0 addressed this issue by stipulating specific criteria for accepting a non-routine adjustment. Specifically, if savings exceeded 50% +/-, either party would be able to make an appeal to remove the project from the portfolio. Other specific considerations may be related to program eligibility, such as a house that adds solar panels during a performance period. At a general level, CalTRACK methods shy away from stipulating methods for non-routine adjustments, as these tend to demand substantial additional effort and may require additional data that would run contrary to the premise of using CalTRACK methods in the first place. As CalTRACK 1.0 testing demonstrated, for aggregators of residential projects, larger sample sizes diminish the effect of these outliers.

**Participant Homework:**

1. Review the Issues page and plans for testing on building qualifications
2. Conduct your own tests on relevant questions
3. Analyze test results as they emerge and comment
