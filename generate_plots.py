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

