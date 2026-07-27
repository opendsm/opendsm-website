# Sufficiency Criteria<br><div style="text-align: left; font-size: 0.5em; color: #888; margin-bottom: -2.3em;">CalTRACK 2.1 hourly methods</div>

The hourly model's data sufficiency criteria follow the
[CalTRACK 2.1 Methods](site:caltrack/methodology/), Section 2 (Data Management); the numbers below are
the CalTRACK 2.1 section numbers, with further detail in the
[Technical Appendix](site:caltrack/technical_appendix/).

Two kinds of check exist: a **disqualification** is a hard line (the meter should not be used for
measurement), while a **flag** asks an expert to take a closer look.

---

## 2.1 Data Inputs

The inputs required to apply the hourly model to a site. These represent the "ideal". Additional requirements follow in Section 2.2.

<div style="padding-left: 20px;" markdown="1">

#### **2.1.1 Energy consumption (meter) data**
<div style="padding-left: 20px;" markdown="1">
- **2.1.1.1** Periods of usage and usage during those periods (AMI data).
- **2.1.1.2** May be combined from multiple sources or accounts.
- **2.1.1.3** Must be in units of energy consumption, not supplied volume.
- **2.1.1.4** Subject to the constraints in 2.2.
- **2.1.1.5** A flag or directional indicator for the presence of net metering. 
</div>

#### **2.1.2 Candidate weather stations**
<div style="padding-left: 20px;" markdown="1">
- **2.1.2.1** Latitude and longitude coordinates.
- **2.1.2.2** Climate-zone information, if needed in weather-station matching (see 2.4).
- **2.1.2.3** IECC climate zone.
- **2.1.2.4** IECC moisture regime.
- **2.1.2.5** Building America climate zone.
- **2.1.2.6** California Building Climate Zone Area (if the site is in California).
- **2.1.2.7** Observed dry-bulb temperature data, subject to the constraints in 2.2.
</div>

#### **2.1.3 Project data**
<div style="padding-left: 20px;" markdown="1">
- **2.1.3.1** Dates:
    - **2.1.3.1.1** Project start date (the start of the intervention period).
    - **2.1.3.1.2** Intervention completion date (the start of the reporting period).
    - **2.1.3.1.3** Intervention active date (for interventions without a defined start, e.g. behavioral).
    - **2.1.3.1.4** Baseline period end (the project start date or the intervention active date).
</div>

#### **2.1.4 Building site data**
<div style="padding-left: 20px;" markdown="1">
- **2.1.4.1** Latitude and longitude coordinates, to four decimal places or more.
    - **2.1.4.1.1** In the absence of a high-quality geocode, the centroid of the ZIP Code Tabulation
      Area (ZCTA) may be used instead.
</div>

#### **2.1.5 Climate zone**
<div style="padding-left: 20px;" markdown="1">
The site climate zone (see 2.1.2.2).
</div>

#### **2.1.6 Time zone**
<div style="padding-left: 20px;" markdown="1">
The site time zone.
</div>

</div>

---

## 2.2 Data Constraints

<div style="padding-left: 20px;" markdown="1">

#### **2.2.1 Missing values and baseline sufficiency**
<div style="padding-left: 20px;" markdown="1">
- **2.2.1.1** Consumption and temperature data sufficient for a 365-day baseline period.
- **2.2.1.2** For the hourly methods, no minimum baseline period length is required; however, baseline
  consumption data must be available for over 90% of the hours in the same calendar month and in each
  of the previous and following calendar months.
- **2.2.1.3** Data is considered missing if marked NULL, NaN, or similar.
- **2.2.1.4** Values of 0 are considered missing for electricity data, but not gas data.
</div>

#### **2.2.2 High-frequency data**
<div style="padding-left: 20px;" markdown="1">
- **2.2.2.1** When aggregating higher-frequency interval data (e.g. 15-minute) up to hourly usage, no
  more than 50% of values may be missing; missing values are filled with the average of non-missing
  values.
- **2.2.2.3** The same 50% limit applies when aggregating higher-frequency temperature data to hourly.
</div>

