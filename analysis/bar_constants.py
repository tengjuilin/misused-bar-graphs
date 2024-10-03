# system
import os
import warnings
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm
import scipy

# plot settings
def set_plot_rc():
    plt.rcParams.update({
        'font.family': 'Arial',  # Times New Roman, Calibri
        'font.weight': 'normal',
        'mathtext.fontset': 'stixsans',
        'font.size': 14,

        'lines.linewidth': 2,

        'axes.linewidth': 2,
        'axes.spines.top': True,
        'axes.spines.right': True,
        'axes.titleweight': 'bold',
        'axes.titlesize': 14,
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
        'legend.fontsize': 12,

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

# directory components and paths
# # top level directory path
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))  # one level up
# # level 1 directory component
DATA_DIR = "data"
FIG_DIR = 'figures'
# # level 1 directory path
DATA_PATH = os.path.join(PROJECT_PATH, DATA_DIR)
FIG_PATH = os.path.join(PROJECT_PATH, FIG_DIR)
# # level 2 directory component
MISUSED_BAR_DATA_DIR = "misused_bar_graph_data"
MISUSED_BAR_FIG_DIR = "misused_bar_graph_figures"
PROCESSED_DATA_DIR = 'processed_data'
ZOTERO_DIR = "zotero_data"
FIG_ARTICLE_SUBPANELS_DIR = 'article-subpanels'
FIG_POSTER_DIR = 'poster-figures'
FIG_GENERAL_SUBPANELS_DIR = 'general-subpanels'
# # level 2 directory path
MISUSED_BAR_DATA_PATH = os.path.join(DATA_PATH, MISUSED_BAR_DATA_DIR)
MISUSED_BAR_FIG_PATH = os.path.join(DATA_PATH, MISUSED_BAR_FIG_DIR)
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, PROCESSED_DATA_DIR)
ZOTERO_PATH = os.path.join(DATA_PATH, ZOTERO_DIR)
FIG_ARTICLE_SUBPANELS_PATH = os.path.join(FIG_PATH, FIG_ARTICLE_SUBPANELS_DIR)
FIG_POSTER_PATH = os.path.join(FIG_PATH, FIG_POSTER_DIR)
FIG_GENERAL_SUBPANELS_PATH = os.path.join(FIG_PATH, FIG_GENERAL_SUBPANELS_DIR)
# # level 3 directory component
ARTICLE_CAT_SUBDIR = 'article_categorization'
DISTORTION_METRIC_SUBDIR = 'data_distortion_metrics'
LOG_SUBDIR = 'log'
ZERO_SUBDIR = 'zero'
OTHERS_SUBDIR = 'others'

# experimental groups
ZERO_LABEL = 'Zeroing'
LOG_LABEL = 'Log'
OTHERS_LABEL = 'Others'

# zotero column labels (fixed by zotero export)
MANUAL_TAGS_LABEL = 'Manual Tags'
PUBLICATION_LABEL = 'Publication Title'

# zotero manual tag labels
NO_BAR_GRAPH_REGEX_LABEL = 'No bar'
NO_MISUSE_REGEX_LABEL = 'No problem'
HAS_MISUSE_REGEX_LABEL = 'Zero|Log|Other'
ZERO_PROBLEM_REGEX_LABEL = 'Zero'
LOG_PROBLEM_REGEX_LABEL = 'Log'
OTHER_PROBLEM_REGEX_LABEL = 'Other'

# article df column labels
HAS_BAR_GRAPH_LABEL = 'Has Bar Graph'
NO_MISUSE_LABEL = 'Has Bar Graph, No Misuse'
HAS_MISUSE_LABEL = 'Has Bar Graph, Has Misuse'
ZERO_PROBLEM_LABEL = 'Zero Problem'
LOG_PROBLEM_LABEL = 'Log Problem'
OTHER_PROBLEM_LABEL = 'Other Problem'
NUM_AUTHORS_LABEL = 'Number of Authors'

