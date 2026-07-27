---
date: 2024-03-27
description: OpenEEmeter working group celebrates the public release of 4.0, compares LSTM neural network vs. elastic net models for the hourly model, and discusses incorporating supplemental data inputs.
---

# OpenEEmeter Technical Working Group Meeting Summary | March 5, 2024

Thanks to everyone who joined our recent OpenEEmeter Technical Working Group meeting on March 5th, 2024.

Travis Sikes kicked off the meeting with an announcement of [RetroMeter](https://es.catapult.org.uk/project/retrometer/)'s use case review of OpenEEmeter 4.0 on Thursday, March 14th at 10am CST, in which they presented some of the work they've been doing adapting the OpenEEmeter for use cases in the U.K., and giving the OpenEEmeter developer community an opportunity to provide feedback on the user experience with the new API and desired features.

Travis then announced the full public release of OpenEEmeter 4.0, now available via pip install. You can learn more about OpenEEmeter 4.0 from the recent [Linux Foundation Energy webinar](https://community.linuxfoundation.org/events/details/lfhq-lf-energy-presents-unveiling-openeemeter-40/). The discussion then moved on to recent work on the hourly model. In the previous meeting, Armin Aligholian presented results showing the elastic net model outperforming XGBoost, AdaBoost and other regression models usable within scikit-learn in terms of test error, computation time, and reduced overfitting. The elastic net had lower error on cloudy days and lower bias.

In this meeting, Armin described how the team explored using an LSTM neural network architecture. While this approach showed some promise, the LSTM model was very computationally expensive, taking 14 minutes per meter on a CPU to achieve test error comparable to the elastic net.

The elastic net model is 11x faster than the current OpenEEmeter model, with lower test error and less overfitting. The team also looked at incorporating supplemental data like EV charging and pump schedules. Adding this binary time series data as an input feature improved predictions of energy spikes by 40% in a worst-case scenario.

Some key next steps are migrating the new elastic net model into the OpenEEmeter API, exploring adding NMBE to the loss function, analyzing performance on commercial buildings, and revisiting data sufficiency criteria in light of the new model structure. While the new architecture allows for easy incorporation of additional time series inputs, the group will need to be thoughtful about which inputs to allow in the base model to ensure quality and standards.

Thanks again to Travis and Armin for leading the group through the latest results and analyses, and to everyone for the great questions and discussion.

**Next Meeting Scheduled: Tuesday, April 2, 2024**

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/niX6sBcYzYQ" frameborder="0" allowfullscreen></iframe>
