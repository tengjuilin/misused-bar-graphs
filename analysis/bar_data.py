# system
from bar_constants import *

# import article categorization data
try:
    articles_df = pd.read_csv(articles_df_filepath, index_col=0)
    articles_stat_df = pd.read_csv(articles_stat_df_filepath, index_col=0)
    percent_bar_df = pd.read_csv(percent_bar_df_filepath, index_col=0)
    percent_bar_correct_df = pd.read_csv(percent_bar_correct_df_filepath, index_col=0)
    percent_bar_incorrect_df = pd.read_csv(percent_bar_incorrect_df_filepath, index_col=0)
    num_total_articles_series = pd.read_csv(num_total_articles_series_filepath, index_col=0).iloc[:, 0]
    num_articles_bar_graph_series = pd.read_csv(num_articles_bar_graph_series_filepath, index_col=0).iloc[:, 0]
    num_articles_misused_bar_graph_series = pd.read_csv(num_articles_misused_bar_graph_series_filepath, index_col=0).iloc[:, 0]
    bar_annot_df = pd.read_csv(bar_annot_df_filepath, index_col=1)
except:
    print('Article categorization data not yet generated')

# import data distortion data
try:
    bar_val_df = pd.read_csv(bar_val_df_filepath, index_col=[0, 1])
    L_df = pd.read_csv(L_df_filepath, index_col=0)
    cv_df = pd.read_csv(cv_df_filepath, index_col=0)
except:
    print('Data distortion metric data not yet generated')