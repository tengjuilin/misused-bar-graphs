# system
from bar_constants import *

# import unfiltered data
articles_df = pd.read_csv(articles_df_filepath, index_col=0)
articles_stat_df = pd.read_csv(articles_stat_df_filepath, index_col=0)
percent_bar_df = pd.read_csv(percent_bar_df_filepath, index_col=0)
percent_bar_correct_df = pd.read_csv(percent_bar_correct_df_filepath, index_col=0)
percent_bar_incorrect_df = pd.read_csv(percent_bar_incorrect_df_filepath, index_col=0)
num_total_articles_series = pd.read_csv(num_total_articles_series_filepath, index_col=0).iloc[:, 0]
num_articles_bar_graph_series = pd.read_csv(num_articles_bar_graph_series_filepath, index_col=0).iloc[:, 0]
num_articles_misused_bar_graph_series = pd.read_csv(num_articles_misused_bar_graph_series_filepath, index_col=0).iloc[:, 0]