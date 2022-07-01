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


# This is for the question that's answer gets effect from other question
# This case is when the sample x forms normal distribution that gets effect from
# two different questions.
# The condition is questions that affects to the samples I want to make.
# Even though this definition can only cover 2 questions, my final goal is
# not to get affected of the number of conditions
# condition: 2 questions, probs: the probabilities(in the form of normal distribution in each cases)
# n: number of samples I want to get
def normal_distribution_with_condition(condition, prob, n):
    cond_count = dict()
    cond2_count = list()
    # condition.iloc[:,:] is from pandas package.
    # It figures out which row and columns to pick by numbers. It does not care what the number of row or column has
    # [a,b]: a means pick a column and b means b row.
    # In the Dataframe starts with 0.
    # This is to count how many same variable(in form of (a,b).)
    # For example, if first condition is [1,2,1,1] and second condition is [1,1,3,1],
    # (In this case, the answer of 1st person will be 1 in first condition, and 1 in second condition)
    #  size ={
    #      1:{
    #          1:{
    #              'count':2
    #          }
    #          3:{
    #              'count':1
    #          }
    #      }
    #      2:{
    #          1:{
    #              'count':1
    #          }
    #
    #      }
    #  }

    for effect1 in condition.iloc[:, 1]:  # pick all columns in 2nd row.
        if effect1 not in cond2_count:
            cond2_count += [effect1]
    for effect2 in condition.iloc[:, 0]:  # pick all columns in 1st row.
        if effect2 not in cond_count:
            cond_count[effect2] = dict()
            for row_count in cond2_count:
                if row_count not in cond_count[effect2]:
                    cond_count[effect2][row_count] = {
                        'count': 0  # It is to count how many certain variables in each case has.
                     }
    for row_count in range(0, n):
        effect2 = condition.iloc[row_count, 0]
        freq_temp = condition.iloc[row_count, 1]
        cond_count[effect2][freq_temp]['count'] += 1

    # Using cond_count, make samples from it
    samples = dict()
    for key in cond_count:
        for key2 in cond_count[key]:
            if cond_count[key][key2]['count'] != 0:
                samples[key] = {
                    key2: normal_distribution(prob[key][key2][0], prob[key][key2][1], cond_count[key][key2]['count'])
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
# This definition can hold only 1 condition. My goal is to make it work no matter how many conditions
# I need to put.
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
