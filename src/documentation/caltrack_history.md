---
hide:
 - navigation
 - toc
---

# History of The CalTRACK Process

The CalTRACK process began in 2012 with a decision ([D.12-05-015](http://docs.cpuc.ca.gov/PublishedDocs/PUBLISHED/FINAL_DECISION/166830-07.htm#P1575_334402)) by the California Public Utilities Commission (CPUC) to “broaden allowable software under Energy Upgrade California.” PG&E led the effort with an agreement to use weather adjusted billing analysis (now called CalTRACK) to create a level playing field for an open market for software tools that contractors use to predict savings and deliver rebates to customers. This system was also designed as a means to track normalized metered savings for pay-for-performance (P4P) programs, and has since become the basis for the Pacific Gas & Electric (PG&E) Residential P4P Pilot.

CalTRACK provides a system that is clearly defined at every granularity, including general methods, implementation rules, and detailed specification, and is instantiated in 100% open source code.

The CalTRACK process was originally designed for 2 use cases:

1. Calibrating the predictions being made by Advanced Home Upgrade (AHU) eligible software tools to ensure a level playing field and ensure relative accuracy in predicting SITE energy savings.
2. Using CalTRACK as a standard measurement for PG&E to provide PAYABLE incentives to Res P4P Pilot Aggregators.

The CalTRACK approach delivers results to establish PAYABLE incentives to implementers and aggregators based on changes in consumption at the customer meter. Rather than being paid upfront based on a prediction of savings through Database for Energy Efficiency Resources (DEER) or local Technical Reference Manual (TRM) this approach only pays for those normalized metered savings that are delivered and calculated with transparent replicable methods. Payments to implementers and aggregators based on this approach is a rigorous means of maintaining accountability for savings achieved at the meter in the energy efficiency portfolio.

To deliver on the CPUC ruling for expanding the software options in AHU, and to deliver a tool capable of supporting the PG&E P4P High Opportunity Program and Projects RFP, PG&E convened a process that spanned nearly four years, and included the CPUC, CEC, IOUs, and other stakeholders. This history is described in the following paragraphs.

## PHASE I

In February of 2013, the CEC, CPUC, and all four CA IOUs agreed to the overall method and approach resulting in an agreement between parties to develop a system to track actual weather normalized site-based savings to calibrate software predictions and send feedback into the market then called "^^[Broadening the Allowable Software for Energy Upgrade California (EUC)](site:assets/reference_docs/caltrack/eucsoftwareproject-phaseiiproposal.pdf)^^" which established the core concept of measuring normalized impacts at the meter that later became known as metered efficiency, or normalized metered energy consumption (NMEC).  

Goal from agreement:

*The empirical calibration system will track the relationship between a ***software’s predictions of future savings, compared to actual energy bills (normalized for weather)***, in terms of both average accuracy and variance levels.  This data will then be used to calibrate prediction levels, creating a level playing field and accountability to actual performance. For example, software that consistently overestimates savings would have a discount applied to it. This “discount” would not only normalize its results with other software, but would influence software company and software users to change their modeling algorithms and behavior to achieve more accurate results.*

*It will be necessary to develop the specific calculation methodology that will be used to measure ***realization rate and variance***, and how this data will then be used to calibrate predicted results for a given model.*

## PHASE II

PG&E convened a ^^**working group of stakeholders and technical experts**^^, including IOUs and CEC / CPUC. This group analyzed past program data and tested generalized methods to achieve the goals set forth in Phase I.

This process led to a consensus around ^^**a method to calculate site-based energy savings**^^ for use to calibrate the site-based weather normalized monthly savings predictions put out by AHU software.

Open Source Meter Development: There was a gap of a year between PHASE II and PHASE III of the CalTRACK process. During this gap, OpenEE / Sustainable Spaces, LLC continued the development of the the CalTRACK methods as an open source code base that was funded in part by the California Energy Commission. This code base resulted in the open source OpenEEmeter platform and is supported and provided as a public resource available for use for both private and commercial applications to all at no cost under a [permissive open-source license](https://www.apache.org/licenses/LICENSE-2.0).

The OpenEEmeter code can be viewed, downloaded, forked, and contributed to at: [~~https://github.com/openeemeter/eemeter/releases​~~](https://github.com/openeemeter/eemeter/releases)

A detailed set of documentation is maintained at: [~~https://www.recurve.com/open-source/how-it-works~~](https://www.recurve.com/open-source/how-it-works)

## PHASE III

At the end of 2015, PG&E reconvened the CalTRACK working group to further refine current methods, and the OpenEEMeter implementation of those methods for use in the AHU program, and P4P Pilots. It was decided that the best process for testing the CalTRACK methods and the OpenEEMeter code base would be through a multiparty beta test using real past AHU meter data. The beta test[^1] plan that was agreed to by the working group can be found [~~here~~](http://www.caltrack.org/caltrack-beta-test-plan.html).

The objectives (and exclusions) were listed in the plan as:

1. Empirically test the draft CalTRACK requirements to verify assumptions made by the technical working group in drafting the protocols and identify necessary changes.
2. Analyze the sensitivity of CalTRACK methods to different software implementations and provide additional technical guidance to future software implementers as needed.

[^1]: It is important to note that the beta test is not a test of equivalency and is not being used to certify software. It is merely a test of the agreed to methods through implementations of methods for use in CalTRACK in order to adjust site energy savings and feedback to contractors on site savings.

The working group, and three beta testers, spent approximately 7 months executing on the Beta Process resulting in a narrowing of the variance between outcomes and generating a set of extremely detailed specifications that were the work product of all three firms involved.

* [~~Data Preparation~~](https://github.com/impactlab/caltrack-betatest/tree/master/data-prep)
* [~~Monthly Analysis Methods~~](https://github.com/impactlab/caltrack-betatest/blob/master/analysis/monthly/Site-level_Monthly_Gross_Savings_Analysis_Methods.ipynb)
* [~~Savings Aggregation~~](https://github.com/impactlab/caltrack-betatest/blob/master/aggregation/Portfolio_savings_aggregation_methods.ipynb)
* [~~GitHub Repo with all BETA Code and Results~~](https://github.com/impactlab/caltrack-betatest)
* [~~Complete Open Source CODE for CalTRACK / OpenEEMeter~~](https://github.com/openeemeter/eemeter)

These work products are to a level of specificity that is unique in M&V.  The project has now evolved from pseudo code to actual code, which is provided in the complete and functioning OpenEEMeter.  

## PHASE IV

In 2018 the CalTRACK development process resumed with consideration of version 2.0.

The effort was initiated and led by [Recurve](http://www.recurve.com/), with participation from the California Energy Commission, the New York State Energy Research and Development Authority (NYSERDA), the Energy Trust of Oregon, and other stakeholders to define a new set of guidelines under the framework of CalTRACK 2.0.

​This new version of the CalTRACK framework included updates to existing CalTRACK methods as well as the development of methods and policy guidance for hourly savings, portfolio load shape, and non-residential sectors. These updates further aligned the CalTRACK framework with the needs and requirements of pay-for-performance programs, energy efficiency procurement, and market development.   

[Nearly 100 experts](http://www.caltrack.org/technical-working-group.html) representing advocates, utilities, regulators, implementers, evaluators and academic researchers participated in the CalTRACK 2.0 process.

Regularly held working group meetings provided a forum to present issues, propose test methods, present results and debate and settle on final methods.  These are documented in the CalTRACK GitHub repository as well as in the archives of the “[Project Status](http://www.caltrack.org/project-updates/quick-links-to-the-2018-project-updates)” blog posts from that period.

<figure style="margin-top: 2em">
  <div style="line-height: 1em;">
    <strong>CalTRACK Continuous Improvement Pathway</strong>
    <img src="site:assets/images/history/caltrack_improvement_pathway.png" alt="CalTRACK continuous improvement pathway">
  </div>
</figure>

## PHASE V

In early 2019, the [~~Energy Market Methods Consortium (EM2)~~](https://www.energymarketmethods.org/) was formed to govern the CalTRACK process as well two related working groups.

Building on the earlier collaboration of CalTRACK, the Energy Market Methods Consortium (EM2)​ is focused on representation from industry stakeholders who are committed to collaboration on methods designed to reduce the costs of scaling demand-side energy programs and procurements.

The methods development process, including CalTRACK, is split into multiple working groups, each representing a core challenge in the development of scalable energy markets. The core tenets uniting the methods development processes are transparency, empirical testing, and consensus.

The Steering Committee is composed of organizations currently using the CalTRACK methods in their pay for performance programs, and vendors who are paid on the basis of these results. Members in EM2 can participate in any working group. EM2 is a organized under the [Joint Development Foundation](http://www.jointdevelopment.org/), an affiliate of the [Linux Foundation Energy](https://www.lfenergy.org/) project. Governance is described in the charter documents and enforced by the rules of the JDF.