---
date: 2023-04-05
description: OpenEEmeter working group discusses CalTRACK data sufficiency barriers for delivered fuels, and previews CalTRACK 2.1 results showing dramatic bias reductions and a 20–120x improvement in computational speed.
---

# OpenEEmeter Technical Working Group Meeting Summary | April 4, 2023

Thanks to everyone who joined the most recent OpenEEmeter working group meeting.

Tim Guiterman from Sealed led off the conversation with a discussion of the need to address delivered fuels such as propane or heating oil in the CalTRACK specifications. CalTRACK's current data sufficiency requirements often limit the ability to model homes using delivered fuels, which are common in the Northeast. Because these fuels are not necessarily delivered on a consistent cadence, CalTRACK's monthly data requirements are a barrier to using it for these kinds of customers. Making CalTRACK more accessible and avoiding unnecessary disqualifications is particularly important given the new funding from the IRA and the opportunities it presents for adopting a measured pathway for incentives.

Adam Scheer and Travis Sikes then shared updates and results related to the CalTRACK Daily 2.1 model, which is nearing completion. Adam reviewed the issues CalTRACK 2.1 is attempting to address around model bias, and the tradeoffs between adding parameters to correct bias and the need to avoid overfitting. Preliminary results on the new 2.1 model showed a dramatic improvement, reducing summer, winter, and weekend bias.

Getting these kinds of improvements requires additional computations. CalTRACK 2.0 performance prohibits any additional complexity due to the time it takes to fit a model (20–60 seconds). This is particularly prohibitive to the cross-validation that is the lynchpin of our current improvement efforts.

To address this, Travis gave an extended presentation of how he has dramatically improved the computational efficiency of the OpenEEmeter, reducing the per-meter fitting time from 20–60 seconds to approximately 0.5 seconds (20–120 times faster) for an equivalent fit. For those that need or want to run the original CalTRACK 2.0, a CalTRACK 2.0 legacy mode will be included that has all of these computational efficiency improvements.

The team discussed the remaining steps needed to finalize the model formulation and are hopeful that it will be wrapped up in the next one to two months. We are excited about the progress made so far and the potential impact of the updated model.

**Next Meeting Scheduled: Tuesday, May 2, 2023, 1pm PT**

Join the working group to get access by clicking this link:

[Join the Technical Working Group](https://opendsm.energy/community/)

Watch the full meeting below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/igrQjCTKzTI" frameborder="0" allowfullscreen></iframe>

[Download meeting slides (PDF)](site:assets/reference_docs/working_group/meeting_6_lfe_openeemeter_wgmtg_4-4-2023.pdf)
