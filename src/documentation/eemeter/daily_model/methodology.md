The daily model is trained using daily energy usage intervals and predicts in daily intervals.

One of the key requirements of the daily model is to be able to disaggregate daily heating and cooling loads.

## Model Theory

### Model Shape and Balance Points

The daily model, at its core, utilizes a piecewise linear regression model that predicts energy usage relative to temperature. The model determines temperature balance points at which energy usage starts changing relative to temperature.

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/daily_model/basic_model.png" alt="Daily model", style="width:85%">
</div>

#### Nomenclature

- **Balance Points**: Outdoor temperature thresholds beyond which heating and cooling effects are observed.
- **Heating and Cooling Coefficients**: Rate of increase of energy use per change in temperature beyond the balance points.
- **Temperature Independent Load**: The regression intercept (height of the flat line in the diagram).

#### Model Archetypes

Based on the site behavior, there are four different model types that may be generated:

- Heating and Cooling Loads
- Heating Only Load
- Cooling Only Load
- Temperature Independent Load

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/common/model_archetypes.png" alt="Different model archetypes", style="width:75%">
</div>

#### Smooth Transitions

The daily model is designed to allow smooth transitions between model regimes. There are many reasons why a smooth transition might be favorable, but one example of this is inlet water temperature into a water heater. In this example, more energy will be required as the temperature decreases, which will be a smooth transition.

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/daily_model/smoothed_winter.png" alt="Smooth winter transition", style="width:85%">
</div>

#### Robust, Adaptive Outlier Downweighting

While the majority of the time Sum of Squares Error (SSE) is the optimal metric to minimize to obtain the best model, there are instances where it is less effective at creating predictive models in data containing influential outliers. The daily model handles these outliers by downweighting them using a robust, adaptive loss function and procedure.

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/daily_model/outliers.png" alt="Downweighted outliers", style="width:85%">
</div>

#### Model Fit

When the model is fit, each site will receive its own unique model fit and coefficients. The general model fitting process is as follows:

1. Balance points are estimated with a global optimization algorithm.
2. Sum of Squares Error (SSE) is minimized with Lasso inspired penalization.
3. The best model type is determined (ex. cooling load only model) using the penalized SSE.

The Lasso inspired penalization means that increased model complexity must be justified by decreased SSE and balanced against these general rules:

- Slopes are pushed to 0
- Intercept is pushed to 0
- Balance points are pushed together
- Balance points are pushed towards the nearest edge (most extreme temperature)
- Smoothing parameter is pushed to 0 (no smoothing)

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/daily_model/lasso_penalization.png" alt="Lasso penalization", style="width:85%">
</div>

### Model Splits

The process described above is effective but may have shortcomings in real life data if energy usage changes fundamentally during different time periods.

For example, what if a site is more populated during a particular season (for example, a Summer House or Ski Lodge) or during weekdays (for example, offices and most homes). This may result in models that fail to accurately predict energy usage because they are trying to account for all time periods at once.

<div style="display: flex; justify-content: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/daily_model/season_problems.png" alt="Seasonal misalignment" style="max-width: 50%">
    <img src="site:assets/images/eemeter/daily_model/weekday_problems.png" alt="Weekday misalignment" style="max-width: 50%">
</div>

To combat this, the model will create "splits" that will store independent submodels for different seasons or weekday/weekend combinations, but only if necessary. 

The general process is as follows:

1. Create submodels using all possible splits of season/weekday|weekend.
2. Calculate modified BIC (Bayesian Information Criterion) for each preliminary combination.
3. Select best combination with the smallest BICmod.

This provides a standardized process for splitting the model to better predict energy usage by certain time periods (if the benefit outweighs the additional model complexity).

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/daily_model/split_model_season.png" alt="Model split by season", style="width:85%">
</div>

## Real Data Example

The daily model is a deceptively complex model capable of handling some complex situations. 

In this real example, we have three models:

1. Summer/shoulder weekday model: a smoothed model with heating, temperature independent, and cooling regions.
2. Winter weekday model: a model with heating and temperature independent regions that relies on adaptive downweighting (see the influential points at 0 kWh/day)
3. Weekend model: an all-season model with significant usage decrease compared to the weekday models.

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/daily_model/real_example.png" alt="Real world example", style="width:85%">
</div>

*For additional information and validation details, see [References](site:documentation/eemeter/daily_model/references/).

## Sufficiency Criteria

Most sufficiency criteria derive their origins from the CalTRACK specifications. Old reference numbers to the CalTRACK specifications are no longer valid and the new reference numbers should be used when discussing OpenDSM. A remnant of the old CalTRACK specifications is that there are two types of checks performed, disqualification and warnings. Disqualifications are a hard line that means meters should not be used for measurement. Warnings are purely for experts to take a deeper look at the data to possibly disqualify them. Only explicit disqualifications will be defined herein.

