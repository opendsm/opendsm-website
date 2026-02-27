---
date: 2023-10-19
description: OpenEEmeter working group announces the public alpha release of 4.0 daily model, and discusses approaches to improving the hourly model for solar PV customers including elastic nets, neural nets, and rolling cross-validation.
---

# OpenEEmeter Technical Working Group Meeting Summary | October 3, 2023

The working group is pleased to announce that they have wrapped up the OpenEEmeter 4.0 Daily Model, and that the Alpha version is now available to the public and can be installed using: `pip install eemeter==4.0.0a2`.

The discussion then moved to progress on the hourly model. Armin began by reviewing some of the issues with the current hourly model, including that it seems to be overfit, and that it is incomplete when it comes to solar photovoltaic customers, where it produces high error rates. The question is how to make the model flexible and allow more inputs, including solar data.

Armin then discussed two broad options for addressing this issue: disaggregating solar data, and including weather and solar data to improve AMI prediction. Solar disaggregation would be more complex, which suggests that improving AMI prediction might be preferable for now.

The discussion then moved to the question of what approach to take when adding complexity to the model. There was discussion of the pros and cons of various machine learning approaches, including elastic nets and neural nets, with elastic nets as a simpler and more "interpretable" option.

There was also discussion in the group about the potential downside of neural nets and losing the interpretability of the model; however it was pointed out that when you add a lot of coefficients, even in a linear model, you lose physical interpretability.

The discussion ended with next steps, including implementing rolling train/test cross validation, using larger datasets for population analysis, doing a deep dive on the impact of GHI in model improvement, and developing neural net models for AMI prediction.

**Next Meeting Scheduled: Tuesday, November 7, 2023**

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/PWry4VnCK1c" frameborder="0" allowfullscreen></iframe>
