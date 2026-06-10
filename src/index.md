---
hide:
 - navigation
 - toc
---
<style>
  .md-typeset h1,
  .md-content__button { display: none; }
  .md-header__title--active .md-header__topic {
        opacity: unset;
        pointer-events: unset;
        transform: unset;
        z-index: unset;
    }
  .md-header__title--active .md-header__topic + .md-header__topic {
      opacity: 0;
      pointer-events: unset;
      transform: unset;
      z-index: unset;
  }
</style>

<p align="center" id="opendsm">
  <a href="https://lfenergy.org/projects/opendsm/"><img src="site:assets/images/common/opendsm-horizontal-color.svg#only-light" alt="OpenDSM"></a>
  <a href="https://lfenergy.org/projects/opendsm/"><img src="site:assets/images/common/opendsm-horizontal-white.svg#only-dark" alt="OpenDSM"></a>
</p>

<p align="center">
    <em>OpenDSM: An open-source python package to develop and implement standard methods for predicting metered energy usage.</em>
</p>

<!-- opendsm-badges -->

---

OpenDSM (formerly OpenEEmeter) is an open-source library ([source code](https://github.com/opendsm/opendsm)) used to measure the impacts of demand-side programs by using historical data to fit models and then create predictions (counterfactuals) to compare to post-intervention, observed energy usage.

## Key Features include:

- **Open Source**: All code is open source, making OpenDSM an excellent choice for measuring energy savings when results must be transparent and reproducible.
- **Fast**: A key tenet of OpenDSM modules are to be highly efficient, critical when there are millions of meters to be modeled. 
- **Easy and Intuitive**: The API interface is inspired by [scikit-learn](https://scikit-learn.org/stable), a well-known data science package for building models. Just fit and predict.
- **Pandas DataFrame Support**: Input data and predictions use pandas DataFrames, a well-known format for data scientists and engineers.
- **Model Serialization and Deserialization**: Models can be serialized into dictionaries or json objects, saved, and deserialized later.

## Core Modules

### [OpenEEmeter](site:documentation/eemeter)

Create long-term models fit on historical data to generate predictions of energy consumption

- **Models to Fit Your Data**: Billing, daily, and hourly models, depending on the time-series resolution
- **Input Data Formatting**: Meter usage and temperature time series are input to models through data classes to ensure standardization and avoid common pitfalls
- **Data and Model Sufficiency**: Native sufficiency checking to verify measurement compliance with the approved methodology

### [DRmeter](site:documentation/drmeter)

Create short-term models fit on historical data to generate predictions of energy consumption 

- **Hourly Model**: All demand response models require at least hourly resolution data

### Comparison Groups

Assign comparison groups (CGs) to correct OpenEEmeter models using non-participant population through one of the following methods

- **Comparison Group Clustering**: Cluster on model error profiles to select unique CG for each treatment meter
- **Individual Meter Matching**: Create population-level corrections by choosing the nearest *n* meters using Euclidean distance
- **Stratified Sampling**: Select meters for CG based upon shared characteristics (outdated methodology)

<span style="font-size: 0.8em;">
* Planned feature in future OpenDSM versions
</span>

### [EEweather](https://github.com/opendsm/eeweather)

Get the most appropriate weather data for a location

- **Match Location**: Select a weather station using latitude/longitude or ZIP code (ZCTA)
- **Climate Zone Sensitive**: Ensures that the selected weather station is within the same climate zone
- **Reliable Data Sources**: Utilizes US Census Bureau, NOAA NCDC, and NREL as primary data sources

<span style="font-size: 0.8em;">
* Planned integration in future OpenDSM versions
</span>