Many sufficiency criteria are duplicated between the various models, but for the sake of completeness they will be included in definitions for all models. Unique sufficiency criteria will be designated with an **\***.

### Nomenclature

- Valid Data: Data which is not NULL, NaN, or otherwise empty
- Joint Data: The combination of all inputs

### Data Sufficiency

#### Common
Common data sufficiency are prerequisites to both the baseline and reporting data sufficiency checks.

##### **2.1.1: Blackout Exclusion**
Blackout period data should not be included in either the baseline or reporting periods.

##### **2.1.2: Data Exists**
Input is not an empty dataset

##### **2.1.3: Datetime Time Zone-Aware**
Datetimes must include time zone information and all data must have the same time-zone information

##### **2.1.4: Duplicate Data**
No duplicated datetimes are allowed

##### **2.1.5: High-Frequency Data**
At least 50% of high-frequency data must be valid. Missing data must be imputed for aggregations 

##### **2.1.6: Missing Temperature**
Missing temperature data will result in the entire datetime to be considered missing

##### **2.1.7: Minimum Monthly Temperature Coverage**
Each month in the period must have at least 90% valid temperature data for all datetimes

##### **2.1.8: Minimum Daily Temperature Coverage**
The percentage of valid days (days with greater than 90% valid temperature data coverage) must be greater than 90%

##### **2.1.9: Minimum Daily Joint Coverage**
The percentage of valid days (days with greater than 90% valid joint data coverage) must be greater than 90%

#### Baseline Period
The baseline period must meet both the common and the baseline period sufficiency criteria.

##### **2.2.1: Baseline Length**
The baseline length must be of an appropriate length

###### **2.2.1.1: Maximum Baseline Length**
The baseline length must be less than 366 days. This is 1 day longer than a standard year to account for leap years

###### **2.2.1.2: Minimum Baseline Length**
The baseline length must be at least the floor of 90% of the maximum baseline length as defined in [Daily DQ 2.2.1.1](#2211-maximum-baseline-length), floor(366*0.9) = 329 days

###### **2.2.1.3: Full Datetime Range**
A full year of datetimes should be provided

##### **2.2.2: Negative Gas Data**
For gas data, observed values may not be less than 0

##### **2.2.3: Minimum Daily Observed Coverage**
The percentage of valid days (days with greater than 90% valid observed data coverage) must be greater than 90%

#### Reporting Period
The reporting period must meet the common sufficiency criteria.

#### User Responsibilities
There are some checks that should be performed which cannot be performed within the confines of the data or model classes, but are critical for valid measurements

##### Period Definition

###### **2.3.1.1 Blackout Period**
The blackout period should be known, or at least estimated, and excluded from being included in the data.

###### **2.3.1.2 Baseline Period**
The baseline period should be one year immediately prior to the blackout period

###### **2.3.1.3 Reporting Period**
The reporting period should be one year immediately following the blackout period

##### **2.3.2 Units**
Units can be critically import to model performance. Convert your units accordingly.

###### **2.3.2.1 Temperature**
Temperature data should in Fahrenheit

###### **3.2.2.1 Consumption/Usage**
Consumption data is expected to be in some kind of units of energy

##### **2.3.3 Net Metering**
A meter's net metering status should be known during all periods. If the status changes ***during*** a period, the meter should be disqualified. Negative meter data is indicative of net metering, but a meter may have an undersized system and remain positive at all datetimes. 

##### **2.3.4 Electric Vehicle**
A meter's elecric vehicle charging status should be known during all periods. If the status changes ***during*** a period, the meter should be disqualified.

##### **2.3.5 Location**
There are two options for location data, but [Daily DQ 2.3.6.1](#2361-latitude-and-longitude) is greatly preferred.

###### **2.3.6.1 Latitude and Longitude**
Latitude and longitude should be known to three decimal places

###### **2.3.6.2 ZIP Code Tabulation Area (ZCTA)**
If absolutely necessary, the centroid of the ZCTA may be used in place of latitude and longitude

##### **2.3.7 Model Results**

###### **2.3.7.1 Predicted Energy Aggregation**
Predicted energy can be aggregated through simple summation

###### **2.3.7.2 Predicted Energy Uncertainty Aggregation**
Predicted energy uncertainty should be aggregated by [summing in quadrature](https://en.wikipedia.org/wiki/Pythagorean_addition)

### Model Sufficiency
A fit daily model must meet ***either*** CVRMSE ***or*** PNRMSE criteria to be qualified for measurement.

#### CVRMSE

##### **2.4.1: Maximum CVRMSE**
The adjusted CVRMSE must be less than or equal to 1.0

##### **2.4.2: Minimum CVRMSE**
The adjusted CVRMSE must be greater than or equal to 0.0

#### PNRMSE

##### **2.5.1: Maximum PNRMSE**
The adjusted PNRMSE must be less than or equal to 1.6