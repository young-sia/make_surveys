import logging

import numpy as np
import pandas as pd

logger = logging.getLogger('logger')


# Getting random values x that becomes a normal distribution
# x~N(mu, sigma), amount of samples: x
def normal_distribution(mu, sigma, n):
    logger.info('about to get normal distribution variable')
    samples = mu + sigma * np.random.randn(n)
    logger.info('successfully got normal distribution variable')
    return samples


def normal_distribution_with_condition(condition, prob, numbers):
    size = dict()
    size_2 = list()
    for n in condition.iloc[:, 1]:
        if n not in size_2:
            size_2 += [n]
    for m in condition.iloc[:, 0]:
        if m not in size:
            size[m] = dict()
            for k in size_2:
                if k not in size[m]:
                    size[m][k] = {
                        'count': 0
                     }
    for k in range(0, numbers):
        m = condition.iloc[k, 0]
        i = condition.iloc[k, 1]
        size[m][i]['count'] += 1
    samples = dict()
    for key in size:
        for key2 in size[key]:
            if size[key][key2]['count'] != 0:
                samples[key] = {
                    key2: normal_distribution(prob[key][key2][0], prob[key][key2][1], size[key][key2]['count'])
                }
    return samples


# Getting random values x that is made by probability i made
# Usually used in nominal variables
def nominal_variance_with_my_probability(k, n, prob):
    numbers = np.arange(1, k+1)
    logger.info(f'list: {numbers}')
    samples = np.random.choice(numbers, size=n, replace=True, p=prob)
    return samples


# If the probability of the samples are different due to the answer of one of the previous question
# There are k types of nominal variables, which each type has condition, and from each condition has
# probability prob(this is a Dataframe)
def nominal_variance_with_my_probability_with_condition(k, condition, prob):
    numbers = np.arange(1, k+1)
    logger.info(f'list: {numbers}')
    size = dict()
    for k in condition:
        if k not in size:
            size[k] = {
                'count': 1
            }
        else:
            size[k]['count'] += 1
    list_size = [size[k]['count'] for k in size]
    samples = dict()
    for key in range(1, len(list_size)+1):
        samples[key] = {
            'samples': np.random.choice(numbers, size=list_size[key-1], replace=True, p=prob.iloc[:, key-1])
        }
    return samples


# Getting basic statistics data: mean, std, min, max
def get_basic_statistics(data, n):
    logger.info('about to get the basic statistics')
    basic_stats_data = pd.DataFrame({'x1': [np.mean(data['x1']), np.std(data['x1']), np.min(data['x1']),
                                            np.max(data['x1'])]}, index=['mean', 'std', 'min', 'max'])
    for k in range(1, n+1):
        basic_stats_data = pd.concat([basic_stats_data, pd.DataFrame({f'x{k}': [np.mean(data[f'x{k}']),
                                                                                np.std(data[f'x{k}']),
                                                                                np.min(data[f'x{k}']),
                                                                                np.max(data[f'x{k}'])]},
                                                                                index=['mean', 'std', 'min', 'max'])],
                                     axis=1, ignore_index=False)
    logger.info('successfully got basic statistics')
    return basic_stats_data


# Getting frequency statistics data from nominal variable: freq, cumulative, percentage, cumulative percentage
def get_freq_statistics(data, x):
    logger.info('about to get the freq statistics')
    var = dict()
    for k in data.loc[:, f'{x}']:
        if k not in var:
            var[k] = {
                'count': 1
            }
        else:
            var[k]['count'] += 1
    variable = [k for k in var]
    freq = [var[k]['count'] for k in var]
    freq_stats = pd.DataFrame({f'{x}': variable, 'freq': freq})
    freq_stats.sort_values(f'{x}', ascending=True, inplace=True)
    freq_stats.fillna(value=0, inplace=True)
    freq_stats['freq_sum'] = freq_stats.freq.cumsum()
    freq_stats_counts_all = sum(freq_sum for freq_sum in freq)
    freq_stats.loc[freq_stats['freq'] >= 0, 'percent'] = freq_stats['freq'] / freq_stats_counts_all
    freq_stats.loc[freq_stats['freq'] >= 0, 'percent_sum'] = freq_stats['freq_sum'] / freq_stats_counts_all
    freq_stats.fillna(value=0, inplace=True)
    logger.info('successfully got the freq_counts')
    return freq_stats
