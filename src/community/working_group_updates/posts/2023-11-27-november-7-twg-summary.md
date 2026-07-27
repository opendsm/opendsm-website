---
date: 2023-11-27
description: OpenEEmeter working group discusses API improvements in 4.0, CalTRACK 2.0 model challenges with overfitting and solar PV, and a proposed shift from CVRMSE to PNRMSE and static to rolling cross-validation.
---

# OpenEEmeter Technical Working Group Meeting Summary | November 7, 2023

Thanks to everyone who attended the most recent OpenEEmeter working group meeting.

The meeting began with a discussion by Jason Chulock of coming improvements in the OpenEEmeter 4.0 API, including consolidating usage between all three methods — hourly, daily, and billing — and making certain common configurations the default. Jason then laid out improvements around data sufficiency and methods compliance. The goal of these changes is to make the API more user-friendly and efficient.

Travis Sikes then led a recap and discussion of the current issues and progress on the CalTRACK 2.0 model. Key concerns of CalTRACK 2.0 include its tendency to be overfit, its incompleteness for solar PV customers, and the inflexibility in handling input data.

Travis explained that the team would be using AMI measurements combined with weather, solar, and categorical data to enhance prediction accuracy. He then discussed evolving the cross-validation methodology from a static 24-hour window to a dynamic rolling test/train approach. There was a consensus on the need for a more robust error metric, suggesting a shift from CVRMSE to PNRMSE. Travis emphasized the need for commercial data to complete the test data sets.

Looking ahead, next steps include the continued exploration of advanced modeling techniques like neural networks and the use of larger datasets for a more thorough population analysis.

**Next Meeting Scheduled: Tuesday, December 5, 2023**

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/A3dEu5HNQ_o" frameborder="0" allowfullscreen></iframe>
