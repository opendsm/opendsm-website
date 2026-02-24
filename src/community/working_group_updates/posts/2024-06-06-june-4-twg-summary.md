---
date: 2024-06-06
description: OpenEEmeter working group recaps the elastic net model selection, discusses interpolation approaches, supplemental data inputs, and hyperparameter optimization for the hourly model.
---

# OpenEEmeter Technical Working Group Meeting Summary | June 4, 2024

Thanks to everyone who joined the most recent OpenEEmeter Working Group Meeting.

The June meeting began with a recap of the previous meeting in which the team had discussed the many models that had been tested for the OpenEEmeter hourly model and how they landed on an elastic net model. The elastic net model is the least computationally expensive approach while providing significant benefits over the previous model. This new model is approximately 11 times faster than the previous version of OpenEEmeter and can take GHI (solar irradiance) and other supplemental data (such as pumping schedules) as new model inputs.

Adam Scheer also reiterated that this refers to OpenEEmeter 4.1; while a more flexible model is also available, it is not appropriate to market this as OpenEEmeter 4.1 while incorporating variables that have not been tested or validated by the working group.

Current goals are to finalize the hourly model (tuning hyperparameters and translating the R&D code into final code), making sure the model is compatible with the revamped API, and debugging any bugs that crop up through testing.

Travis Sikes then discussed the model's new approach to interpolation. This change is important, because while the earlier model was based on individual hours, the input and output of the new model takes 24 hours at a time. This means that missing data must be interpolated.

Travis explained the different types of interpolation (univariate vs multivariate, linear, cubic, nearest data, etc.) and why the working group has settled on a multivariate RBF interpolator. This led to a detailed Q&A and discussion of why this approach was chosen, what data sufficiency was required, and other topics.

The discussion then moved on to the model's ability to incorporate supplemental data. Travis explained that the new model has the same input requirements as the old model with the addition of solar irradiance, and then discussed how the model also has the option for supplemental data inputs which can help in cases when limited data is available.

As an example, Travis showed how using PV installation date as supplemental data for commercial buildings (for which there are a limited number that have solar PV) yields imperfect results, but were a way to make the most of existing data. The conversation then moved on to a detailed presentation of recent efforts at hyperparameter optimization and population results.

Next steps include much more analysis on population-level results, and fully incorporating the hourly model into the OpenEEmeter.

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/sNTUOqbAbrE" frameborder="0" allowfullscreen></iframe>
