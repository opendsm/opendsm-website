The billing model uses the [daily model](site:documentation/eemeter/daily_model/methodology/) with small configuration changes and billing (monthly or bimonthly) interval data.

## Model Theory

### Converting from billing data to daily data

The billing model intakes billing data and calculates the average energy usage for each given period. For example if a bill covers 31 days and uses 93 therms total, then each day would be given 3 therms of usage. A billing period is assumed to start on the datetime in which it has a value and to end 1 day prior to the next datetime with a value with 1 final empty datetime signifying the end of the year resulting in 13 total datetimes for monthly billing data and 7 for bimonthly billing data. Pulling the temperature from `EEweather` ensures that each day's mean temperature is correct.

From here, the data is treated as daily interval data and uses the daily model internally.

### Configuration Changes

The model shape, balance points, nomenclature, archetypes, and fitting procedure are those of the [daily model](site:documentation/eemeter/daily_model/methodology/) and are not repeated here. The billing model differs in the following ways:

- **[Smooth Transitions](site:documentation/eemeter/daily_model/methodology/#smooth-transitions)**: disabled.
- **[Robust, Adaptive Outlier Downweighting](site:documentation/eemeter/daily_model/methodology/#robust-adaptive-outlier-downweighting)**: disabled.
- **[Model Splits](site:documentation/eemeter/daily_model/methodology/#model-splits)**: disabled.

---

## Real Data Example

Here are 6 examples of how the billing model performs on real data. Because the billing data is converted to daily data, the plots show lines of data points where the usage is the same over the range of temperatures seen during each billing period.

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/billing_model/real_examples.png" alt="Real world examples">
</div>

<div style="text-align: left; font-size: 0.9em; color: #888; margin-top: 40px;">
    For additional information and validation details, see <a href="site:documentation/eemeter/billing_model/references/">References</a>.
</div>
