---
date: 2024-12-09
---

# November 19, 2024 | OpenEEmeter Technical Working Group Meeting — Wrap Up

Thanks to everyone who joined the most recent OpenEEmeter meeting!

After two years of collaborative development through the OpenEEmeter Working Group, we've made significant upgrades to the daily model and now we're approaching the final stages of another significant upgrade to the hourly model. The enhanced capabilities will improve how we measure the impact of demand-side resources across diverse conditions — particularly for customers with solar PV systems.

<!-- more -->

As part of these developments, OpenEEmeter is transitioning to become part of OpenDSM, a new project under Linux Foundation Energy. OpenDSM will serve as an umbrella project that includes not only OpenEEmeter but also GRIDmeter and EEweather, with the potential to add other open-source packages in the future. This organizational change will provide more flexibility and opportunities for collaboration across related energy analytics tools. The project has already unveiled a new logo that symbolizes demand-side management's core mission of reducing peak demand, with design elements representing both load curves and buildings.

In the most recent working group meeting, Travis Sikes presented the latest results from Version 5 of the new hourly model, which shows several key improvements over the earlier CalTRACK model:

- 10x faster processing speed with lower memory requirements
- 2-5% improvement in accuracy metrics for residential customers
- Similar levels of bias in high-temperature predictions
- Better handling of solar PV systems through incorporation of solar irradiance data
- More extensible framework that can accommodate additional variables

One particularly interesting finding is that the solar-enabled version of the model shows benefits even for non-solar customers, suggesting it could become the standard approach for all hourly analysis.

## Next Steps

The development team will:

1. Complete final hyperparameter optimization
2. Prepare a comprehensive report for community review
3. Make the code available for testing through the solar-hourly branch on GitHub
4. Collect feedback over a ~2 week period in early 2025
5. Barring any significant issues, proceed with formal acceptance of the new model

The working group meetings will pause while this review process takes place. Community members are encouraged to test the model on their own datasets and provide feedback before final acceptance.

We extend our sincere thanks to everyone who participated in the working group over the past two years. Your insights and feedback have been instrumental in creating a more robust and versatile tool for the energy efficiency and demand flexibility community.

Watch the complete meeting below.

<iframe src="https://www.youtube.com/embed/eDyR6xwAKl8" frameborder="0" allowfullscreen="" width="100%" height="400"></iframe>
