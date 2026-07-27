---
date: 2023-05-04
description: OpenEEmeter working group discusses relaxing data requirements for delivered fuels like propane and heating oil, and reviews CalTRACK 2.1 results showing 74% reduction in seasonal bias and up to 100x speed improvement over 2.0.
---

# OpenEEmeter Technical Working Group Meeting Summary | May 2, 2023

Thanks to everyone who joined for this month's OpenEEmeter working group. We're excited at the huge progress we're making on CalTRACK 2.1, and greatly appreciate all who have taken time out of their schedule to participate in this important discussion.

Tim Guiterman from Sealed led off the discussion with a follow-up conversation on revising CalTRACK's requirements to permit its usage with delivered fuels such as propane and heating oil. Because these fuels are delivered and manually refilled, data for them are not as consistent nor as abundant as metered energy is. Tim and the Sealed team proposed making an exception to the 70 day data limit for delivered fuels.

The group discussed what the minimum number of data points should be and various factors that could alter this. There was also discussion of relaxing the 365 day baseline period to allow for more data when fitting this period. Most delivered fuel customers can provide data in the form of bills that cover years of time. Adam pointed out that while there might not be a perfect answer to the delivered fuel problem, using the CalTRACK approach is still much better than deemed approaches which are much less accurate.

The conversation concluded with Tim agreeing to analyze Sealed data so that the working group can make a data-driven decision on whether rule changes should be made for delivered fuel customers and, if so, what the minimum requirements should be, with proof that backs up these revisions.

Adam and Travis then summarized CalTRACK 2.0's deficiencies and how the nearly final model of CalTRACK 2.1 rectifies them. The main problem the team was attempting to solve was seasonal bias in the CalTRACK 2.0 model found primarily in gas meters. They showed that CalTRACK 2.1 has significantly reduced seasonal bias. At the same time it has been necessary to revisit how fast the model can be fit. Travis has implemented several clever means of speeding up the model from worst-case scenarios of 1 minute to fit down to 10 seconds. He also went into detail about how CalTRACK 2.1 differs from CalTRACK 2.0 in order to solve the issues laid out prior. Additionally, Travis briefly mentioned that they have implemented a CalTRACK 2.0 mode — a legacy mode — which can replicate CalTRACK 2.0 results with all of the speed improvements developed recently.

Overall, CalTRACK 2.1 reduces seasonal bias by 74% and is between 2 and 100 times faster than CalTRACK 2.0, depending on how it's used (legacy mode or not).

Adam and Travis anticipate that by the next meeting, the final CalTRACK 2.1 model will have completed its R&D phase. Next steps involve code cleanup, polishing, and documentation so that CalTRACK 2.1 can be integrated into the OpenEEmeter.

**Next Meeting Scheduled: Tuesday, June 6, 2023, 1pm PT**

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Enwj0yjw0Q0" frameborder="0" allowfullscreen></iframe>

Join the working group to get access by clicking this link:

[Join the Technical Working Group](https://opendsm.energy/community/)
