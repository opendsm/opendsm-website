---
date: 2024-02-27
description: OpenEEmeter working group discusses integrating EEweather functions into OpenEEmeter, simplifications in 4.0 code, data sufficiency updates, and an elastic net model outperforming alternatives for the hourly model.
---

# OpenEEmeter Technical Working Group Meeting Summary | February 6, 2024

Travis led off the meeting with an explanation of why the group is integrating the written methods into the OpenEEmeter repository. The group then discussed the many functions (such as weather data) that are duplicated between the EEweather and OpenEEmeter and the advantage of integrating them, including eliminating redundancies and making the process of updating much simpler while providing a more seamless experience for users.

Travis then explained a number of simplifications that have been made in OpenEEmeter 4.0 code, specifically including default data settings in the baseline class. As most users use these defaults, this will simplify the use of the software and offer more consistency and standardization, while still allowing more expert users to change defaults for their particular use cases.

Travis also proposed some adjustments to data sufficiency requirements, such as removing the requirement that daily data for electric meters not have negative values, as this doesn't necessarily indicate an error (there are many solar users, for example, who may show negative consumption on a regular basis). Instead, a requirement would be added that non-electric meters cannot have negative values.

Armin recapped the discussion from last week of the advantage of switching from CVRMSE to PNRMSE as a more reliable model performance measure, especially for solar customers. Armin then explained how the working group has been testing different models with combined data from different weather features (solar irradiance, humidity, and temperature) to determine which perform the best. The team found that an elastic net model performs better than the current hourly model and better than other models tested, including for computational speed.

For future work, the team will continue to focus on the challenge of overfitting, load shape analysis for different seasons, and considering the potential of ensemble models.

**Next Meeting Scheduled: Tuesday, March 5, 2024**

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/P8QUs7WKCJ0" frameborder="0" allowfullscreen></iframe>
