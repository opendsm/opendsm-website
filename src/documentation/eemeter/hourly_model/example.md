In this example, we'll walk through creating an Hourly Model and predicting usage with it.

In this release the hourly model is the CalTRACK hourly (Time-Of-Week and Temperature) model; see the
[Methodology](site:documentation/eemeter/hourly_model/methodology/) for an overview.

<span style="font-size: 0.9em;">
1) This example makes use of Matplotlib. Matplotlib is not a required dependency of OpenDSM.<br>
2) OpenDSM 1.0 requires `pandas<3`.<br>
3) The example data is downloaded from the OpenDSM repository (see the fetch step below).
</span>

### Imports

```python
import matplotlib.pyplot as plt

import opendsm as odsm
from opendsm.eemeter.models.hourly_caltrack import (
    HourlyModel,
    HourlyBaselineData,
    HourlyReportingData,
)
```

### Loading data

The hourly model requires hourly meter usage (`observed`) and hourly temperature (`temperature`), each
with a timezone-aware datetime index. For weather data see
[EEweather](https://github.com/opendsm/eeweather), which performs site-to-weather-station matching and
can pull and cache temperature data from public (US) sources.

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

This returns two dataframes of hourly electricity data (one per meter id), for the baseline and
reporting periods. As in the other examples, we filter to a single meter.

```python
df_baseline, df_reporting = odsm.test_data.load_test_data("hourly_treatment_data")

n = 15
id = df_baseline.index.get_level_values(0).unique()[n]

df_baseline_n = df_baseline.loc[id]
df_reporting_n = df_reporting.loc[id]
```

We can plot the first couple of weeks of the baseline period to get a feel for the meter:

```python
sl = df_baseline_n.iloc[:336]
ax = sl['observed'].plot(label='Observed Usage', color='blue')
sl['temperature'].plot(ax=ax, secondary_y=True, label='Temperature (F)', color='orange')
ax.set_ylabel('Observed Usage (kWh)')
ax.right_ax.set_ylabel('Temperature (F)')
plt.title('Observed Usage and Temperature (first 2 weeks, baseline)')
plt.show()
```

??? Returns
    <div style="text-align: center; margin-top: 30px">
        <img src="site:assets/images/eemeter/hourly_model/example/baseline_data_hourly.png" alt="Hourly Baseline Data">
    </div>

### Loading Data into EEmeter Data Objects

We load the usage and temperature series into the hourly data classes, which validate the data and
check sufficiency. The classes accept a `DataFrame` directly, or `Series` via `.from_series`.

```python
baseline_data = HourlyBaselineData.from_series(df_baseline_n['observed'], df_baseline_n['temperature'], is_electricity_data=True)
reporting_data = HourlyReportingData.from_series(df_reporting_n['observed'], df_reporting_n['temperature'], is_electricity_data=True)

print(f"Warnings: {[w.qualified_name for w in baseline_data.warnings]}")
```

??? Returns
    ```
    Warnings: ['eemeter.caltrack_sufficiency_criteria.incorrect_number_of_total_days',
               'eemeter.caltrack_sufficiency_criteria.extreme_values_detected']
    ```

These are warnings, not disqualifications — see the
[Sufficiency](site:documentation/eemeter/hourly_model/sufficiency/) page for the criteria.

### Creating the Model

The hourly model follows the same initialize → fit → predict flow:

```python
hourly_model = HourlyModel()
hourly_model.fit(baseline_data)

df_results = hourly_model.predict(reporting_data)
print(df_results.head())
```

??? Returns
    ```
    datetime                   temperature   observed  predicted  predicted_uncertainty
    2019-01-01 00:00:00-06:00        -5.08  23.181797  34.036280              16.830413
    2019-01-01 01:00:00-06:00        -5.98  29.068728  34.468984              16.830413
    2019-01-01 02:00:00-06:00        -7.06  30.883118  35.019203              16.830413
    2019-01-01 03:00:00-06:00        -7.06  31.304552  35.163008              16.830413
    2019-01-01 04:00:00-06:00        -7.06  30.778175  35.420675              16.830413
    ```

We can plot the predicted usage against the observed usage over the reporting period:

```python
sl = df_results.iloc[:336]
ax = sl['observed'].plot(label='Observed', color='blue')
sl['predicted'].plot(ax=ax, label='Predicted', color='orange')
ax.set_ylabel('Usage (kWh)')
ax.legend()
plt.title('Observed vs Predicted (first 2 weeks, reporting)')
plt.show()
```

??? Returns
    <div style="text-align: center; margin-top: 30px">
        <img src="site:assets/images/eemeter/hourly_model/example/hourly_observed_vs_predicted.png" alt="Hourly Observed vs Predicted">
    </div>

### Calculating Savings

Savings are the difference between predicted (counterfactual) and observed usage over the reporting
period:

```python
predicted = df_results['predicted'].sum()
observed = df_results['observed'].sum()
print(f"Predicted Usage (kWh):  {round(predicted, 2)}")
print(f"Observed Usage (kWh):   {round(observed, 2)}")
print(f"Savings (kWh):          {round(predicted - observed, 2)}")
```

??? Returns
    ```
    Predicted Usage (kWh):  76176.31
    Observed Usage (kWh):   58782.37
    Savings (kWh):          17393.94
    ```

### Model Serialization

The fit model can be serialized to JSON and read back in later. The hourly model's serialization is a
large object (the Time-Of-Week and Temperature segment models with their coefficients), so it is not
shown here in full.

```python
saved_model = hourly_model.to_json()
loaded_model = HourlyModel.from_json(saved_model)
```

## Example Code
```python
import matplotlib.pyplot as plt

import requests
import opendsm as odsm
from opendsm.common import test_data
from opendsm.eemeter.models.hourly_caltrack import (
    HourlyModel,
    HourlyBaselineData,
    HourlyReportingData,
)

# OpenDSM 1.0's loader expects the example data in its data directory; fetch it once.
test_data.data_dir.mkdir(parents=True, exist_ok=True)
for fname in ["hourly_data_2.parquet", "attribution.txt"]:
    dest = test_data.data_dir / fname
    if not dest.exists():
        r = requests.get(f"https://raw.githubusercontent.com/opendsm/opendsm/v1.0.0/data/{fname}")
        r.raise_for_status()
        dest.write_bytes(r.content)

df_baseline, df_reporting = odsm.test_data.load_test_data("hourly_treatment_data")

n = 15
id = df_baseline.index.get_level_values(0).unique()[n]

df_baseline_n = df_baseline.loc[id]
df_reporting_n = df_reporting.loc[id]

baseline_data = HourlyBaselineData.from_series(df_baseline_n['observed'], df_baseline_n['temperature'], is_electricity_data=True)
reporting_data = HourlyReportingData.from_series(df_reporting_n['observed'], df_reporting_n['temperature'], is_electricity_data=True)

hourly_model = HourlyModel()
hourly_model.fit(baseline_data)

# Save model to json
saved_model = hourly_model.to_json()
loaded_model = HourlyModel.from_json(saved_model)

df_results = hourly_model.predict(reporting_data)
predicted = df_results['predicted'].sum()
observed = df_results['observed'].sum()
print(f"Predicted Usage (kWh):  {round(predicted, 2)}")
print(f"Observed Usage (kWh):   {round(observed, 2)}")
print(f"Savings (kWh):          {round(predicted - observed, 2)}")
```
