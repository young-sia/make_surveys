import logging
import random as rd

import pandas as pd
from sklearn.model_selection import train_test_split

logger = logging.getLogger('logger')


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
    # intoin = index - 0
    sys_sample = pd.DataFrame()
    while len(sys_sample) < k:
        sys_sample = sys_sample.combine_first(data.loc[index, ...])
        index += section_k
    return sys_sample


# stratified random sampling
def stratified_sampling(data, criteria_name, n):
    logger.info('about to do stratified random sampling')
    c = criteria_name
    split_ratio = n/len(data)
    logger.info(f'got total number of population as {split_ratio}')
    x_train, x_test, y_train, y_test = train_test_split(data.drop(columns=f'{criteria_name}'), data[f'{criteria_name}'],
                                                        test_size=split_ratio, shuffle=True, stratify=data[c])
    x_test[c] = y_test
    logger.info('successfully got the train data')
    return x_test


# cluster random sampling
def cluster_sampling(data, cluster_name, how_many_clusters_in_sampling):
    cluster_min = min(data[f'{cluster_name}'])
    cluster_max = max(data[f'{cluster_name}'])
    clustered_sample = pd.DataFrame()
    temp_count = dict()
    while how_many_clusters_in_sampling > 0:
        cluster_number = rd.randint(cluster_min, cluster_max)
        if cluster_number not in temp_count:
            temp_count[cluster_number] = {
                cluster_number: True
            }
            how_many_clusters_in_sampling = how_many_clusters_in_sampling - 1
            temp_data = data[data[f'{cluster_name}'] == cluster_number]
            clustered_sample = pd.concat([clustered_sample, temp_data])
    return clustered_sample
