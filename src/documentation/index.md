---
hide:
 - toc
---

## Background

If you are new to OpenDSM, start with [General Concepts](site:documentation/general_concepts/), which introduces the vocabulary used throughout these docs (counterfactuals, baseline and reporting periods, error metrics). [Philosophy](site:documentation/philosophy/) explains the design constraints all OpenDSM models share, and [History](site:documentation/history/) traces their origins in the CalTRACK methods.

## Modules

### [EEmeter](site:documentation/eemeter)

Create long-term models fit on historical data to generate predictions of energy consumption

### [DRmeter](site:documentation/drmeter)

Create short-term models fit on historical data to generate predictions of energy consumption 

### [Comparison Groups](site:documentation/comparison_groups)*

Assign comparison groups (CGs) to correct EEmeter and DRmeter models using a non-participant population through one of the following methods

### [EEweather](https://github.com/opendsm/eeweather)*

Get the most appropriate weather data for a location

<span style="font-size: 0.8em;">
* Part of OpenDSM, but not yet fully developed; a well-defined API is planned for a future version
</span>