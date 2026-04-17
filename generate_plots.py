"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.


def generate_data(seed):
    """Generate synthetic sensor temperature data and timestamps.

    Parameters
    ----------
    seed : int
        Seed used to initialize NumPy's random number generator for
        reproducible results.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of shape (200,) containing Sensor A temperature readings in
        degrees Celsius, sampled from a normal distribution with mean 25.0
        and standard deviation 3.0.
    sensor_b : numpy.ndarray
        Array of shape (200,) containing Sensor B temperature readings in
        degrees Celsius, sampled from a normal distribution with mean 27.0
        and standard deviation 4.5.
    timestamps : numpy.ndarray
        Array of shape (200,) containing timestamps in seconds sampled
        uniformly from 0.0 to 10.0.
    """
    rng = np.random.default_rng(seed)
    n_readings = 200

    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n_readings)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n_readings)
    timestamps = rng.uniform(low=0.0, high=10.0, size=n_readings)

    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor temperature readings versus time on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of shape (200,) with Sensor A temperature readings in
        degrees Celsius.
    sensor_b : numpy.ndarray
        Array of shape (200,) with Sensor B temperature readings in
        degrees Celsius.
    timestamps : numpy.ndarray
        Array of shape (200,) with timestamp values in seconds.
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes to draw the scatter plot on. The axes are
        modified in place.

    Returns
    -------
    None
        This function updates ``ax`` directly and does not create or return
        a new figure or axes.
    """
    ax.scatter(
        timestamps,
        sensor_a,
        color="tab:blue",
        alpha=0.75,
        s=28,
        label="Sensor A",
    )
    ax.scatter(
        timestamps,
        sensor_b,
        color="tab:orange",
        alpha=0.75,
        s=28,
        label="Sensor B",
    )

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (\N{DEGREE SIGN}C)")
    ax.set_title("Sensor Temperature vs Time")
    ax.legend()
    ax.grid(alpha=0.25)

    return None

