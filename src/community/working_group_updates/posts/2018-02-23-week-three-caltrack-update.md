---
date: 2018-02-23
description: Week three CalTRACK update with methods updates on weather station interpolation, documentation clarifications on definitions of "month" and data sufficiency, and early weather station visualizations by state.
---

# Updates to Monthly and Daily Methods & Documentation

## Week Three CalTRACK Update

As week 3 comes to a conclusion, we continue to "Test Monthly and Daily Methods". Here are a few updates that have occurred this week and some early weather data visualizations. (Click links to [GitHub](https://github.com/CalTRACK-2/caltrack/issues))

## Methods Updates

1. **[Nearest-neighbor interpolation for determining weather value estimates](https://github.com/CalTRACK-2/caltrack/issues/65)**
    - Due to a limited number of available weather stations, there have been suggestions to interpolate weather data using the "nearest-neighbor approach"
    - Employing an interpolation method may provide a more accurate estimate on weather value for units in our dataset. However, there are concerns about the standard errors on interpolated data, its computation requirements, and the issue of missing data when applied to interpolated methods
    - At this point, our discussion has not reached a resolution. We will provide more information on the progress of this discussion when it is available

## Documentation Updates

To ensure effective communication, it is important that we are precise with our vocabulary and identification. Please read these updates to ensure that we are consistent in our discussions and documentation.

1. **[We have three distinct definitions for the word "month"](https://github.com/CalTRACK-2/caltrack/issues/78)**
    - **Month as a period of time** (e.g 12 months): In this case, we are using month as a unit to describe a period of time. Because months vary in length, it is recommended to use more specific time period units, such as day periods. For example, best practice for referring to 12 months would 365 day periods.
    - **Month as calendar month:** If the objective is to refer to a month more generally and not as a unit to measure time periods, please use the term "calendar month"
    - **Month as a billing period:** Month is occasionally used synonymously with the term "billing period". This is not advised because billing periods typically contain a different number of days and start and end on different dates than months. To avoid this ambiguity, use the term billing period when referring to the time interval between billings.

2. **[Distinction between data sufficiency and test data preparation requirements](https://github.com/CalTRACK-2/caltrack/issues/79)**
    - In the documentation for data cleaning and preparation, some of the methods apply exclusively to test data and others may apply to general data sufficiency methods.
    - Best practice: define specifications that are intended for general data sufficiency in a separate "General Data Sufficiency" documentation. Otherwise, add the specification to the documentation for which it applies.

3. **[Distinction between data sufficiency in baseline and reporting period data](https://github.com/CalTRACK-2/caltrack/issues/80)**
    - Certain methods only require baseline data and other methods require data from the reporting period
    - There is some ambiguity about sufficiency requirements for baseline and the reporting period data
    - Our goal is to define sufficiency requirements for baseline and reporting period data, then designate the data sufficiency requirements for each method

Below are plots of all the weather stations in several states (New York, Texas, Illinois, Colorado, and California). You can see that California actually has three weather patterns, but in the other states, the weather is remarkably consistent across the state. The next question will be, how much do the variations in the weather matter?

![Weather stations — New York](site:assets/images/community/blog/caltrack-week3-weather-stations-new-york.png)

![Weather stations — Texas](site:assets/images/community/blog/caltrack-week3-weather-stations-texas.png)

![Weather stations — Illinois](site:assets/images/community/blog/caltrack-week3-weather-stations-illinois.png)

![Weather stations — California](site:assets/images/community/blog/caltrack-week3-weather-stations-california.png)

![Weather stations — Colorado](site:assets/images/community/blog/caltrack-week3-weather-stations-colorado.png)

As we enter week 4 (starting 2/26), we will continue to accept data from testing of "Monthly and Daily Methods". Starting on Wednesday (2/28), we will begin accepting proposals for "Building Qualification Parameters". We look forward to reviewing your test results on GitHub!

**Homework:**

- Test the monthly and daily methods with your own data
- Share results on GitHub with a description of data characteristics
- Continue to contribute to discussions on GitHub Issues on monthly and daily methods and building qualification parameters
- Working Group Meeting on 3/1

![CalTRACK GitHub activity](site:assets/images/community/blog/caltrack-week3-github-activity.png)
