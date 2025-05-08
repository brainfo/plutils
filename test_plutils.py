import pytest
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from plutils import save_single_ax, save_multiple_axes, reset_mpl_style

@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for test outputs."""
    return tmp_path

@pytest.fixture
def single_ax_figure():
    """Create a figure with a single axis for testing."""
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x), label='sin(x)')
    return fig, ax

@pytest.fixture
def multiple_axes_figure():
    """Create a figure with multiple axes for testing."""
    fig, axs = plt.subplots(2, 2)
    x = np.linspace(0, 10, 100)
    for ax in axs.flat:
        ax.plot(x, np.sin(x))
    return fig, axs.flat  # Return flattened array of axes

def test_save_single_ax_with_legend(temp_dir, single_ax_figure):
    """Test saving a single axis with legend outside."""
    fig, ax = single_ax_figure
    out_path = temp_dir / "test_single_ax.png"
    
    save_single_ax(ax, out_path, plot_size=(4, 3), legend_out=True)
    
    assert out_path.exists()
    assert out_path.stat().st_size > 0

def test_save_single_ax_without_legend(temp_dir, single_ax_figure):
    """Test saving a single axis without legend."""
    fig, ax = single_ax_figure
    out_path = temp_dir / "test_single_ax_no_legend.png"
    
    save_single_ax(ax, out_path, plot_size=(4, 3), legend_out=False)
    
    assert out_path.exists()
    assert out_path.stat().st_size > 0

def test_save_single_ax_with_labels(temp_dir, single_ax_figure):
    """Test saving a single axis with custom labels."""
    fig, ax = single_ax_figure
    out_path = temp_dir / "test_single_ax_labels.png"
    
    save_single_ax(ax, out_path, 
                  plot_size=(4, 3),
                  xlabel="X Axis",
                  ylabel="Y Axis")
    
    assert out_path.exists()
    assert out_path.stat().st_size > 0

def test_save_multiple_axes(temp_dir, multiple_axes_figure):
    """Test saving multiple axes in a grid."""
    fig, axs = multiple_axes_figure
    out_path = temp_dir / "test_multiple_axes.png"
    
    save_multiple_axes(axs, out_path, 
                      grid_size=(2, 2),
                      plot_size=(4, 3))
    
    assert out_path.exists()
    assert out_path.stat().st_size > 0

def test_save_multiple_axes_with_labels(temp_dir, multiple_axes_figure):
    """Test saving multiple axes with custom labels."""
    fig, axs = multiple_axes_figure
    out_path = temp_dir / "test_multiple_axes_labels.png"
    
    xlabels = ["X1", "X2", "X3", "X4"]
    ylabels = ["Y1", "Y2", "Y3", "Y4"]
    
    save_multiple_axes(axs, out_path,
                      grid_size=(2, 2),
                      plot_size=(4, 3),
                      xlabels=xlabels,
                      ylabels=ylabels)
    
    assert out_path.exists()
    assert out_path.stat().st_size > 0

def test_reset_mpl_style():
    """Test resetting matplotlib style."""
    # First change some style parameters
    plt.rcParams['figure.figsize'] = [10, 10]  # Use list instead of tuple
    plt.rcParams['figure.dpi'] = 200
    
    # Reset to default
    reset_mpl_style()
    
    # Check if parameters are reset
    assert plt.rcParams['figure.figsize'] == [6.4, 4.8]  # Compare with list
    assert plt.rcParams['figure.dpi'] == 100  # default dpi 