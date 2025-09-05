# Sufficiency Criteria

Most sufficiency criteria derive their origins from the CalTRACK specifications. Old reference numbers to the CalTRACK specifications are no longer valid and the new reference numbers should be used when discussing OpenDSM. A remnant of the old CalTRACK specifications is that there are two types of checks performed, disqualification and warnings. Disqualification is a hard line that means meters should not be used for measurement. A warning is purely for experts to take a deeper look at the data to possibly disqualify them. Only explicit disqualifications will be defined herein.

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

##### **1.1.1.2 Baseline Period**
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
Units can be critically import to model performance. Convert your units accordingly.

##### **1.1.2.1 Temperature**
<div style="padding-left: 20px;" markdown="1">
Temperature data should in Fahrenheit
</div>

##### **1.1.2.1 Consumption/Usage**
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

#### **1.1.4 Electric-Only Criteria**
<div style="padding-left: 20px;" markdown="1">

##### **1.1.4.1 Net Metering**
<div style="padding-left: 20px;" markdown="1">
A meter's net metering status should be known during all periods. If the status changes ***during*** a period, the meter should be disqualified. Negative meter data is indicative of net metering, but a meter may have an undersized system and remain positive at all datetimes.
</div>

##### **1.1.4.2 Electric Vehicle**
<div style="padding-left: 20px;" markdown="1">
A meter's elecric vehicle charging status should be known during all periods. If the status changes ***during*** a period, the meter should be disqualified.
</div>

</div>

#### **1.1.5 Location**
<div style="padding-left: 20px;" markdown="1">
There are two options for location data, but [Billing DQ 1.1.5.1](#1151-latitude-and-longitude) is greatly preferred.

##### **1.1.5.1 Latitude and Longitude**
<div style="padding-left: 20px;" markdown="1">
Latitude and longitude should be known to three decimal places
</div>

##### **1.1.5.2 ZIP Code Tabulation Area (ZCTA)**
<div style="padding-left: 20px;" markdown="1">
If absolutely necessary, the centroid of the ZCTA may be used in place of latitude and longitude
</div>

</div>

</div>

---

### **1.2 Common**
<div style="padding-left: 20px;" markdown="1">
Common data sufficiency are prerequisites to both the baseline and reporting data sufficiency checks.

#### **1.2.1: Blackout Exclusion**
<div style="padding-left: 20px;" markdown="1">
Blackout period data should not be included in either the baseline or reporting periods.
</div>

#### **1.2.2: Data Exists**
<div style="padding-left: 20px;" markdown="1">
Input is not an empty dataset
</div>

#### **1.2.3: Datetime Time Zone-Aware**
<div style="padding-left: 20px;" markdown="1">
Datetimes must include time zone information and all data must have the same time-zone information
</div>

#### **1.2.4: Duplicate Data**
<div style="padding-left: 20px;" markdown="1">
No duplicated datetimes are allowed
</div>

#### **1.2.5: High-Frequency Data**
<div style="padding-left: 20px;" markdown="1">
At least 50% of high-frequency data must be valid. Missing data must be imputed for aggregations
</div>

#### **1.2.6: Billing Period Length**
<div style="padding-left: 20px;" markdown="1">

##### **1.2.6.1: Minimum Billing Period**
<div style="padding-left: 20px;" markdown="1">
All billing periods must be greater or equal than 25 days
</div>

##### **1.2.6.2: Maximum Billing Period**
<div style="padding-left: 20px;" markdown="1">
All billing periods must be less than or equal to 35 days (if monthly cadence) or 70 days (if bimonthly cadence)
</div>

##### **1.2.6.3: Combining Estimated Periods**
<div style="padding-left: 20px;" markdown="1">
Estimated periods should be combined with the next period up to a 70 day limit. Estimated periods are considered as missing data for the purpose of determining data sufficiency.
</div>

</div>

#### **1.2.7: Missing Temperature**
<div style="padding-left: 20px;" markdown="1">
Missing temperature data will result in the entire datetime to be considered missing
</div>

#### **1.2.8: Minimum Daily Temperature Coverage**
<div style="padding-left: 20px;" markdown="1">
The percentage of valid days (days with greater than 90% valid temperature data coverage) must be greater than 90%
</div>

#### **1.2.9: Minimum Daily Joint Coverage**
<div style="padding-left: 20px;" markdown="1">
The percentage of valid days (days with greater than 90% valid joint data coverage) must be greater than 90%
</div>

#### **1.2.10: Minimum Monthly Temperature Coverage**
<div style="padding-left: 20px;" markdown="1">
Each month in the period must have at least 90% valid temperature data for all datetimes
</div>

</div>

---

### **1.3 Baseline Period**
<div style="padding-left: 20px;" markdown="1">
The baseline period must meet both the [Common](#22-common) and the baseline period sufficiency criteria.

#### **1.3.1: Baseline Length**
<div style="padding-left: 20px;" markdown="1">
The baseline length must be of an appropriate length

##### **1.3.1.1: Maximum Baseline Length**
<div style="padding-left: 20px;" markdown="1">
The baseline length must be less than 366 days. This is 1 day longer than a standard year to account for leap years
</div>

##### **1.3.1.2: Minimum Baseline Length**
<div style="padding-left: 20px;" markdown="1">
The baseline length must be at least the floor of 90% of the maximum baseline length as defined in [Billing DQ 1.3.1.1](#1311-maximum-baseline-length), floor(366*0.9) = 329 days
</div>

##### **1.3.1.3: Full Datetime Range**
<div style="padding-left: 20px;" markdown="1">
A full year of datetimes should be provided
</div>

</div>

#### **1.3.2: Negative Gas Data**
<div style="padding-left: 20px;" markdown="1">
For gas data, observed values may not be less than 0
</div>

#### **1.3.3: Minimum Daily Observed Coverage**
<div style="padding-left: 20px;" markdown="1">
The percentage of valid days (days with greater than 90% valid observed data coverage) must be greater than 90%
</div>

</div>

---

### **1.4 Reporting Period**
<div style="padding-left: 20px;" markdown="1">
The reporting period must meet the [Common](#22-common) sufficiency criteria.
</div>

---

## **2. Model Sufficiency**
A fit billing model must meet either [CVRMSE](site:documentation/general_concepts/#cvrmse) <span style="color: orange;">or</span> [PNRMSE](site:documentation/general_concepts/#pnrmse) criteria to be qualified for measurement.

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

### **2.2 PNRMSE**
<div style="padding-left: 20px;" markdown="1">

#### **2.2.1: Maximum PNRMSE**
<div style="padding-left: 20px;" markdown="1">
The adjusted PNRMSE must be less than or equal to 1.6
</div>

</div>

---

<div style="text-align: right; font-size: 0.9em; color: #888; margin-top: 40px;">
    OpenDSM v1.2
</div>