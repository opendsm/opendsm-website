---
date: 2023-06-12
description: OpenEEmeter working group reviews CalTRACK 2.1 testing results showing dramatic reductions in seasonal and weekend/weekday bias, discusses an adaptive loss function, and previews plans for CalTRACK 3.0.
---

# OpenEEmeter Technical Working Group Meeting Summary | June 6, 2023

Thanks to everyone who attended the most recent working group meeting.

Adam Scheer led off the meeting with results of testing on how CalTRACK 2.1 running in "2.0 mode" gives almost identical model results to CalTRACK 2.0, while benefitting from the enormous improvements in computational efficiency of CalTRACK 2.1. This is important, because in many use cases (such as when only monthly data is available), users will be running the methods with the older model; they can now have confidence that results will be almost identical.

Adam then discussed the testing results for CalTRACK 2.1, noting that while not every problem has been solved, many big-ticket items have been addressed. He mentioned the model's improved reliability and more efficient handling of complex data. He pointed out that CalTRACK 2.1 has improved seasonal and weekend/weekday bias dramatically over CalTRACK 2.0:

- Wintertime bias across 4,000 residential gas meters went from -7% to -1%
- Summertime bias went from 11% to 5%
- Weekday/weekend bias for electric meters went from -3% to 1%
- For commercial buildings, the weekend/weekday bias went from 14% to under 1%

Adam and Travis then discussed the introduction of an adaptive loss function, a step beyond using mean squared error. Introducing this function yields similar results to the CalTRACK 2.1 model, but is slightly better for some use cases and does not introduce significant bias.

The discussion moved towards the final steps in the development of CalTRACK 2.1. Adam highlighted the importance of good software hygiene and maintaining updated versions. He also talked about the possibility of incorporating new features, such as more efficient data handling and storage capabilities provided by the new version of the Pandas library.

The discussion on the future of the working group centered around what comes next, including the potential development of CalTRACK 3.0 and its associated features, such as improved daily modeling and potential incorporation of thermal lag and other factors into the model. The conversation also included a brief mention of possible code consolidation under the OEEM umbrella. Adam noted the increasing use of OpenEEmeter, indicating that it might be beneficial to bring all these tools and methods together for a more streamlined approach.

The team is aiming to get the updates into the OpenEEmeter to be available for others to test within the month.

**Next Meeting Scheduled: Tuesday, July 11, 2023, 1pm PT**

Watch the full presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/uNRL2_CF-y4" frameborder="0" allowfullscreen></iframe>

[Join the Technical Working Group](https://opendsm.energy/community/)
