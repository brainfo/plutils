from pathlib import Path
import matplotlib as mpl

def reset_mpl_style(rcfile=None):
    """
    Reset matplotlib style to default, optionally loading a different rc file.
    """
    if rcfile is not None:
        mpl.rc_file(rcfile)
    else:
        mpl.rcParams.update(mpl.rcParamsDefault)
        mpl.rcParams["figure.autolayout"] = False       # kills implicit tight_layout
        mpl.rcParams["figure.constrained_layout.use"] = False

def save_single_ax(ax, out, *, plot_size=(4, 3), dpi=400,
                   legend_out=True, right_pad_frac=0.3, xlabel=None, ylabel=None):
    """
    Save `ax` so the *data pane* is exactly plot_size (inches).

    ax.figure is resized automatically; legend can be pushed outside.
    """
    w, h = plot_size
    left, bottom = 0, 0
    right_pad = w * right_pad_frac if legend_out else 0
    fig_w, fig_h = w + right_pad, h
    fig = ax.figure
    fig.set_size_inches(fig_w, fig_h)

    # enforce axes rectangle
    ax.set_position([left/fig_w, bottom/fig_h, w/fig_w, h/fig_h])

    if legend_out:
        ax.legend(loc="center left",
                  bbox_to_anchor=(1, 0.5),
                  bbox_transform=fig.transFigure)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight", dpi=dpi)


def save_multiple_axes(axs, out, *, grid_size, plot_size=(4, 3), dpi=400,
                       xlabels=None, ylabels=None):
    """
    `axs` is a flat list; `grid_size` is (n_rows, n_cols).

    Every data pane keeps plot_size inches; margins auto-sized.
    """
    n_rows, n_cols = grid_size
    w, h = plot_size
    fig_w, fig_h = w * n_cols, h * n_rows
    fig = axs[0].figure
    fig.set_size_inches(fig_w, fig_h)

    for i, ax in enumerate(axs):
        r, c = divmod(i, n_cols)
        ax.set_position([(c*w)/fig_w,               # left
                         1 - (r+1)*h/fig_h,         # bottom (origin top-left)
                         w/fig_w, h/fig_h])
        if xlabels is not None:
            ax.set_xlabel(xlabels[i])
        if ylabels is not None:
            ax.set_ylabel(ylabels[i])

    fig.savefig(out, bbox_inches="tight", dpi=dpi)
