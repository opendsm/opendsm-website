---
hide:
 - toc
---

OpenDSM's origin lies within the [CalTRACK methodology](site:documentation/caltrack_history). CalTRACK originated in a working group initiated by California Public Utility Commission (CPUC) in 2012 to track metered savings for pay-for-performance energy efficiency programs. 

The first versions were developed collaboratively by PG&E and other California IOU's in conjunction with the California Energy Commission (CEC), Recurve, and other stakeholders. The goal was to develop reliable and transparent processes to calculate avoided energy use. The models that emerged from this process were the daily/billing models and the hourly model. The daily/billing models were heavily influenced by the Princeton Scorekeeping Method (PRISM)[^1]. Similarly the hourly model was an adapted version of Lawrence Berkeley National Laboratory's Time-of-Week and Temperature (TOWT) model[^2].

[^1]: PRISM 1986: [PDF](https://marean.mycpanel.princeton.edu/images/prism_intro.pdf) --- [Permalink](https://doi.org/10.1016/0378-7788(86)90003-4)
[^2]: TOWT 2011: [PDF](https://eta-publications.lbl.gov/sites/default/files/LBNL-4944E.pdf) --- [Permalink](https://doi.org/10.1109/TSG.2011.2145010)

CalTRACK was only a methodological specification, however; it was not itself a library that users could utilize to make measurements. OpenEEmeter was developed to be the open-source Python implementation of the CalTRACK methods. OpenEEmeter has since joined [EEweather](https://github.com/opendsm/eeweather) and comparison groups under the umbrella of OpenDSM.

OpenDSM continues to develop and evolve from the foundational work from those before us. Today's OpenDSM models have moved beyond CalTRACK while remaining rooted in methodological guidelines such as ASHRAE Guideline 14, IPMVP Option C, and the Uniform Methods Project. Development of the latest OpenDSM models occurred through a transparent, public, and collaborative working group process that grew out of the original CalTRACK working group. Changes to the models since CalTRACK can be found in each model's references section.

The latest models are easier to use, significantly faster, more accurate, and proven in extensive testing. In fact, OpenDSM was the first measurement methodology to be approved for the Inflation Reduction Act (IRA) Home Efficiency Rebates (HOMES) Program and verified by National Renewable Energy Laboratory (NREL). 
 
