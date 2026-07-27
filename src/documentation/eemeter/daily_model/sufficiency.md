# Sufficiency Criteria<br><div style="text-align: left; font-size: 0.5em; color: #888; margin-bottom: -2.3em;">Last updated: OpenDSM 1.0</div>

Most sufficiency criteria derive their origins from the CalTRACK specifications. OpenDSM uses its own
reference numbers; the corresponding CalTRACK 2.1 rule is cited inline after each criterion for
cross-reference. A remnant of the old CalTRACK specifications is that there are two types of checks performed, disqualification and warnings. Disqualification is a hard line that means meters should not be used for measurement. A warning is purely for experts to take a deeper look at the data to possibly disqualify them. This page records the complete set of sufficiency criteria — both those the library checks (as a disqualification or warning) and those left to the user to apply — regardless of how strictly the code enforces each.

Many sufficiency criteria are duplicated between the various models, but for the sake of completeness they will be included in definitions for all models.

---

## Nomenclature

- Valid Data: Data which is not NULL, NaN, or otherwise empty
- Joint Data: The combination of all inputs

---

## 1. Data Sufficiency

### **1.1 User Responsibilities**
There are some checks that should be performed which cannot be performed within the confines of the data or model classes, but are critical for valid measurements
<div style="padding-left: 20px;" markdown="1">

#### **1.1.1 Period Definition**
<div style="padding-left: 20px;" markdown="1">

##### **1.1.1.1 Blackout Period**
<div style="padding-left: 20px;" markdown="1">
The blackout period should be known, or at least estimated, and excluded from being included in the data.
</div>

##### **1.1.1.2 Baseline Period**  ·  CalTRACK 2.2.1.1
<div style="padding-left: 20px;" markdown="1">
The baseline period should be one year immediately prior to the blackout period
</div>

##### **1.1.1.3 Reporting Period**
<div style="padding-left: 20px;" markdown="1">
The reporting period should be one year immediately following the blackout period
</div>

</div>

#### **1.1.2 Units**
<div style="padding-left: 20px;" markdown="1">
Units can be critically important to model performance. Convert your units accordingly.

##### **1.1.2.1 Temperature**
<div style="padding-left: 20px;" markdown="1">
Temperature data should be in °Fahrenheit
</div>

##### **1.1.2.2 Consumption/Usage**  ·  CalTRACK 2.1.1.3
<div style="padding-left: 20px;" markdown="1">
Consumption data is expected to be in some kind of units of energy
</div>

</div>

#### **1.1.3 Model Results**
<div style="padding-left: 20px;" markdown="1">

##### **1.1.3.1 Predicted Energy Aggregation**
<div style="padding-left: 20px;" markdown="1">
Predicted energy can be aggregated through simple summation
</div>

