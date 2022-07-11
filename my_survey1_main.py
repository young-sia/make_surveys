import logging
from typing import List, Dict

from report_survey.survey import my_survey
from report_survey.statistics import get_basic_statistics, get_freq_statistics
from report_survey.sampling import simple_random_sampling, sys_sampling, stratified_sampling, cluster_sampling
import else_in_need.color as color

logger = logging.getLogger('logger')


def main():
    logger.info("Trying to make population using python")
    # Make population
    test = my_survey(3000)
    # Get basic statistic result of the population
    basic_stats_test = get_basic_statistics(test, 8)

    x_values: List[Dict] = [{}] * 6

    # Get frequency statistics of the nominal variables
    for i in range(len(x_values)):
        x_values[i]['frequency_statistics'] = get_freq_statistics(test, f'x{i+1}')
    logger.info("Successfully got all population")

    logger.info("trying to get samples sampled in 4 types of sampling: SRS, sys, str, cls")
    # Get samples of 300, using 4 types of sample
    sample_test_srs = simple_random_sampling(test, 100)
    sample_test_sys = sys_sampling(test, 100)
    # why only 5?
    sample_test_str = stratified_sampling(test, 'x5', 100)
    # However, cluster sampling may not get 300 samples, so if it gets less than 300,
    # get new cluster. If the sample is bigger than 300, get random 300 samples from it
    # by using simple_random_variable
    # temp is just to get enough loop to get 300 samples
    temp = 0
    while temp < 1000:
        # again, why only 5?
        sample_test_cls_sub = cluster_sampling(test, 'x5', 3)
        if len(sample_test_cls_sub) >= 100:
            sample_test_cls = simple_random_sampling(sample_test_cls_sub, 100)
            break
        else:
            continue
    logger.info("successfully got all samples")

    logger.info("Trying to get basic statistics and frequency statistics")
    # Get basic statistic results of 4 types of samplings
    basic_stats_sample_rss = get_basic_statistics(sample_test_srs, 8)
    basic_stats_sample_sys = get_basic_statistics(sample_test_sys, 8)
    basic_stats_sample_str = get_basic_statistics(sample_test_str, 8)
    basic_stats_sample_cls = get_basic_statistics(sample_test_cls, 8)

    # Get frequency statistic results of 4 types of samplings
    # srs
    for i in range(len(x_values)):
        x_values[i]['rss'] = get_freq_statistics(sample_test_srs, f'x{i+1}')

    # sys
    for i in range(len(x_values)):
        x_values[i]['sys'] = get_freq_statistics(sample_test_sys, f'x{i+1}')

    # str
    for i in range(len(x_values)):
        x_values[i]['str'] = get_freq_statistics(sample_test_str, f'x{i+1}')

    # cls
    for i in range(len(x_values)):
        x_values[i]['cls'] = get_freq_statistics(sample_test_cls, f'x{i+1}')

    logger.info("successfullly got all statistics data")

    # The block below is to save the population data in csv
    # test.to_csv('my_survey1.csv', index=True)
    # sample_test_srs.to_csv('sample_test_srs.csv', index=True)
    # sample_test_sys.to_csv('sample_test_sys.csv', index=True)
    # sample_test_str.to_csv('sample_test_str.csv', index=True)
    # sample_test_cls.to_csv('sample_test_cls.csv', index=True)

    logger.info("print all the data I want to see.")
    # Print population data
    print(color.purple+"My First Survey"+color.white)
    print(test)
    print(color.purple+"Basic Statistics of Population"+color.white)
    print(basic_stats_test)
    print(color.purple+"Frequencies of nominal variables(x1~x6)"+color.white)
    for variable in x_values:
        print(f"{variable['frequency_statistics']}\n")

    # Print SRS method sampling
    print(color.green+"rss sampling result"+color.white)
    print(f'{sample_test_srs}\n')

    print(color.green+"rss sampling basic statistics"+color.white)
    print(f'{basic_stats_sample_rss}\n')
    for variable in x_values:
        print(f"{variable['rss']}\n")

    # Print systematic sampling method
    print(color.green+"sys sampling result"+color.white)
    print(f'{basic_stats_sample_sys}\n')
    for variable in x_values:
        print(f"{variable['sys']}\n")

    # Print stratified random sampling
    print(color.green+"stratified sampling result"+color.white)
    print(f"{basic_stats_sample_str}\n")
    for variable in x_values:
        print(f"{variable['str']}\n")

    # Print cluster random sampling
    print(color.green+"cluster random sampling result"+color.white)
    print(f"{basic_stats_sample_cls}\n")
    for variable in x_values:
        print(f"{variable['cls']}\n")
    logger.info("successfully printed all data I want")


if __name__ == '__main__':
    main()
