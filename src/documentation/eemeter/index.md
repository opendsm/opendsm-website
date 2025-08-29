Create long-term models fit on historical data to generate predictions of energy consumption.

As an example: energy efficiency interventions (modifications to a building) must be measured over the course of a year because they will likely affect the energy usage during various seasons differently. An OpenEEmeter model would therefore need to be trained on a baseline year (1 year prior to the change) and will predict what would have happened if the intervention never occurred (a counterfactual) for the reporting year (1 year after the change).

### Models

#### [Hourly Model](site:documentation/eemeter/hourly_model/methodology)

A model designed to operate quickly on hourly interval data to provide accurate predictions in a reporting year.

#### [Daily Model](site:documentation/eemeter/daily_model/methodology)

A model using daily interval data to provide accurate predictions and to be able to disaggregate daily heating and cooling loads.

#### [Billing Model](site:documentation/eemeter/billing_model/methodology)

A modification of the daily model using billing, monthly or bimonthly, data to provide accurate annual predictions.