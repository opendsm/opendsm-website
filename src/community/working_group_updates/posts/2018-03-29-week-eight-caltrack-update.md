---
date: 2018-03-29
description: CalTRACK working group discusses building qualification testing results, establishing CV(RMSE) metrics and thresholds to determine which buildings are suitable for portfolio analysis.
---

# Building Qualifications Test Reveals Wide Applicability of CalTRACK Method for Portfolio Analysis

## Week Eight CalTRACK Update

Today we had an exciting working group meeting focused on Building Qualifications with test results and recommendations. We will be stepping into hourly methods in the upcoming week.

[3/29 CalTRACK Working Group Meeting Recording](https://zoom.us/recording/play/c5vbkGb1wM_Jjrt6S2yfZ71aE_7xLHK0m972aiFmG31CEjsTBT8fB_ADZrVXwRx4)

*Note: Zoom recording links may no longer be accessible.*

## Daily and Billing Period Methods Specifications

The final comments on daily and billing period methods have been received. The new, finalized specifications are currently being updated you can track the final on [GitHub Issue #82](https://github.com/CalTRACK-2/caltrack/issues/82). Participants can review the final specifications and track any issues that fed into the final specification prior to their publication at this site.

## Building Qualifications

The CalTRACK methods are equipped to normalize for weather's effect on a building's energy consumption. The methods become unreliable when a building's energy consumption patterns are instead correlated with non-weather variables. For example, irrigation pumps are used on an agricultural cycle rather than in response to temperature changes. It is reasonable to expect higher energy consumption during the growing season and an analyst may suggest re-specifying the model to control for these seasonal variations. Without modification, existing billing and daily CalTRACK models cannot accommodate these nuanced cases. For this reason, buildings that are not well-specified by the CalTRACK model should be identified and removed from portfolios because they have significant effects on portfolio uncertainty. This issue can be tracked on [GitHub Issue #71](https://github.com/CalTRACK-2/caltrack/issues/71).

![CV(RMSE) Analysis](site:assets/images/community/blog/caltrack-building-qualifications-cvrmse.png){ align=right width=400 style="margin: 10px 0 10px 20px" }

## Building Qualification Metric

To evaluate a building's qualification status, a metric and a thresholds should be defined. After empirical testing, the recommended metric for CalTRACK 2.0 is CV(RMSE).

### Justification

- The properties of the CV(RMSE) metric penalize buildings with outlier energy use. Due to their significant effect on portfolio uncertainty, it is recommended that buildings with outlier energy use are eliminated from portfolios. The CV(RMSE) metric makes removing outlier buildings from portfolios more important.
- CV(RMSE) is not sensitive to close to zero individual usage values. This makes it more robust than MAPE and similar metrics.

## Building Type

Building type can be a useful identifier for aggregators to determine a building's suitability for a portfolio. In figure 1, the relationship between energy consumption and CV(RMSE) is measured by building type. The size of each dot corresponds with the number of meters per building type.

![Building Type Analysis](site:assets/images/community/blog/caltrack-building-type-analysis.png)

The CalTRACK methods will be most effective for buildings in region A, which have relatively low energy consumption and low CV(RMSE). Buildings in region B are high energy consumers. These buildings often have a single meter tracking consumption for various sub-buildings with mixed uses, which make it difficult to quantify the effect of an energy-efficiency intervention on overall consumption. These buildings will likely require custom M&V and not qualify for CalTRACK. The buildings in region C have high CV(RMSE). The high CV(RMSE) is likely due to correlation in energy usage that is not specified in the model, such as seasonality. These models should not qualify for CalTRACK.

## CV(RMSE) Threshold for Building Qualification

Due to differences in model quality, portfolio size, and building type between aggregator datasets, it is difficult to establish a universally applicable building-level CV(RMSE) cut-off. The graphs below visualize the relationship between building-level CV(RMSE), portfolio uncertainty, and building attrition. The various graphs show these relationships with different building types and portfolio sizes. While analyzing the graphs, consider that procurers and aggregators tend to be more concerned with portfolio-level uncertainty and building attrition than the building-level CV(RMSE), especially for pay-for-performance programs and Non-Wires Alternatives procurements.

![Portfolio Uncertainty Analysis](site:assets/images/community/blog/caltrack-portfolio-uncertainty.png)

The results show that strict building-level thresholds of 25% CV(RMSE) result in low portfolio uncertainty, but significant building attrition. Also, the results vary depending on the portfolio size and building type. From an aggregators perspective, it may be preferable to adopt a less restrictive building-level CV(RMSE) threshold and focus on minimizing building attrition with respect to a strict portfolio uncertainty threshold.

## Recommendations

We are recommending that the specific building eligibility requirements be generally left to the procurer, who can set the requirements that align best with their goals for a procurement, provided these are specified clearly upfront. CalTRACK can provide general guidelines as follows.

- For use cases where confidence in portfolio-level performance is required (e.g. aggregator-driven pay-for-performance, non-wires alternatives (NWA) procurements), we recommend using a permissive building-level CVRMSE threshold (100% is recommended), but requiring that a portfolio-level metric be respected (e.g. weighted mean CVRMSE or portfolio fractional savings uncertainty). The portfolio-level threshold will be a policy decision and may differ depending on the use case (e.g. NWA procurement may require less than 15% uncertainty, regular pay-for-performance program may require 25% to align with ASHRAE Guideline 14 etc.)
- For use cases where confidence in individual building results is required (e.g. customer-facing performance based incentives), ASHRAE Guideline 14 thresholds may be used.

## Other Reading

Referenced in the working group meeting:

- [Normalized Metered Energy Consumption Draft Guidance CPUC](http://www.cpuc.ca.gov/General.aspx?id=6442456320)
- [ASHRAE Guideline 14](https://www.ashrae.org/technical-resources/standards-and-guidelines)

## Homework

1. Comments on Recommendations for Building Qualifications
2. Suggestions and recommendations for hourly models
3. Revisiting other requirements in terms of hourly models
4. Tests for hourly models

Next CalTRACK working group meeting will be April 12, 2018.
