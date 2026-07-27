---
date: 2024-08-26
description: OpenEEmeter working group discusses completed documentation, 24-hour hourly model approach, bias correction strategies, and new daily usage pattern clustering module.
---

# OpenEEmeter Technical Working Group Meeting Summary | August 6, 2024

Thanks to everyone who joined the most recent OpenEEmeter Working Group Meeting.

The meeting began with a discussion of the documentation that has been developed for all of the OpenEEmeter. This documentation can be accessed at the [OpenEEmeter GitHub site](https://openeemeter.github.io/eemeter/).

Documentation is complete for the daily and billing models, and will soon be completed for the hourly model.

Travis Sikes then gave a recap of previous meetings, and addressed a question that came up regarding a change from the OpenEEmeter 3.0 hourly model, which output for each individual hour, to the OpenEEmeter 4.1 hourly model, which outputs 24 hours at a time. Travis explained that this is because with the elastic net approach, each day must have a complete set of features (data) or it must be excluded from the data set.

Armin Aligholian followed up with a more detailed discussion of the 24 hour approach, explaining that it is both faster and yields improved prediction over the individual hour approach.

Armin then went into the question of how to fix bias (the difference between observed and modeled). Fixing this bias is important, is it was slightly larger than the previous model. Armin explained that there were two approaches to fixing this bias--binning by temperature, and linearizing temperature response. He then gave a detailed explanation of how temperature binning works.

Armin then discussed a new module, clustering daily usage patterns, and advantage of adding it. The main benefit of clustering is that it captures the behavior of each meter, speeds up the model, and reduces noise.

Travis then discussed progress in hyperparameter optimization.

The meeting concluded with a discussion of next steps, which include finishing the hyperparameter optimization and fulling integrating the hourly model into OpenEEmeter.

Watch the complete presentation below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/dJb0j_TgC5w" frameborder="0" allowfullscreen></iframe>
