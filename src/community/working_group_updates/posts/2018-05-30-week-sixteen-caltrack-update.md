---
date: 2018-05-30
description: CalTRACK working group finalizes site-specific hourly methods including temperature bins, data sufficiency by coverage, and LBNL's occupancy algorithm, then begins discussion on aggregating hourly savings into portfolio load shapes.
---

# Site-Specific Hourly Methods Finalized

**Week Sixteen CalTRACK Update**

![CalTRACK hourly methods finalized](site:assets/images/community/blog/caltrack-week16-hourly-methods.png)

During the standing meeting on 5/24, the working group finalized hourly methods for calculating hourly energy savings and commenced discussion on aggregating hourly savings into portfolio load shapes. The finalized hourly methods and an introduction on aggregating portfolio load shapes are outlined below.

[View May 24, 2018 Working Group Meeting](https://zoom.us/recording/share/B5x90NFPqYqvJbgBPx5JRWajpmqtk1yfLlkwpFC4N-CwIumekTziMw)

**Finalized Hourly Methods:**

1. Data sufficiency for independent variables will be defined by coverage instead of the minimum time period required for daily and billing period methods.
2. The temperature variable will be defined by fixed temperature bins between 30–90°F instead of the variable degree day balance points used in billing period and daily methods.
3. In Lawrence Berkeley National Lab's (LBNL) TOWT model, there is a model adaptation function that gives higher weight to recent data to improve short-term demand forecasts. This model adaptation function will not be used in CalTRACK's hourly methods.
4. The occupancy variable will be defined with LBNL's default occupancy algorithm. This is described in greater detail in Phil Price's [Everything I Know About Building Energy Modelling, But Never Told Anyone Before](https://vimeo.com/144156352) (18:30–30:00).

**Aggregating Hourly Savings into Portfolio Load Shapes**

To provide an accurate valuation of energy efficiency as a grid resource, energy savings must be quantified at specified time intervals and geographic locations. To create portfolio load shapes, building-level savings must be aggregated. The method of aggregation has implications on the portfolio uncertainty and provides different granularity of information for aggregators, utilities, and customers. Different use cases may prefer different aggregation methods based on priorities specific to their use case. To accommodate different use cases, flexible methods for aggregating hourly savings into portfolio load shapes may be preferred.

As we explore this topic further, some potential use cases to consider are:

**Pay-for-Performance Programs**
In the PG&E pay-for-performance program, the utility provides incentives for peak savings. This requires estimates of portfolio savings at the hourly level.

**Non-Wires-Alternative Procurement**
Non-Wires-Alternative procurements require estimates of portfolio savings for buildings connected to specific grid nodes in order to measure grid impacts and potentially avoid infrastructure investments.

**Cap and Trade, Greenhouse Gases, or Carbon Tracking or Trading Initiatives**
Initiatives attempting to accurately quantify carbon offsets from energy efficiency investments require savings estimates at specified time and geographic locations because generation portfolios utilize resources with different carbon intensity at different times and locations.

We discussed a few options for aggregation methods, and look forward to input from the working group in the coming week.

**Homework:**

- Review final Methods documentation and provide comments on [GitHub (issue 101)](https://github.com/CalTRACK-2/caltrack/issues/101)
- Review proposed Hourly guidelines on [GitHub (issue 85)](https://github.com/CalTRACK-2/caltrack/issues/85)
- Provide ideas on aggregation approaches for Portfolio Load shapes on [GitHub (issue 97)](https://github.com/CalTRACK-2/caltrack/issues/97)
- Contribute to the [Sand Box](https://github.com/CalTRACK-2/caltrack/projects/2) of future issues
