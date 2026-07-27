---
date: 2024-07-04
description: OpenEEmeter working group proposes new umbrella naming convention, discusses autocorrelation interpolation, population-level model results, and strategies for fixing temperature bias.
---

# OpenEEmeter Technical Working Group Meeting Summary | July 2, 2024

Thanks to everyone who joined the most recent OpenEEmeter technical working group meeting.

In this meeting, the team proposed a new naming convention, in which there would be an umbrella term encompassing EEmeter, EEweather, and OpenEEmeter as submodules, along with the Recurve project GRIDmeter, which would be donated to LFEnergy.

The advantage of this approach is that it would allow much more flexibility in the future to add additional features to the library, without making the library focused entirely around AMI meter-based savings. It would also reduce duplicative work in updating functions that exist in more than one place.

After a recap of recent working group meetings, the discussion moved to recent work on interpolation, including changing the method to autocorrelation interpolation.

The conversation moved toward a discussion of population-level results, which has improved over the previous model, as well as bias in the model and approaches to fix it. The preferred approach to fixing this is through binning by temperature, with a second option of linearizing the temperature response, which would require multiple fits.

Next steps include fixing temperature bias (including determining if binning is sufficient or linearization is necessary), updating the objective function to include PNMBE, reoptimizing hyperparameters, and moving the hourly model fully into the OpenEEmeter.

Watch the full discussion below.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/aKFXCJbUeuI" frameborder="0" allowfullscreen></iframe>
