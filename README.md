# plutils

A collection of matplotlib utilities for creating publication-quality plots.

## Installation

Install the package in development mode:

```bash
pip install -e .
```

## Testing

Run the test suite:

```bash
pytest test_plutils.py -v
```

## Features

- `save_single_ax`: Save a single axis with customizable plot size and legend placement
- `save_multiple_axes`: Save multiple axes in a grid layout with consistent sizing
- `reset_mpl_style`: Reset matplotlib style to default settings

## Example Usage

```python
import matplotlib.pyplot as plt
import numpy as np
from plutils import save_single_ax, save_multiple_axes

# Single axis plot
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)')
save_single_ax(ax, 'plot.png', plot_size=(4, 3), legend_out=True)

# Multiple axes plot
fig, axs = plt.subplots(2, 2)
for ax in axs.flat:
    ax.plot(x, np.sin(x))
save_multiple_axes(axs.flat, 'grid.png', grid_size=(2, 2), plot_size=(4, 3))
```
