In this example, we'll walk through creating a Billing Model and predicting usage with it.

You can find a working example in the [Example Code](#example-code) at the bottom of the page.

<span style="font-size: 0.9em;">
1) This example makes use of Matplotlib. Matplotlib is not a required dependency of OpenDSM.<br>
2) OpenDSM 1.0 requires `pandas<3`.<br>
3) The example data is downloaded from the OpenDSM repository (see the fetch step below).
</span>

### Imports

```python
import numpy as np
import matplotlib.pyplot as plt

import opendsm as odsm
from opendsm import eemeter as em
```

### Loading data

The essential inputs to OpenDSM library functions are the following:

1. Meter baseline data named `observed`
2. Meter reporting data named `observed`
3. Temperature data from a nearby weather station for both named `temperature`
4. All data is expected to have a timezone-aware datetime index or column named `datetime`

Users of the library are responsible for obtaining and formatting this data (to get weather data, see [EEweather](https://github.com/opendsm/eeweather), which helps perform site to weather station matching and can pull and cache temperature data directly from public (US) data sources).

We utilize data classes to store meter data, perform transforms, and validate the data to ensure data compliance. The inputs into these data classes can either be [pandas](https://pandas.pydata.org/) `DataFrame` if initializing the classes directly or `Series` if initializing the classes using `.from_series`.

The test data contained within the OpenDSM library is derived from [NREL ComStock](https://comstock.nrel.gov/) simulations.

If working with your own data instead of these samples, please refer directly to the excellent pandas documentation for instructions for loading data (e.g., [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)).

#### Important notes about data
- *These models were developed and tested using temperature in units of °Fahrenheit. Please convert your temperatures accordingly*
- *It is expected that all data is trimmed to its appropriate time period (baseline and reporting) and does not contain extraneous datetimes*
    - *The exception to this is that a billing period is assumed to start on the datetime in which it has a value and to end 1 day prior to the next datetime with a value with 1 final empty datetime signifying the end of the year resulting in 13 total datetimes for monthly billing data and 7 for bimonthly billing data*

The built-in `load_test_data` utility reads bundled example data. In OpenDSM 1.0 it looks for that data
in the package's data directory, so fetch the files into place once:

```python
import requests
from opendsm.common import test_data

test_data.data_dir.mkdir(parents=True, exist_ok=True)
for fname in ["hourly_data_2.parquet", "attribution.txt"]:
    dest = test_data.data_dir / fname
    if not dest.exists():
        r = requests.get(f"https://raw.githubusercontent.com/opendsm/opendsm/v1.0.0/data/{fname}")
        r.raise_for_status()
        dest.write_bytes(r.content)
```

This function returns two dataframes of monthly billing electricity data, one for the baseline period and one for the reporting period.

```python
df_baseline, df_reporting = odsm.test_data.load_test_data("monthly_treatment_data")
```

If we inspect these dataframes, we will notice that there are 100 meters for you to experiment with, indexed by meter id and datetime.

```python
print(df_baseline)
```

??? Returns
    ```      
    id      datetime                   temperature       observed
    108618  2018-01-01 00:00:00-06:00    -2.384038  257406.539278
            2018-01-02 00:00:00-06:00     1.730000            NaN
            2018-01-03 00:00:00-06:00    13.087946            NaN
            2018-01-04 00:00:00-06:00     4.743269            NaN
            2018-01-05 00:00:00-06:00     4.130577            NaN
                                  ...          ...            ...
    120841  2018-12-27 00:00:00-06:00    52.010625            NaN
            2018-12-28 00:00:00-06:00    35.270000            NaN
            2018-12-29 00:00:00-06:00    29.630000            NaN
            2018-12-30 00:00:00-06:00    34.250000            NaN
            2018-12-31 00:00:00-06:00    43.311250            NaN
    ```

Notice that there is only a single observed value and the rest are NaN. This is because these are daily average temperatures and only 12 data points out of the year have observed values. This is prior to the observed averaging that will take place later.

To simplify things, we will filter down to a single meter for the rest of the example. Let's filter down to the 15th id.

```python
n = 15

id = df_baseline.index.get_level_values(0).unique()[n]

df_baseline_n = df_baseline.loc[id]
df_reporting_n = df_reporting.loc[id]
```

If we inspect one of these dataframes, we will now notice that only a single meter is present with 365 days of data in each dataframe. 

```python
print(df_baseline_n)
```

??? Returns
    ```
    datetime                   temperature       observed
    2018-01-01 00:00:00-06:00   -10.045000  143527.500929
    2018-01-02 00:00:00-06:00    -4.712500            NaN
    2018-01-03 00:00:00-06:00    11.352500            NaN
    2018-01-04 00:00:00-06:00     0.972500            NaN
    2018-01-05 00:00:00-06:00     3.147500            NaN
    ...                                ...            ...
    2018-12-27 00:00:00-06:00    46.760000            NaN
    2018-12-28 00:00:00-06:00    35.323125            NaN
    2018-12-29 00:00:00-06:00    26.386250            NaN
    2018-12-30 00:00:00-06:00    28.463750            NaN
    2018-12-31 00:00:00-06:00    40.345250            NaN
    ```

Also notice the general structure of these dataframes for a single meter. We have three columns:

1. A timezone-aware datetime index.
2. A temperature column (float) in °F (be sure to convert any other units to °F first) and must be at least daily interval data.
3. Observed meter usage (float). The example here is electricity data in kWh, but it could also be gas data.

Note that billing data is reversed from a customer perspective. From a customer perspective, you pay for the month you used energy and so the bill is for the month prior. To model this, the start date should have the usage for a given month.

We can stop to plot this data to get a better understanding of the general behavior of this meter.

```python
fig, ax1 = plt.subplots(figsize=(7, 5))

color = 'tab:blue'
ax1.set_xlabel('Datetime')
ax1.set_ylabel('Observed Usage', color=color)
ax1.plot(df_baseline_n.index, df_baseline_n['observed'], label='Observed Usage', color=color, marker='o', linestyle='-')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Temperature (F)', color=color)
ax2.plot(df_baseline_n.index, df_baseline_n['temperature'], label='Temperature (F)', color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.suptitle('Observed Usage and Temperature in the Baseline Period')
fig.tight_layout()
plt.show()
```

??? Returns
    <div style="text-align: center; margin-top: 30px">
        <img src="site:assets/images/eemeter/billing_model/example/baseline_data_billing.png" alt="Billing Baseline Data">
    </div>

If we observe the data we can see a full year of data with observed usage peaking in the winter and lowering in the summer with warmer temperatures. It's clear that this site is located in a colder climate and uses more electricity in the winter.

### Loading Data into EEmeter Data Objects

With our sample data loaded into dataframes, we can create our Baseline and Reporting Data objects. Note that only the baseline period is needed to fit a model, but we will use our reporting period data to predict against.

```python
baseline_data = em.BillingBaselineData(df_baseline_n, is_electricity_data=True)
reporting_data = em.BillingReportingData(df_reporting_n, is_electricity_data=True)
```

These classes are critical to ensure standardized data loaded into the model. As with the daily model, these classes scan the data to check for data sufficiency and other criteria that might cause a model to be disqualified (unable to build a model of sufficient integrity). 

In the case of the billing model, these classes also perform the observed averaging over the billing period. Let's see what this looks like.

```python
print(baseline_data.df)
```

??? Returns
    ```
    datetime                   season weekday_weekend  temperature     observed
    2018-01-01 00:00:00-06:00  winter         weekday   -10.045000  4629.919385
    2018-01-02 00:00:00-06:00  winter         weekday    -4.712500  4629.919385
    2018-01-03 00:00:00-06:00  winter         weekday    11.352500  4629.919385
    2018-01-04 00:00:00-06:00  winter         weekday     0.972500  4629.919385
    2018-01-05 00:00:00-06:00  winter         weekday     3.147500  4629.919385
    ...                           ...             ...          ...          ...
    2018-12-27 00:00:00-06:00  winter         weekday    46.760000  3312.268813
    2018-12-28 00:00:00-06:00  winter         weekday    35.323125  3312.268813
    2018-12-29 00:00:00-06:00  winter         weekend    26.386250  3312.268813
    2018-12-30 00:00:00-06:00  winter         weekend    28.463750  3312.268813
    2018-12-31 00:00:00-06:00  winter         weekday    40.345250  3312.268813
    ```

As these classes are derived from the daily data classes, season and weekday_weekend are still computed, but the biggest change from what we saw previously is that the observed column appears to be completely filled out. If you were to sum up the observed values over a given billing period it would equal the results of the input data. Let's see how this looks compared to the last plot.

```python
fig, ax1 = plt.subplots(figsize=(7, 5))

color = 'tab:blue'
ax1.set_xlabel('Datetime')
ax1.set_ylabel('Observed Usage', color=color)
ax1.plot(baseline_data.df.index, baseline_data.df['observed'], label='Observed Usage', color=color, linestyle='-')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Temperature (F)', color=color)
ax2.plot(baseline_data.df.index, baseline_data.df['temperature'], label='Temperature (F)', color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.suptitle('Observed Usage and Temperature in the Baseline Period')
fig.tight_layout()
plt.show()
```

??? Returns
    <div style="text-align: center; margin-top: 30px">
        <img src="site:assets/images/eemeter/billing_model/example/baseline_data_daily.png" alt="Billing Baseline Data Averaged">
    </div>

In this plot the observed usage is now continuous in time with discontinuities where the billing periods change.

With data classes successfully instantiated, we can also check for any disqualifications or warnings before moving on to the model fitting step.

```python
print(f"Disqualifications: {baseline_data.disqualification}")
print(f"Warnings:          {baseline_data.warnings}")
```

??? Returns
    ```
    Disqualifications: []
    Warnings:          [EEMeterWarning(qualified_name=eemeter.sufficiency_criteria.unable_to_confirm_daily_temperature_sufficiency)]
    ```

From this, we can see that no disqualifications are present but there are some warnings to be aware of as we proceed. Warnings will not stop us from creating a model.

### Creating the Model

The billing model follows the general process of:

1. Initialize
2. Fit
3. Predict

We can do this easily as follows:

```python
billing_model = em.BillingModel()
billing_model.fit(baseline_data)
```

Before we move to predicting against a dataframe, we can actually use the built in plot function (requiring Matplotlib) to plot the performance of the model against the provided data.

```python
billing_model.plot(baseline_data)
```

??? Returns
    <div style="text-align: center; margin-top: 30px">
        <img src="site:assets/images/eemeter/billing_model/example/daily_baseline_vs_model.png" alt="Daily Baseline Observed vs. Model">
    </div>

It's not always very intuitive to input billing data and then to see daily plots, so the plot function has an optional input where you can specify `monthly` or `bimonthly` to aggregate to the specified interval.

```python
billing_model.plot(baseline_data, aggregation="monthly")
```

??? Returns
    <div style="text-align: center; margin-top: 30px">
        <img src="site:assets/images/eemeter/billing_model/example/billing_baseline_vs_model.png" alt="Monthly Baseline Observed vs. Model">
    </div>

While it might initially be concerning that this model does not appear to look like any of the [Model Archetypes](site:documentation/eemeter/billing_model/methodology/#model-archetypes), remember that this is utilizing the daily model under the hood. We've found through extensive testing that this model is more accurate than a CalTRACK model that does follow those model archetypes on a billing interval basis ([References pg. 28](site:documentation/eemeter/billing_model/references/)).

We can also use this function to plot the model prediction against the reporting period as follows:

```python
billing_model.plot(reporting_data, aggregation="monthly")
```

??? Returns
    <div style="text-align: center; margin-top: 30px">
        <img src="site:assets/images/eemeter/billing_model/example/billing_reporting_vs_model.png" alt="Monthly Reporting Observed vs. Model">
    </div>

In this plot we can see that the site is using significantly less energy in colder temperatures compared to the model / baseline period. Perhaps this site installed an efficiency intervention that saves energy in colder temperatures?

### Predicting with the Model and Calculating Savings

With our fit model, we can now predict across a given reporting period. The billing model predict method has the same functionality as the plot function. Let's skip straight to using that.

```python
df_results = billing_model.predict(reporting_data, aggregation="monthly")
print(df_results.head())
```

??? Returns
    ```                             
    datetime                     season  temperature      observed      predicted  predicted_unc  heating_load  cooling_load  model_split model_type
    2019-01-01 00:00:00-06:00    winter    23.684855  83259.561689  113204.189203    4816.317005  41972.011102           0.0  fw-su_sh_wi   hdd_tidd
    2019-02-01 00:00:00-06:00    winter    32.858562  59500.977283   94352.449401    4577.340634  30013.707891           0.0  fw-su_sh_wi   hdd_tidd
    2019-03-01 00:00:00-06:00  shoulder    37.632207  59374.674004   99912.353102    4816.317005  28680.175001           0.0  fw-su_sh_wi   hdd_tidd
    2019-04-01 00:00:00-05:00  shoulder    45.590826  55628.416668   89349.469105    4737.997688  20415.103201           0.0  fw-su_sh_wi   hdd_tidd
    2019-05-01 00:00:00-05:00  shoulder    72.356294  67624.123278   71439.541663    4816.317005    207.363562           0.0  fw-su_sh_wi   hdd_tidd
    ```

From here, we can easily calculate savings by subtracting observed usage from predicted usage.

```python
df_results['savings'] = df_results['predicted'] - df_results['observed']
print(f"Predicted Usage (kWh):  {round(df_results['predicted'].sum(), 2)}")
print(f"Observed Usage (kWh):   {round(df_results['observed'].sum(), 2)}")
print(f"Savings (kWh):          {round(df_results['savings'].sum(), 2)}")
```

??? Returns
    ```
    Predicted Usage (kWh):  1038677.49
    Observed Usage (kWh):    789252.05
    Savings (kWh):           249425.45
    ```

### Model Serialization

After creating a model, we can also serialize it for storage and read it back in later.

```python
saved_model = billing_model.to_json()
print(saved_model)
```

??? Returns
    ```python
    {"submodels": {"fw-su_sh_wi": {"coefficients": {"model_type": "hdd_tidd", "intercept": 2297.8121967963853, "hdd_bp": 67.72680897508171, "hdd_beta": -30.741956585408087, "hdd_k": null, "cdd_bp": null, "cdd_beta": null, "cdd_k": null}, "temperature_constraints": {"T_min": -10.045, "T_max": 83.00500000000001, "T_min_seg": 12.545, "T_max_seg": 81.155}, "f_unc": 865.0360703415635}}, "info": {"error": {"wRMSE": 419.24394756674826, "RMSE": 419.24394756674826, "MAE": 257.92400477097476, "CVRMSE": 0.14731511466233266, "PNRMSE": 0.17173849707207972}, "baseline_timezone": "America/Chicago", "disqualification": [], "warnings": [{"qualified_name": "eemeter.sufficiency_criteria.unable_to_confirm_daily_temperature_sufficiency", "description": "Cannot confirm that pre-aggregated temperature data had sufficient hours kept", "data": {}}]}, "settings": {"developer_mode": true, "algorithm_choice": "nlopt_sbplx", "initial_guess_algorithm_choice": "nlopt_direct", "full_model": "hdd_tidd_cdd", "allow_smooth_model": false, "alpha_minimum": -100, "alpha_selection": 2, "alpha_final_type": "last", "alpha_final": 2.0, "final_bounds_scalar": 1, "regularization_alpha": 0.001, "regularization_percent_lasso": 1, "segment_minimum_count": 10, "maximum_slope_oom_scalar": 2, "initial_step_percentage": 0.1, "split_selection": {"criteria": "bic", "penalty_multiplier": 0.24, "penalty_power": 2.061, "allow_separate_summer": false, "allow_separate_shoulder": false, "allow_separate_winter": false, "allow_separate_weekday_weekend": false, "reduce_splits_by_gaussian": false, "reduce_splits_num_std": null}, "season": {"january": "winter", "february": "winter", "march": "shoulder", "april": "shoulder", "may": "shoulder", "june": "summer", "july": "summer", "august": "summer", "september": "summer", "october": "shoulder", "november": "winter", "december": "winter", "options": ["summer", "shoulder", "winter"]}, "weekday_weekend": {"monday": "weekday", "tuesday": "weekday", "wednesday": "weekday", "thursday": "weekday", "friday": "weekday", "saturday": "weekend", "sunday": "weekend", "options": ["weekday", "weekend"]}, "uncertainty_alpha": 0.1, "cvrmse_threshold": 1}}
    ```

Afterwards, we can instantiate the model as follows:

```python
loaded_model = em.BillingModel.from_json(saved_model)
```

### Automatic Sufficiency Checking

Two of the core features of the OpenDSM Data and Model classes are automatic data sufficiency and model sufficiency checking. This ensures that only acceptable data and models are allowed to be used for making measurements. Let's show an example of how this works by introducing too many NaN values into the observed data of the prior example.

```python
# set rows 1:38 of observed to nan
df_baseline_n_dq = df_baseline_n.copy()
df_baseline_n_dq.loc[df_baseline_n_dq.index[1:38], "observed"] = np.nan

baseline_data_DQ = em.BillingBaselineData(df_baseline_n_dq, is_electricity_data=True)
print(f"Disqualifications: {baseline_data_DQ.disqualification}")
```

??? Returns
    ```python
    Disqualifications: [
        EEMeterWarning(qualified_name=eemeter.sufficiency_criteria.offcycle_reads_in_billing_monthly_data), 
        EEMeterWarning(qualified_name=eemeter.sufficiency_criteria.incorrect_number_of_total_days)
    ]
    ```

If this data were to try to be fit on it would return an error by default.

```python
try:
    billing_model = em.BillingModel().fit(baseline_data_DQ)
except Exception as e:
    print(f"Exception: {e}")
```

??? Returns
    ```python
    Exception: Can't fit model on disqualified baseline data
    ```

In some circumstances it may still be possible to fit a model on disqualified data for investigative purposes. This can be done by setting the `ignore_disqualification` flag to True.

```python
billing_model = em.BillingModel().fit(baseline_data_DQ, ignore_disqualification=True)
```

Please remember that enabling `ignore_disqualification` or making any changes to the model configuration fundamentally alters the model and such models are **not approved for measurement purposes**.

## Example Code
```python
import numpy as np
import matplotlib.pyplot as plt

import requests
import opendsm as odsm
from opendsm import eemeter as em
from opendsm.common import test_data

# OpenDSM 1.0's loader expects the example data in its data directory; fetch it once.
test_data.data_dir.mkdir(parents=True, exist_ok=True)
for fname in ["hourly_data_2.parquet", "attribution.txt"]:
    dest = test_data.data_dir / fname
    if not dest.exists():
        r = requests.get(f"https://raw.githubusercontent.com/opendsm/opendsm/v1.0.0/data/{fname}")
        r.raise_for_status()
        dest.write_bytes(r.content)

df_baseline, df_reporting = odsm.test_data.load_test_data("monthly_treatment_data")

n = 15

id = df_baseline.index.get_level_values(0).unique()[n]

df_baseline_n = df_baseline.loc[id]
df_reporting_n = df_reporting.loc[id]

baseline_data = em.BillingBaselineData(df_baseline_n, is_electricity_data=True)
reporting_data = em.BillingReportingData(df_reporting_n, is_electricity_data=True)

print(f"Disqualifications: {baseline_data.disqualification}")
print(f"Warnings:          {baseline_data.warnings}")

billing_model = em.BillingModel()
billing_model.fit(baseline_data)

# Save model to json
saved_model = billing_model.to_json()
loaded_model = em.BillingModel.from_json(saved_model)

# Model results
billing_model.plot(baseline_data, aggregation="monthly")
billing_model.plot(reporting_data, aggregation="monthly")

df_results = billing_model.predict(reporting_data, aggregation="monthly")
df_results['savings'] = df_results['predicted'] - df_results['observed']
print(f"Predicted Usage (kWh):  {round(df_results['predicted'].sum(), 2)}")
print(f"Observed Usage (kWh):   {round(df_results['observed'].sum(), 2)}")
print(f"Savings (kWh):          {round(df_results['savings'].sum(), 2)}")
```
