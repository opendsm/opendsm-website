---
date: 2023-03-08
description: OpenEEmeter working group reviews goals for CalTRACK 2.1 daily model bias improvements, discusses international implementation challenges from Carbon Co-op, and debates tradeoffs between daily and hourly model investment.
---

# OpenEEmeter Technical Working Group Meeting Summary | March 7, 2023

Thanks to everyone who joined us for yesterday's OpenEEmeter technical working group meeting.

Adam Scheer led off the meeting by reiterating the high-level goals for the CalTRACK 2.1 Daily model, which are to improve specific and known areas of model bias and gain computational efficiency in the process. He explained the need to solve seasonal and weekend/weekday bias by adding parameters and optimization steps without creating an overfitting problem or making the model so complex that it can't be scaled to hundreds of thousands or millions of meters.

For the CalTRACK Hourly model, Adam laid out issues to discuss in future meetings, including remedying known small bugs, specifying demand response baselines, and incorporating solar PV modeling.

Adam then introduced James Fenna from Carbon Co-op to discuss some challenges and modifications needed to implement CalTRACK (specifically EEweather) in the U.K. and internationally. In particular, James discussed the problems of calibrating for metric temperatures and the need for different sources of weather data internationally.

Adam then led a more detailed discussion of the specific tradeoffs of adding parameters to address seasonal bias in the model.

The group discussed how seasonal bias is a problem that has been known for decades, and how much effort should be put into improving the Daily model versus Hourly.

**Next Meeting Scheduled: Tuesday, April 4, 2023, 10am ET / 1pm PT**

Join the working group to get access by clicking this link:

[Join the Technical Working Group](https://opendsm.energy/community/)

Watch the full meeting below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/GYQOPgPZzFE" frameborder="0" allowfullscreen></iframe>

[Download meeting slides (PDF)](site:assets/reference_docs/working_group/meeting_5_lfe_openeemeter_wgmtg_3-7-2023.pdf)
