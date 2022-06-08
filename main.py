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


# making an arbitrary survey with questions- 3 questions: 2 continuous variable+ 1 nominal variable
def make_random_survey(n):
    logger.info('about to get random survey')
    data = pd.DataFrame({'x': np.arange(1, n+1)})
    logger.info('successfully got list data')
    x1 = normal_distribution(171, 3, n)
    x2 = normal_distribution(300000, 50000, n)
    logger.info('about to get random nominal variable')
    prob = [0.31, 0.27, 0.20, 0.1, 0.1, 0.01, 0.01]
    numbers = [1, 2, 3, 4, 5, 6, 7]
    x3 = np.random.choice(numbers, size=n, replace=True, p=prob)
    logger.info('successfully got random nominal variable')
    logger.info('about to append each list')
    data['x1'] = x1
    data['x2'] = x2
    data['x3'] = x3
    logger.info('successfully got the data')
    return data


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


# simple random sampling method(SRS)
def simple_random_sampling(data, n):
    logger.info('about to do simple random sampling')
    print("Selection Method: Simple Random Sampling")
    sample_data = data.sample(n, replace=False)
    print("Sample Size : ", n)
    logger.info('successfully got random sample')
    return sample_data


# systematic sampling method
def sys_sampling(data, k):
    total_n = len(data)
    section_k = total_n // k
    index = data[:section_k].sample(1).index
    sys_sample = pd.DataFrame()
    while len(sys_sample) < k:
        sys_sample = sys_sample.append(data.loc[index, :])
        index += section_k
    return sys_sample


# stratified random sampling

# cluster random sampling


def main():
    test = make_random_survey(5000)
    basic_stats_test = get_basic_statistics(test)
    freq_statistics = get_freq_statistics(test)
    sample_test1 = simple_random_sampling(test, 50)
    sample_test2 = simple_random_sampling(test, 10)
    basic_stats_sample1 = get_basic_statistics(sample_test1)
    basic_stats_sample2 = get_basic_statistics(sample_test2)
    # population
    print(test)
    print(basic_stats_test)
    print(freq_statistics)
    # SRS method sampling
    print(basic_stats_sample1)
    # systematic sampling method
    print(basic_stats_sample2)
    # stratified random sampling
    # cluster random sampling


if __name__ == '__main__':
    main()
