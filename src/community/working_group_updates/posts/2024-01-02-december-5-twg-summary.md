---
date: 2024-01-02
description: OpenEEmeter working group discusses switching from stratified K-fold to rolling test/train cross-validation, replacing CVRMSE with PNRMSE, and incorporating solar irradiance (GHI) into the hourly model.
---

# OpenEEmeter Technical Working Group Meeting Summary | December 5, 2023

Thanks to everyone who joined the most recent OpenEEmeter working group.

Travis Sikes led off this meeting with a recap of the last meeting, in which the goal was to explore how to incorporate a variety of additional data inputs into the OpenEEmeter, such as temperature, humidity, and especially solar irradiance, in addition to contextual time series (day of week and month) data.

Travis pointed out that initially the team was using a stratified K-fold scheme within the baseline period for cross validation, but has moved on from that due to a concern of information leak; instead, they are now using a rolling test/train approach to minimize model overfitting.

Travis then reviewed the previous discussion in which the group had discussed the need to move away from CVRMSE (Coefficient of Variation of Root Mean Squared Error) as a metric for calibrating models, which doesn't work well for buildings with solar panels. The group discussed instead using PNRMSE (Percentile Normalized Root Mean Squared Error), which appears to correlate well with CVRMSE.

Armin Aligholian then went into more detail on the switch from stratified sampling to the three-year rolling test/train framework. He went on to explain how the team was exploring the addition of GHI (solar irradiance) and its impact on model performance, specifically for solar customers. Moreover, CCI (cloud cover index) was used as a metric to analyze the importance of GHI specifically on more cloudy days.

The meeting ended with a discussion of the need for more models in future work, including more work on neural network models, more input variation, as well as looking more closely at the impacts of cloud coverage, larger datasets for population analysis, and other factors.

**Next Meeting Scheduled: Tuesday, February 6, 2024**

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/NxxjyFbyokY" frameborder="0" allowfullscreen></iframe>
