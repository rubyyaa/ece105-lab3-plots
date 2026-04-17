# Sensor Data Plot Generation

Standalone Python workflow that generates synthetic two-sensor temperature data and saves a three-panel analysis figure.

## Installation

Activate your `ece105` conda environment:

```bash
conda activate ece105
```

Install dependencies with either `conda` or `mamba`:

```bash
conda install numpy matplotlib
```

```bash
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example Output

The script creates a 1x3 figure with the following plots:

1. Scatter plot of Sensor A and Sensor B temperature readings versus timestamps.
2. Overlaid histograms (30 bins) for Sensor A and Sensor B, including dashed mean lines.
3. Side-by-side box plot comparing Sensor A and Sensor B, including a dashed overall-mean line.

### Output files

- `sensor_analysis.png`: Saved at 150 DPI with a tight bounding box.

## AI tools used and disclosure

This section is intentionally left as a placeholder. Add your disclosure text here describing any AI tools you used, what they were used for, and how you verified or edited the generated content.