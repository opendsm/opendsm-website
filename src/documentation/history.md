---
hide:
 - toc
---

OpenDSM's origin lies within the [CalTRACK methodology](site:documentation/caltrack_history).

The CalTRACK methodology comes from a working group initiated by California Public Utility Commission (CPUC) in 2012 to track metered savings for pay-for-performance energy efficiency programs and is similar to ASHRAE Guideline 14, IPMVP Option C, and the Uniform Methods Project (UMP).

The first versions were developed collaboratively by PG&E and other California IOU's in conjunction with the California Energy Commission (CEC), Recurve, and other stakeholders. The goal was to develop reliable and transparent processes to calculate avoided energy use. The models that came from this process were the daily/billing models and the hourly model. The daily/billing models were heavily influenced by the Princeton Scorekeeping Method (PRISM)[^1]. Similarly the hourly model was an adapted version of Lawrence Berkeley National Laboratory's Time-of-Week and Temperature (TOWT) model[^2].

[^1]: PRISM 1986: [PDF](https://marean.mycpanel.princeton.edu/images/prism_intro.pdf) --- [Permalink](https://doi.org/10.1016/0378-7788(86)90003-4)
[^2]: TOWT 2011: [PDF](https://eta-publications.lbl.gov/sites/default/files/LBNL-4944E.pdf) --- [Permalink](https://doi.org/10.1109/TSG.2011.2145010)

The CalTRACK methodology only defined how to set up the models; it was not itself a library that users could utilize to make measurements. OpenEEmeter came in to become the open-source Python implementation of the CalTRACK methods. The changes to the models since the CalTRACK methods can be found in each model's references section. 

OpenEEmeter has since joined [EEweather](https://github.com/opendsm/eeweather) and comparison groups under the umbrella of OpenDSM.

Today, OpenDSM has moved beyond the CalTRACK methods. Our models are easier to use, significantly faster, more accurate, and proven in extensive testing. In fact, OpenDSM is the first -- and currently only -- measurement methodology to be approved for the Inflation Reduction Act (IRA) Home Efficiency Rebates (HOMES) Program and verified by National Renewable Energy Laboratory (NREL). 

OpenDSM continues to develop and evolve from the foundational work from those before us.