#### **2.2.4 Hourly temperature sufficiency**
<div style="padding-left: 20px;" markdown="1">
- **2.2.4.1** Temperature may not be missing for more than six consecutive hours; up to six
  consecutive missing hours may be linearly interpolated.
</div>

#### **2.2.5 Data beyond the period**
<div style="padding-left: 20px;" markdown="1">
Data spanning beyond the baseline period should not be used in analysis.
</div>

#### **2.2.6 Net-metering status change**
<div style="padding-left: 20px;" markdown="1">
Exclude projects whose net-metering status changes during the baseline period.

- **2.2.6.1** Exception: future efforts may allow sub-meter data to back out on-site generation; this
  data is not currently readily obtained.
</div>

#### **2.2.7 Electric-vehicle charging**
<div style="padding-left: 20px;" markdown="1">
Flag projects where electric-vehicle charging is installed during the baseline period.
</div>

</div>

---

## 2.3 Data Quality

<div style="padding-left: 20px;" markdown="1">

#### **2.3.1 Impossible dates**
<div style="padding-left: 20px;" markdown="1">
- **2.3.1.1** For billing analysis, an impossible day-of-month (e.g. Jan 32) uses the first of the month.
- **2.3.1.2** An impossible month or year is flagged and removed; check for mis-coding (e.g. 2015 → 2051).
</div>

#### **2.3.2 Duplicate records**
<div style="padding-left: 20px;" markdown="1">
- **2.3.2.1** Combine versions into a single series, dropping duplicates; conflicting records flag
  possible multiple meters or sub-meters, whose usage may then be aggregated.
</div>

#### **2.3.3 Time zones**
<div style="padding-left: 20px;" markdown="1">
Meter and temperature data must use matching, correct time zones and daylight-savings handling.
</div>

#### **2.3.4 NOAA weather**
<div style="padding-left: 20px;" markdown="1">
Convert to hourly by near-interpolation (60-minute limit), then mean downsampling.
</div>

#### **2.3.5 Negative values**
<div style="padding-left: 20px;" markdown="1">
Negative meter values are flagged for review as a possible indicator of unreported net metering.
</div>

#### **2.3.6 Extreme values**
<div style="padding-left: 20px;" markdown="1">
Usage more than three interquartile ranges above the median is flagged as an outlier for manual review.
</div>

#### **2.3.7 Dataset audit**
<div style="padding-left: 20px;" markdown="1">
Audit dataset completeness against expected site, meter, and project counts.
</div>

#### **2.3.8 Frequency**
<div style="padding-left: 20px;" markdown="1">
Roll up data not provided at the expected frequency.
</div>

</div>

---

## 2.4 Matching a Site to a Weather Station

<div style="padding-left: 20px;" markdown="1">

#### **2.4.1 Closest qualifying station**
<div style="padding-left: 20px;" markdown="1">
Use the closest weather station within the climate zone that meets CalTRACK sufficiency requirements.

- **2.4.1.1** If there are no stations within that climate zone, fall back to the closest station with
  complete data.
</div>

#### **2.4.2 Distant matches**
<div style="padding-left: 20px;" markdown="1">
Matches farther than 200 km should be flagged for review.
</div>

</div>

---

## 3.5 Reporting-Period Sufficiency

The reporting period follows the same data-management and quality requirements as the baseline, with
these reporting-specific rules.

<div style="padding-left: 20px;" markdown="1">

#### **3.5.1 Missing temperature values**
<div style="padding-left: 20px;" markdown="1">
A day missing temperature has its corresponding consumption value masked.
</div>

#### **3.5.2 Missing consumption values**
<div style="padding-left: 20px;" markdown="1">
A day missing consumption has its corresponding counterfactual value masked.
</div>

#### **3.5.3 Counterfactual with missing temperature**
<div style="padding-left: 20px;" markdown="1">
Counterfactual usage is not calculated when daily temperature data is missing.
</div>

#### **3.5.4 Avoided energy with missing consumption**
<div style="padding-left: 20px;" markdown="1">
Avoided energy use is not calculated when consumption data is missing.
</div>

#### **3.5.6 Net-metering status change**
<div style="padding-left: 20px;" markdown="1">
Exclude projects whose net-metering status changes during the reporting period.
</div>

</div>
