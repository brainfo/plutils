# plutils

A collection of matplotlib utilities for creating publication-quality plots.

## Installation

Install the package from github (uv):

```bash
uv pip install git+https://github.com/brainfo/plutils.git
```

## Features

- `save_single_ax`: Save a single axis with customizable plot size and legend placement
- `save_multiple_axes`: Save multiple axes in a grid layout with consistent sizing
- `reset_mpl_style`: Reset matplotlib style to default settings or given matplotlibrc

## Example Usage

```python
import matplotlib.pyplot as plt
import numpy as np
import plutils plu

plu.reset_mpl_style()
fig_size = [7.09, 6.69]
# Single axis plot
## for any given axes object ax, or from Figure object fig: fig.axes[0]
plu.save_single_ax(ax, 'plot.pdf', plot_size=(fig_size[0]/4, fig_size[1]/8), legend_out=True, right_pad_frac=0.3)

# Multiple axes plot
## for example if start with Figure object fig
axs = fig.axes
plu.save_multiple_axes(axs, 'grid.pdf', grid_size=(2, 2), plot_size=(fig_size/4, fig_size/8))
```
