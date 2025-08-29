Create short-term models fit on historical data to generate predictions of energy consumption.

As an example: demand response events generally occur over the course of a few hours in a given day. To model this event, a DRmeter model might use 45 days prior to the event and 15 days after as the training period while excluding the event day.

### Models

#### [CalTRACK Model](site:documentation/drmeter/caltrack_model/methodology)

An implementation of the time-of-week and temperature model designed to operate on short-term, hourly data.

#### [New Model](site:documentation/drmeter/new_model)

A derivative of the OpenEEmeter hourly model. This model will be able to accurate measure solar and non-solar meters using short-term, hourly data.