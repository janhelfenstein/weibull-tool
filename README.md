#readme
This tool is helpful for visualizing Weibull distributions based on 3 parameters:
b: form parameter
T: characteristic life (failure probability of 63.2%)
t0: failure free time (failure probability of 0.0%)

Failure probability function:
F(t) = 1 - exp(-((t-t0)/(T-t0))^b)

We use Weibull function to give a mathematic model based on our historical, statistical data. We have llimited data from inspections (pass/fail results), so the mathematic model is here to approximate how failure probability increases as life time increases.

Use the sliders to adjust values of parameters b, T, t0 to visualize how the shape of the function changes.
