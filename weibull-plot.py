# weibull 2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def weibull_cdf(t, t0, T, b):
    """
    Weibull CDF:
    F(t) = 1 - exp(-((t-t0)/T)^b)

    F(t) = 0 for t < t0
    """
    F = np.zeros_like(t, dtype=float)

    valid = t >= t0
    F[valid] = 1 - np.exp(-((t[valid] - t0) / (T-t0))** b)

    return F


# Initial values
t0_init = 15000
b_init = 2.0
T_init = 25000

# x-axis
t = np.linspace(0, 80000, 2000)

# Initial curve
F = weibull_cdf(t, t0_init, T_init, b_init)

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.30)

line, = ax.plot(t, F, lw=2)

ax.set_title("Weibull CDF")
ax.set_xlabel("Flight Hours")
ax.set_ylabel("Failure Probability")
ax.set_ylim(0, 1.05)
ax.set_xlim(0, 80000)
ax.grid(True)

# Slider axes
ax_t0 = plt.axes([0.15, 0.18, 0.70, 0.03])
ax_b  = plt.axes([0.15, 0.12, 0.70, 0.03])
ax_T  = plt.axes([0.15, 0.06, 0.70, 0.03])

# Sliders
slider_t0 = Slider(
    ax=ax_t0,
    label='t0',
    valmin=10000,
    valmax=25000,
    valinit=t0_init,
    valstep=100
)

slider_b = Slider(
    ax=ax_b,
    label='b',
    valmin=0.5,
    valmax=22.0,
    valinit=b_init,
    valstep=0.1
)

slider_T = Slider(
    ax=ax_T,
    label='T',
    valmin=18000,
    valmax=35000,
    valinit=T_init,
    valstep=100
)


def update(val):
    t0 = slider_t0.val
    b = slider_b.val
    T = slider_T.val

    F = weibull_cdf(t, t0, T, b)

    line.set_ydata(F)

    ax.set_title(
        f"Weibull CDF   t0={t0:.0f},  b={b:.1f},  T={T:.0f}"
    )

    fig.canvas.draw_idle()


slider_t0.on_changed(update)
slider_b.on_changed(update)
slider_T.on_changed(update)

plt.show()