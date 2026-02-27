---
date: 2023-09-14
description: OpenEEmeter working group announces the deprecation of the CalTRACK name in favor of OpenEEmeter, previews the upcoming 2.1 daily model release, and discusses limitations of the 2.0 hourly TOWT model and goals for 3.0.
---

# OpenEEmeter Technical Working Group Meeting Summary | September 5, 2023

Thanks to everyone who joined the last OpenEEmeter working group.

Adam Scheer kicked off the meeting with the announcement that the name CalTRACK was being deprecated; going forward, both methods and code will be referred to as the OpenEEmeter under a single umbrella to emphasize the tool's global relevance. This decision was influenced by feedback from clients and users that the name CalTRACK gave an impression of regional specificity, leading to concerns about the model's applicability outside California.

In addition, while it is appropriate to continue to have a detailed description of methods, the OpenEEmeter code is now sophisticated enough that it should be considered the source of truth as to what is actually happening with model calculations.

Adam then announced that the 2.1 daily model is at the point where it will soon be ready to be merged and available to everyone. In addition, the team will soon release comprehensive R&D results to support the decisions made in the final formulation of the model.

Next, Adam gave a high level overview of the 2.0 hourly methods to set the stage for discussing improvements in the performance of the 3.0 methods. Adam explained that 2.0 is founded on a Time of Week and Temperature (TOWT) model, which is primarily based on two variables: the hour of the week and the temperature. With 168 hours in a week, this results in a unique energy consumption prediction for each hour. To capture seasonal variations, the model is designed to create an independent prediction for each month of the year, considering the unique energy consumption characteristics of every month.

Issues with the 2.0 model include potential overfitting and that the model is incomplete when it comes to solar PV customers, whose consumption is heavily dependent on the amount of sunlight (solar irradiance). Without an awareness of solar irradiance the model will perform poorly when predicting consumption patterns of solar customers.

The goal of 3.0 is to reduce over- or under-fitting, introduce solar irradiance and other weather variables that may have an impact on consumption, and allow the model to take advantage of the patterns that it recognizes in the data.

The group then discussed in detail various aspects of these challenges and potential solutions. The meeting concluded with a discussion of laying the groundwork for next steps.

**Next Meeting Scheduled: Tuesday, October 3, 2023, 1pm PT**

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/-0tQP3xlRlE" frameborder="0" allowfullscreen></iframe>