# article statistics df column labels
NUM_ARTICLES_LABEL = 'Total number of articles'
NUM_ARTICLES_WITH_BAR_GRAPH_LABEL = 'Number of articles with bar graphs'
NUM_ARTICLES_WITHOUT_BAR_GRAPH_LABEL = 'Number of articles without bar graphs'
NUM_ARTICLES_CORRECT_BAR_GRAPH_LABEL = 'Number of articles with correct bar graphs'
NUM_ARTICLES_INCORRECT_BAR_GRAPH_LABEL = 'Number of articles with incorrect bar graphs'
NUM_ARTICLES_ZERO_PROBLEM_LABEL = 'Number of articles with nonzero bar graph y-min'
NUM_ARTICLES_LOG_PROBLEM_LABEL = 'Number of articles with logarithmic bar graph y axis'
NUM_ARTICLES_OTHER_PROBLEM_LABEL = 'Number of articles with other bar graph misrepresentations'
PERCENT_ARTICLES_WITH_BAR_GRAPH_LABEL = 'Percentage of articles with bar graphs'
PERCENT_ARTICLES_WITHOUT_BAR_GRAPH_LABEL = 'Percentage of articles without bar graphs'
PERCENT_ARTICLES_CORRECT_BAR_GRAPH_LABEL = 'Percentage of articles with correct bar graphs'
PERCENT_ARTICLES_INCORRECT_BAR_GRAPH_LABEL = 'Percentage of articles with incorrect bar graphs'
PERCENT_ARTICLES_ZERO_PROBLEM_LABEL = 'Percentage of articles with nonzero bar graph y-min'
PERCENT_ARTICLES_LOG_PROBLEM_LABEL = 'Percentage of articles with logarithmic bar graph y axis'
PERCENT_ARTICLES_OTHER_PROBLEM_LABEL = 'Percentage of articles with other bar graph misrepresentations'
TOTAL_LABEL = 'Total'

# color scheme
ARTICLES_WITH_BAR_GRAPH_COLOR = 'navy'
ARTICLES_WITHOUT_BAR_GRAPH_COLOR = 'lightgray'
ARTICLES_INCORRECT_BAR_GRAPH_COLOR = 'royalblue'
ARTICLES_CORRECT_BAR_GRAPH_COLOR = 'lightgray'
ARTICLES_ZERO_PROBLEM_COLOR = 'lightcoral'
ARTICLES_LOG_PROBLEM_COLOR = 'mediumslateblue'
ARTICLES_OTHER_PROBLEM_COLOR = 'goldenrod'

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
SAMPLE_SIZE = 1000

# file extensions
EXCEL_FILEEXT = '.xlsx'
CSV_FILEEXT = '.csv'
PDF_FILEEXT = '.pdf'

# file suffix
VIZ_LABEL = 'viz'
VAL_LABEL = 'val'

# journal names
JOURNALS = [
    'acs_nano',
    'bioeng_transl_med',
    'cell',
    'nat_biomed_eng',
    'nat_biotechnol',
    'nat_cancer',
    'nat_cell_biol',
    'nat_nanotechnol',
    'nat_neurosci',
    'nat_plants',
    'nature',
    'sci_immunol',
    'sci_signal',
    'sci_transl_med',
    'science',
]
MISTAKES = [ZERO_SUBDIR, LOG_SUBDIR]

# DATA FILES
# filenames
articles_df_filename = 'articles_df'
articles_stat_df_filename = 'articles_stat_df'
percent_bar_df_filename = 'percent_bar_df'
percent_bar_correct_df_filename = 'percent_bar_correct_df'
percent_bar_incorrect_df_filename = 'percent_bar_incorrect_df'
num_total_articles_series_filename = 'num_total_articles_series'
num_articles_bar_graph_series_filename = 'num_articles_bar_graph_series'
num_articles_misused_bar_graph_series_filename = 'num_articles_misused_bar_graph_series'
bar_annot_df_filename = 'bar_annot_df'
bar_val_df_filename = 'bar_val_df'
L_df_filename = 'L_df'
cv_df_filename = 'cv_df'

