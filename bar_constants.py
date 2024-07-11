# system
import os
import warnings
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# plot settings
def set_plot_rc():
    plt.rcParams.update({
        'font.family': 'Arial',  # Times New Roman, Calibri
        'font.weight': 'normal',
        'mathtext.fontset': 'stixsans',
        'font.size': 18,

        'lines.linewidth': 2,

        'axes.linewidth': 2,
        'axes.spines.top': True,
        'axes.spines.right': True,
        'axes.titleweight': 'bold',
        'axes.titlesize': 18,
        'axes.labelweight': 'bold',

        'xtick.major.size': 8,
        'xtick.major.width': 2,
        'ytick.major.size': 8,
        'ytick.major.width': 2,

        'figure.dpi': 80,
        'savefig.dpi': 300,

        'legend.framealpha': 1,
        'legend.edgecolor': 'black',
        'legend.fancybox': False,
        'legend.fontsize': 14,

        'animation.html': 'html5',
        'pdf.fonttype': 42,
    })


def set_save_fig_rc():
    plt.rcParams.update({
        'font.family': 'Arial',  # Times New Roman, Calibri
        'font.weight': 'normal',
        'mathtext.fontset': 'stixsans',
        'font.size': 12,

        'lines.linewidth': 1,

        'axes.linewidth': 1,
        'axes.spines.top': True,
        'axes.spines.right': True,
        'axes.titleweight': 'normal',
        'axes.titlesize': 12,
        'axes.labelweight': 'normal',

        'xtick.major.size': 4,
        'xtick.major.width': 1,
        'ytick.major.size': 4,
        'ytick.major.width': 1,

        'figure.dpi': 80,
        'savefig.dpi': 600,

        'legend.framealpha': 1,
        'legend.edgecolor': 'black',
        'legend.fancybox': False,
        'legend.fontsize': 10,

        'animation.html': 'html5',
        'pdf.fonttype': 42,
    })



# def set_plot_rc():
#     plt.rcParams.update({
#         'font.family': 'Arial',  # Times New Roman, Calibri
#         'font.weight': 'normal',
#         'mathtext.fontset': 'stixsans',
#         'font.size': 18,
#
#         'lines.linewidth': 2,
#
#         'axes.linewidth': 2,
#         'axes.spines.top': True,
#         'axes.spines.right': True,
#         'axes.titleweight': 'bold',
#         'axes.titlesize': 18,
#         'axes.labelweight': 'bold',
#
#         'xtick.major.size': 8,
#         'xtick.major.width': 2,
#         'ytick.major.size': 8,
#         'ytick.major.width': 2,
#
#         'xtick.minor.size': 4,
#         'xtick.minor.width': 1,
#         'ytick.minor.size': 4,
#         'ytick.minor.width': 1,
#
#         'xtick.labelsize': 14,
#         'ytick.labelsize': 14,
#
#         'figure.dpi': 80,
#         'savefig.dpi': 300,
#
#         'legend.framealpha': 0,
#         'legend.edgecolor': 'black',
#         'legend.fancybox': False,
#         'legend.fontsize': 12,
#
#         'animation.html': 'html5',
#         'pdf.fonttype': 42,
#     })


set_plot_rc()
warnings.filterwarnings("ignore")

DATA_DIR = "data"
ZOTERO_DIR = "zotero_data"
MISUSED_BAR_DIR = "misused_bar_graph_data"
LOG_SUBDIR = 'log'
ZERO_SUBDIR = 'zero'
OTHERS_SUBDIR = 'others'

# plot settings
SWARM_LINEWIDTH = 1
SWARM_MARKERSIZE = 4
SWARM_COLOR = 'w'
SWARM_EDGECOLOR = 'k'
BAR_ERRORBAR = 'sd'
BAR_LINEWIDTH = 0
BAR_CAPSIZE = 0.25
BAR_EDGECOLOR = 'k'
BAR_ALPHA = 0.7
BAR_WIDTH = 0.8

# generate data
np.random.seed(0)
SAMPLE_SIZE = 10

# file extensions
EXCEL_FILEEXT = '.xlsx'
CSV_FILEEXT = '.csv'

# file suffix
VIZ_LABEL = 'viz'
VAL_LABEL = 'val'

# filenames
bar_classification_filename = "bar-graph-classification"
bar_classification_sorted_filename = "bar-graph-classification-sorted"

# filename with extensions
bar_classification_filename_full = bar_classification_filename + EXCEL_FILEEXT
bar_classification_sorted_filename_full = bar_classification_sorted_filename + EXCEL_FILEEXT

# full filepath
bar_classification_filepath = os.path.join(DATA_DIR, ZOTERO_DIR, bar_classification_filename_full)
bar_classification_sorted_filepath = os.path.join(DATA_DIR, ZOTERO_DIR, bar_classification_sorted_filename_full)
