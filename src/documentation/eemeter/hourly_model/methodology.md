The hourly model is trained using hourly energy usage intervals and predicts in hourly intervals.

The hourly model is the **CalTRACK hourly model**: a time-of-week and temperature (TOWT) model with
temperature and occupancy binning, closely related to the original
[LBNL TOWT model](https://eta-publications.lbl.gov/sites/default/files/LBNL-4944E.pdf).

## Model Theory

The model predicts hourly usage from three sources of variation:

- **Hour of week** — the week is divided into 168 hourly intervals (starting Monday), capturing the
  recurring weekly load shape.
- **Outdoor dry-bulb temperature** — a binned temperature response.
- **Occupancy state** — whether the building is in a high-load ("occupied") or low-load
  ("unoccupied") mode for a given time of week.

A separate prediction is produced for each combination of hour-of-week and occupancy state — so, for
example, Tuesday 7 pm, Friday 3 am, and Sunday 7 pm each get their own fitted behavior.

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/hourly_model/methodology/weekly_load_shape.png" alt="Average weekly load shape by hour of week" style="width:75%">
</div>

### Occupancy

Occupancy is not supplied as an input; the model infers it from the baseline data. Each of the 168
hours of the week is classified as either "occupied" (a high-load mode) or "unoccupied" (a low-load
mode), and that classification is what lets the model treat, say, a weekday business afternoon
differently from the same building overnight.

The classification is made by first fitting a simple weather-only regression of usage against heating
and cooling effects, with fixed reference temperatures (cooling above 65 °F, heating below 50 °F). For
every hour of the week, the model then looks at how the actual usage sits relative to that weather-only
expectation. If more than 65% of the observations for an hour of the week fall *above* the weather-only
prediction, that hour is marked occupied; otherwise it is marked unoccupied. The intuition is that hours where usage
routinely exceeds the simple weather baseline correspond to periods of activity, while hours that sit
at or below it correspond to a building's idle state.

### Temperature response

Within each occupancy mode the response to outdoor temperature is captured with a binned (piecewise)
scheme rather than a single slope, so the model can bend at the temperatures where heating and cooling
behavior changes. Candidate bin edges at 30, 45, 55, 65, 75, and 90 °F divide the temperature range
into segments. The bins are fit **separately for occupied and unoccupied** hours, allowing the two
modes to respond to temperature in different ways. Where a candidate bin holds too few temperature
readings to be estimated reliably, it is merged inward from the extremes, so sparsely populated cold or
hot bins do not destabilize the fit.

### Model components

The fitted model is a sum of components, each capturing a distinct "bucket" of consumption:

1. Temperature-independent ("always-on") load across all hours of the week.
2. Temperature-dependent usage during **unoccupied** hours.
3. Additional temperature-independent usage during **occupied** hours.
4. Additional temperature-dependent usage during **occupied** hours.

$$
UPH_{pi} = \underbrace{\sum \alpha_t TOW_p + \sum \beta_{T, n} Tc_{n, p}}_{\text{unoccupied}} + \underbrace{\sum \alpha_t TOW_p + \sum \beta_{T, n} Tc_{n, p}}_{\text{occupied}} + \epsilon_{pi}
$$

The occupancy classification, temperature binning, and the full hourly design matrix are specified in
Sections 3.8–3.10 of the [CalTRACK 2.1 Methods](site:caltrack/methodology/).

### Monthly models

Building energy consumption changes through the year, so the annual model is stitched together from
monthly models — a separate hourly model is fit for each month.

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/hourly_model/methodology/monthly_load_shapes.png" alt="Weekly load shape for each month" style="width:55%">
</div>

Each monthly model is fit with a weighting that emphasizes its own month and tapers off across the
adjacent months, so the transition from one month to the next is smooth.

<div style="text-align: center; margin-top: 30px">
    <img src="site:assets/images/eemeter/hourly_model/methodology/monthly_model_weight.png" alt="Monthly model weighting" style="width:75%">
</div>

### Limitations

The biggest limitation of this model is that it is not designed to function on sites with solar PV systems.
The model will not fail completely because solar irradiance is highly correlated with both temperature and 
time of year, but it will only capture solar effects in a very broad sense. If the training data that it was fit on was
largely cloudy in the spring and fall; it will predict the average cloudy day from its training data. It is
highly suggested that users adopt the newer OpenDSM hourly model which is built explicitly with solar PV sites
in mind.

---

Additional details can be found in the [CalTRACK 2.1 Methods](site:caltrack/methodology/) and the
[Technical Appendix](site:caltrack/technical_appendix/).
