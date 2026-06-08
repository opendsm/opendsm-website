---
date: 2018-02-19
description: Week Two concludes discussion of monthly and daily methods updates, presenting six key proposals for weather station selection, baseline periods, balance points, and model selection criteria.
---

# Proposed Testing for Monthly & Daily Methods

## Week Two CalTRACK Update

![GitHub Issues Screenshot](site:assets/images/community/blog/caltrack-github-issues.png){ align=right width=333 }

As we complete Week Two (2/12-2/16), we conclude our discussion of "Proposals for Monthly and Daily Methods Updates" and begin testing proposed methods. Here are the six main updates to the daily and monthly methods (click links to jump to [GitHub](https://github.com/CalTRACK-2/caltrack/issues)):

### [Criteria for choosing weather stations](https://github.com/CalTRACK-2/caltrack/issues/65)

- There is still deliberation regarding this topic. CalTrack 1.0's methods chose weather station based on the closest weather station in a unit's climatic zone.
- An evaluation of weather station quality should be included in weather station mapping because data quality varies between weather stations

### [Adjustment to monthly data for models](https://github.com/CalTRACK-2/caltrack/issues/67)

- To simplify the data preparation requirements for monthly modeling, we are proposing an alternate model that accounts for the variability of days in a bill cycle by using a customer's average daily energy use per month in models

### [Defining maximum baseline period](https://github.com/CalTRACK-2/caltrack/issues/68)

- When defining a baseline, too many months of data may positively bias energy usage. To address this, we would like to provide guidance for defining a maximum time period for a more precise definition of the baseline
- Our strategy to investigate the effects of differing baseline periods is to compare test results after running models with a baseline that contains 12, 15, 18, 21, and 24 months of data

### [Include search grid to determine balance points on Monthly Methods](https://github.com/CalTRACK-2/caltrack/issues/69)

- Previously, we only used search grid to determine balance points in Daily Methods. We plan to expand this to Monthly Methods in CalTrack 2.0

### [Expand Balance Point Search Range](https://github.com/CalTRACK-2/caltrack/issues/72)

- From previous data analysis, we determined that the range of allowed values when selecting balance points may have been too restrictive for more severe climates.
- We intend to expand the balance point range as much as possible without causing inflated standard errors

### [Site Model Selection Criteria](https://github.com/CalTRACK-2/caltrack/issues/76)

- We plan to simplify our model selection process. Instead of filtering out all models with insignificant coefficients, we plan to evaluate the best fit models before filtering potentially insignificant results

## Testing Begins

In this upcoming week (starting 2/19), we look forward to beginning the testing process for our daily and monthly methods! We are encouraging participants to test models on their own data and share results on the GitHub. Please include information about data characteristics with the results.

### Homework

- Test the monthly and daily methods with your own data
- Share results on GitHub with a description of data characteristics
- Continue to contribute to discussions on GitHub Issues

## Meeting Recording

If you missed last week's meeting, feel free to review it below at your leisure:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Nn22QZK5oq0" frameborder="0" allowfullscreen></iframe>

[Watch the Video on Zoom](https://zoom.us/recording/play/hm5Bk6AT9exzt8W7yLiULso7AcJh0JLcGtD_h5lvcm7RxJjgBJGso6b3a8LkPml7)

*Note: Zoom recording links may no longer be accessible.*