##### **1.1.3.2 Predicted Energy Uncertainty Aggregation**
<div style="padding-left: 20px;" markdown="1">
Predicted energy uncertainty should be aggregated by [summing in quadrature](https://en.wikipedia.org/wiki/Pythagorean_addition)
</div>

</div>

#### **1.1.4 Location**
<div style="padding-left: 20px;" markdown="1">
There are two options for location data, but [Daily DQ 1.1.4.1](#1141-latitude-and-longitude) is greatly preferred.

##### **1.1.4.1 Latitude and Longitude**  ·  CalTRACK 2.1.4.1 {#1141-latitude-and-longitude}
<div style="padding-left: 20px;" markdown="1">
Latitude and longitude should be known to three decimal places
<br><span style="color: #888; font-size: 0.9em;">Note: CalTRACK 2.1.4.1 specifies four or more decimal places.</span>
</div>

##### **1.1.4.2 ZIP Code Tabulation Area (ZCTA)**  ·  CalTRACK 2.1.4.1.1
<div style="padding-left: 20px;" markdown="1">
If absolutely necessary, the centroid of the ZCTA may be used in place of latitude and longitude
</div>

</div>

#### **1.1.5 Non-Routine Events**
<div style="padding-left: 20px;" markdown="1">
Identifying and addressing non-routine events (NRE) is a best practice for making measurements, but is not required by OpenDSM.

##### **1.1.5.1 Net Metering Status Change**  ·  CalTRACK 2.2.6
<div style="padding-left: 20px;" markdown="1">
If a meter's net metering status changes ***during*** a period, the meter should be disqualified as an NRE. Negative meter data is indicative of net metering, but a meter may have an undersized system and remain positive at all datetimes.
</div>

##### **1.1.5.2 Electric Vehicle Status Change**  ·  CalTRACK 2.2.7
<div style="padding-left: 20px;" markdown="1">
If a meter's electric vehicle charging status changes ***during*** a period, the meter should be disqualified as an NRE.
</div>

##### **1.1.5.3 Heuristic-Based Identification**  ·  CalTRACK 2.3.6
<div style="padding-left: 20px;" markdown="1">
Observed values which fall outside of $[Q_1 - 3\times IQR, Q_3 + 3\times IQR]$, a modification of the general [1.5 IQR Rule](https://en.wikipedia.org/wiki/Interquartile_range), can be investigated for disqualification as an NRE.
</div>

</div>

</div>

---

### **1.2 Common**
<div style="padding-left: 20px;" markdown="1">
Common data sufficiency are prerequisites to both the baseline and reporting data sufficiency checks.

#### **1.2.1: Blackout Exclusion**  ·  CalTRACK 2.2.5
<div style="padding-left: 20px;" markdown="1">
Blackout period data should not be included in either the baseline or reporting periods.
</div>

#### **1.2.2: Data Exists**
<div style="padding-left: 20px;" markdown="1">
Input is not an empty dataset
</div>

#### **1.2.3: Datetime Time Zone-Aware**  ·  CalTRACK 2.1.6
<div style="padding-left: 20px;" markdown="1">
Datetimes must include time zone information and all data must have the same time-zone information
</div>

#### **1.2.4: Duplicate Data**  ·  CalTRACK 2.3.2
<div style="padding-left: 20px;" markdown="1">
No duplicated datetimes are allowed
</div>

#### **1.2.5: High-Frequency Data**  ·  CalTRACK 2.2.2.1
<div style="padding-left: 20px;" markdown="1">
At least 50% of high-frequency data must be valid. Missing data must be imputed for aggregations
</div>

#### **1.2.6: Missing Temperature**  ·  CalTRACK 2.2.1.3
<div style="padding-left: 20px;" markdown="1">
Missing temperature data will result in the entire datetime to be considered missing
</div>

#### **1.2.7: Minimum Daily Temperature Coverage**  ·  CalTRACK 2.2.1.2
<div style="padding-left: 20px;" markdown="1">
The percentage of valid days (days with greater than 90% valid temperature data coverage) must be greater than 90%
</div>

#### **1.2.8: Minimum Daily Joint Coverage**  ·  CalTRACK 2.2.1.2
<div style="padding-left: 20px;" markdown="1">
The percentage of valid days (days with greater than 90% valid joint data coverage) must be greater than 90%
</div>

#### **1.2.9: Minimum Monthly Temperature Coverage**
<div style="padding-left: 20px;" markdown="1">
Each month in the period must have at least 90% valid temperature data for all datetimes
</div>

</div>

---

### **1.3 Baseline Period**
<div style="padding-left: 20px;" markdown="1">
The baseline period must meet both the [Common](#12-common) and the baseline period sufficiency criteria.

#### **1.3.1: Baseline Length**
<div style="padding-left: 20px;" markdown="1">
The baseline length must be of an appropriate length

##### **1.3.1.1: Maximum Baseline Length**  ·  CalTRACK 2.2.1.1 {#1311-maximum-baseline-length}
<div style="padding-left: 20px;" markdown="1">
The baseline length must be less than 366 days. This is 1 day longer than a standard year to account for leap years
</div>

##### **1.3.1.2: Minimum Baseline Length**  ·  CalTRACK 2.2.1.2
<div style="padding-left: 20px;" markdown="1">
The baseline length must be at least the floor of 90% of the maximum baseline length as defined in [Daily DQ 1.3.1.1](#1311-maximum-baseline-length), floor(366*0.9) = 329 days
</div>

##### **1.3.1.3: Full Datetime Range**  ·  CalTRACK 2.2.1.1
<div style="padding-left: 20px;" markdown="1">
A full year of datetimes should be provided
</div>

</div>

#### **1.3.2: Negative Gas Data**  ·  CalTRACK 2.3.5
<div style="padding-left: 20px;" markdown="1">
For gas data, observed values may not be less than 0
</div>

#### **1.3.3: Minimum Daily Observed Coverage**  ·  CalTRACK 2.2.1.2
<div style="padding-left: 20px;" markdown="1">
The percentage of valid days (days with greater than 90% valid observed data coverage) must be greater than 90%
</div>

</div>

---

### **1.4 Reporting Period**
<div style="padding-left: 20px;" markdown="1">
The reporting period must meet the [Common](#12-common) sufficiency criteria.
</div>

---

## **2. Model Sufficiency**
A fit daily model must meet the [CVRMSE](site:documentation/general_concepts/#cvrmse) criterion to be qualified for measurement.

### **2.1 CVRMSE**
<div style="padding-left: 20px;" markdown="1">

#### **2.1.1: Maximum CVRMSE**
<div style="padding-left: 20px;" markdown="1">
The adjusted CVRMSE must be less than or equal to 1.0
</div>

#### **2.1.2: Minimum CVRMSE**
<div style="padding-left: 20px;" markdown="1">
The adjusted CVRMSE must be greater than or equal to 0.0
</div>

</div>

---
