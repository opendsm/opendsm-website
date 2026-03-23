---
date: 2018-04-23
description: CalTRACK working group begins hourly methods discussion, introducing the Time of Week and Temperature (TOWT) model from LBNL and identifying key topics for empirical testing including data sufficiency, model selection, and portfolio uncertainty.
---

# Hourly Methods Approach & Testing Considerations

**Week Eleven CalTRACK Update**

Week eleven was the first week of hourly methods discussion. Developing hourly methods will require discussion and empirical testing of topics unique to hourly methods before we can make final specifications.

Topics that must be addressed include:

- Data sufficiency requirements
- Modeling approach
- Model selection criteria
- The effect of aggregating hourly models on portfolio uncertainty

**Time Of Week Temperature Models (TOWT):**

A proposed model for hourly methods is the TOWT model from Lawrence Berkeley National Labs (LBNL) is shown below.

![CalTRACK TOWT model diagram 1](/assets/images/community/blog/caltrack-week11-towt-model-1.png)

![CalTRACK TOWT model diagram 2](/assets/images/community/blog/caltrack-week11-towt-model-2.png)

**Notes:**

1. The number of temperature ranges and the balance points will need to be defined. The LBNL model had 5 ranges (< 55F, 55-65 F, 65-75 F, 75-90 F, 90 F <).
2. The methods for defining if a building is occupied or not is explained in detail in Phil Price's [Everything I Know About Building Energy Modeling, But Never Told Anyone Before](https://vimeo.com/144156352) (18:30-30:00).

**Homework:**

1. Use Hourly Method Tools on test data
2. Report findings on [Github](https://github.com/CalTRACK-2/caltrack/issues)
3. Offer test criteria for hourly models
