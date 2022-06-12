import logging

import numpy as np
import pandas as pd

logger = logging.getLogger('logger')


# getting random values x that becomes a normal distribution
# x~N(mu, sigma), amount of samples: x
def normal_distribution(mu, sigma, n):
    logger.info('about to get normal distribution variable')
    samples = mu + sigma * np.random.randn(n)
    logger.info('successfully got normal distribution variable')
    return samples


# getting basic statistics data: mean, std, min, max
def get_basic_statistics(data):
    logger.info('about to get the basic statistics')
    basic_stats_data = pd.DataFrame(
        {'x1': [np.mean(data['x1'])], 'x2': [np.mean(data['x2'])], 'x3': [np.mean(data['x3'])]}, index=['mean'])
    std_data = pd.Series({'x1': np.std(data['x1']), 'x2': np.std(data['x2']), 'x3': np.std(data['x3'])},
                         name='std')
    min_data = pd.Series({'x1': np.min(data['x1']), 'x2': np.min(data['x2']), 'x3': np.min(data['x3'])},
                         name='min')
    max_data = pd.Series({'x1': np.max(data['x1']), 'x2': np.max(data['x2']), 'x3': np.max(data['x3'])},
                         name='max')
    basic_stats_data = basic_stats_data.append(std_data)
    basic_stats_data = basic_stats_data.append(min_data)
    basic_stats_data = basic_stats_data.append(max_data)
    logger.info('successfully got basic statistics')
    return basic_stats_data


# getting frequency statistics data from nominal variable: freq, cumulative, percentage, cumulative percentage
def get_freq_statistics(data):
    logger.info('about to get the freq statistics')
    freq_stats = pd.DataFrame({'x3': [1, 2, 3, 4, 5, 6, 7]})
    freq_stats_count = data.x3.value_counts()
    freq_stats_count.sort_index(ascending=True, inplace=True)
    freq_stats['freq'] = freq_stats_count
    freq_stats.fillna(value=0, inplace=True)
    freq_stats['freq_sum'] = freq_stats.freq.cumsum()
    freq_stats_counts_all = sum(data.x3.value_counts())
    freq_stats.loc[freq_stats['freq'] >= 0, 'percent'] = freq_stats['freq'] / freq_stats_counts_all
    freq_stats.loc[freq_stats['freq'] >= 0, 'percent_sum'] = freq_stats['freq_sum'] / freq_stats_counts_all
    freq_stats.fillna(value=0, inplace=True)
    logger.info('successfully got the counts of x3')
    return freq_stats_count