# filename with extensions
articles_df_filename_full = articles_df_filename + CSV_FILEEXT
articles_stat_df_filename_full = articles_stat_df_filename + CSV_FILEEXT
percent_bar_df_filename_full = percent_bar_df_filename + CSV_FILEEXT
percent_bar_correct_df_filename_full = percent_bar_correct_df_filename + CSV_FILEEXT
percent_bar_incorrect_df_filename_full = percent_bar_incorrect_df_filename + CSV_FILEEXT
num_total_articles_series_filename_full = num_total_articles_series_filename + CSV_FILEEXT
num_articles_bar_graph_series_filename_full = num_articles_bar_graph_series_filename + CSV_FILEEXT
num_articles_misused_bar_graph_series_filename_full = num_articles_misused_bar_graph_series_filename + CSV_FILEEXT
bar_annot_df_filename_full = bar_annot_df_filename + CSV_FILEEXT
bar_val_df_filename_full = bar_val_df_filename + CSV_FILEEXT
L_df_filename_full = L_df_filename + CSV_FILEEXT
cv_df_filename_full = cv_df_filename + CSV_FILEEXT

# full filepath
articles_df_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, articles_df_filename_full)
articles_stat_df_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, articles_stat_df_filename_full)
percent_bar_df_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, percent_bar_df_filename_full)
percent_bar_correct_df_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, percent_bar_correct_df_filename_full)
percent_bar_incorrect_df_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, percent_bar_incorrect_df_filename_full)
num_total_articles_series_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, num_total_articles_series_filename_full)
num_articles_bar_graph_series_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, num_articles_bar_graph_series_filename_full)
num_articles_misused_bar_graph_series_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, num_articles_misused_bar_graph_series_filename_full)
bar_annot_df_filepath = os.path.join(PROCESSED_DATA_PATH, ARTICLE_CAT_SUBDIR, bar_annot_df_filename_full)
bar_val_df_filepath = os.path.join(PROCESSED_DATA_PATH, DISTORTION_METRIC_SUBDIR, bar_val_df_filename_full)
L_df_filepath = os.path.join(PROCESSED_DATA_PATH, DISTORTION_METRIC_SUBDIR, L_df_filename_full)
cv_df_filepath = os.path.join(PROCESSED_DATA_PATH, DISTORTION_METRIC_SUBDIR, cv_df_filename_full)


def get_figure_filepath(filename, loc=FIG_GENERAL_SUBPANELS_PATH):
    return os.path.join(loc, filename + PDF_FILEEXT)

# FIGURE FILES
# filenames
# # `bar-graph-classification-viz-article`
article_categorization_filename = 'fig-1abc-article-stat'
graph_bias_mitigation_filename = 'graph-bias-mitigation'
author_num_correlation_filename = 'ex-fig-6-author-number-correlation'
title_length_correlation_filename = 'title-length-correlation'

# # `data-distortion-quantification`
data_distortion_metrics_main_filename = 'fig-1defghi-data-distortion-metrics-main'
data_distortion_metrics_filename = 'data-distortion-metrics'
data_distortion_metrics_abs_rel_filename = 'data-distortion-metrics-by-abs-rel'
data_distortion_metrics_measurand_ii_filename = 'ex-fig-8abcde-data-distortion-metrics-by-measurand-ii'
data_distortion_metrics_measurand_i_filename = 'data-distortion-metrics-by-measurand-i'
data_distortion_metrics_journals_filename = 'ex-fig-8fghij-data-distortion-metrics-by-journals'
lie_factor_correlation_filename = 'ex-fig-7-lie-factor-correlation'

# # `bar-graph-examples`
example_zeroing_mistake_filename = 'ex-fig-1-zeroing-mistake'
example_log_mistake_numerical_filename = 'ex-fig-2-log-mistake-numerical'
example_log_mistake_ratio_rel_filename = 'ex-fig-3-log-mistake-ratio-relative'
example_log_mistake_ratio_abs_filename = 'ex-fig-4-log-mistake-ratio-absolute'
example_single_value_filename = 'ex-fig-5-single-value'
example_decision_tree_result_filename = 'ex-fig-9-decision-tree-result-example'
example_bar_graph_guideline_filename = 'fig-2e-bar-graph-guideline'
example_stacked_bar_graph_guideline_filename = 'stacked-bar-graph-guideline'

# # `polar-bar-graphs`
circular_bar_graph_filename = 'ex-fig-10abc-circular-bar-graphs'
radial_bar_graph_filename = 'ex-fig-10def-radial-bar-graphs'