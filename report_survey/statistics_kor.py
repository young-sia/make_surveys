import logging

import numpy as np
import pandas as pd

logger = logging.getLogger('logger')


# 평균이 mu, 표준 편차가 sigma 인 정규 분포의 x값을 n개 만큼 구하기
# x~N(mu, sigma), 표본 개수: n
def normal_distribution(mu, sigma, n):
    logger.info('about to get normal distribution variable')
    samples = mu + sigma * np.random.randn(n)
    logger.info('successfully got normal distribution variable')
    return samples


# 명목 변수인 경우 만드는 n개의 표본
# 확률: prob, 명목 변수 종류: k개
def nominal_variance_with_my_probability(k, n, prob):
    numbers = np.arange(1, k+1)
    logger.info(f'list: {numbers}')
    samples = np.random.choice(numbers, size=n, replace=True, p=prob)
    return samples


# 다른 질문 1개의 답에 따라 현 질문의 명목 변수 값이 변화할 떄
# 명목 변수 종류: k개, 조건이 되는 질문지: condition, 각 경우별 확률: prob(dataframe의 구조를 지니고 있다)
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


# 생성 데이터에 대한 기초통계량(평균, 표준편차, 최솟값, 최댓값)
def get_basic_statistics(data, n):
    logger.info('about to get the basic statistics')
    basic_stats_data = pd.DataFrame({'x1': [np.mean(data['x1']), np.std(data['x1']), np.min(data['x1']),
                                            np.max(data['x1'])]}, index=['평균', '표준편차', '최솟값', '최댓값'])
    for k in range(1, n+1):
        basic_stats_data = pd.concat([basic_stats_data, pd.DataFrame({f'x{k}': [np.mean(data[f'x{k}']),
                                                                                np.std(data[f'x{k}']),
                                                                                np.min(data[f'x{k}']),
                                                                                np.max(data[f'x{k}'])]},
                                                                                index=['평균', '표준편차', '최솟값', '최댓값'])],
                                     axis=1, ignore_index=False)
    logger.info('successfully got basic statistics')
    return basic_stats_data


# 범주형 data에 대한 기초 통계량(빈도수, 백분율, 누적 빈도, 누적 백분율 )
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
    freq_stats = pd.DataFrame({f'{x}': variable, '빈도': freq})
    freq_stats.sort_values(f'{x}', ascending=True, inplace=True)
    freq_stats.fillna(value=0, inplace=True)
    freq_stats['누적 빈도'] = freq_stats.freq.cumsum()
    freq_stats_counts_all = sum(freq_sum for freq_sum in freq)
    freq_stats.loc[freq_stats['빈도'] >= 0, '백분율'] = freq_stats['빈도'] / freq_stats_counts_all
    freq_stats.loc[freq_stats['빈도'] >= 0, '누적 백분율'] = freq_stats['누적 빈도'] / freq_stats_counts_all
    freq_stats.fillna(value=0, inplace=True)
    logger.info('successfully got the freq_counts')
    return freq_stats
