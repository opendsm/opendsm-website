---
date: 2024-10-11
description: Latest OpenEEmeter developments optimize handling of solar and non-solar data with elastic net approach, incorporating solar irradiance for better accuracy and computational efficiency.
---

# OpenEEmeter Technical Working Group Meeting Summary | October 1, 2024

Thanks to everyone who joined the most recent OpenEEmeter Working Group Meeting.

In this meeting, the group discussed the latest developments and optimizations for the OpenEEmeter in handling both solar and non-solar data. The meeting began with a recap of progress so far. Adam Scheer reviewed the development of the hourly model and associated documentation, noting significant progress and ongoing work to finalize and document new models.

Travis Sikes then explained how changes in the model handle hourly data better, including the incorporation of solar irradiance (GHI) for more accurate modeling of solar PV customers, and how the new model uses an elastic net approach to optimize computational efficiency and incorporate various input data.

There was a discussion of challenges such as temperature bias and how the model requires interpolation to handle missing data. The discussion concluded with a comparison of the new models against CalTRACK 2.0. The new model significant improvements in computational efficiency and better handling of solar data.

The team also compared the idea of using two models, one for data without solar and one with solar included, versus a joint model. They concluded that the joint model effectively combines the capability of handling both solar and non-solar customers without needing two separate models. This greatly simplifies implementation and maintenance.

The meeting ended with a discussion of next steps, including finalizing model validation, incorporating feedback, and updating and completing any necessary documentation.

Watch the complete meeting below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/ocLa3U8He70" frameborder="0" allowfullscreen></iframe>
