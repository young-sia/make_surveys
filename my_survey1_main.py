import logging

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
    # Get frequency statistics of the nominal variables
    freq_statistics_x1 = get_freq_statistics(test, 'x1')
    freq_statistics_x2 = get_freq_statistics(test, 'x2')
    freq_statistics_x3 = get_freq_statistics(test, 'x3')
    freq_statistics_x4 = get_freq_statistics(test, 'x4')
    freq_statistics_x5 = get_freq_statistics(test, 'x5')
    freq_statistics_x6 = get_freq_statistics(test, 'x6')
    logger.info("Successfully got all population")

    logger.info("trying to get samples sampled in 4 types of sampling: SRS, sys, str, cls")
    # Get samples of 300, using 4 types of sample
    sample_test_srs = simple_random_sampling(test, 100)
    sample_test_sys = sys_sampling(test, 100)
    sample_test_str = stratified_sampling(test, 'x5', 100)
    # However, cluster sampling may not get 300 samples, so if it gets less than 300,
    # get new cluster. If the sample is bigger than 300, get random 300 samples from it
    # by using simple_random_variable
    # temp is just to get enough loop to get 300 samples
    temp = 0
    while temp < 1000:
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
    freq_statistics_rss_x1 = get_freq_statistics(sample_test_srs, 'x1')
    freq_statistics_rss_x2 = get_freq_statistics(sample_test_srs, 'x2')
    freq_statistics_rss_x3 = get_freq_statistics(sample_test_srs, 'x3')
    freq_statistics_rss_x4 = get_freq_statistics(sample_test_srs, 'x4')
    freq_statistics_rss_x5 = get_freq_statistics(sample_test_srs, 'x5')
    freq_statistics_rss_x6 = get_freq_statistics(sample_test_srs, 'x6')

    freq_statistics_sys_x1 = get_freq_statistics(sample_test_sys, 'x1')
    freq_statistics_sys_x2 = get_freq_statistics(sample_test_sys, 'x2')
    freq_statistics_sys_x3 = get_freq_statistics(sample_test_sys, 'x3')
    freq_statistics_sys_x4 = get_freq_statistics(sample_test_sys, 'x4')
    freq_statistics_sys_x5 = get_freq_statistics(sample_test_sys, 'x5')
    freq_statistics_sys_x6 = get_freq_statistics(sample_test_sys, 'x6')

    freq_statistics_str_x1 = get_freq_statistics(sample_test_str, 'x1')
    freq_statistics_str_x2 = get_freq_statistics(sample_test_str, 'x2')
    freq_statistics_str_x3 = get_freq_statistics(sample_test_str, 'x3')
    freq_statistics_str_x4 = get_freq_statistics(sample_test_str, 'x4')
    freq_statistics_str_x5 = get_freq_statistics(sample_test_str, 'x5')
    freq_statistics_str_x6 = get_freq_statistics(sample_test_str, 'x6')

    freq_statistics_cls_x1 = get_freq_statistics(sample_test_cls, 'x1')
    freq_statistics_cls_x2 = get_freq_statistics(sample_test_cls, 'x2')
    freq_statistics_cls_x3 = get_freq_statistics(sample_test_cls, 'x3')
    freq_statistics_cls_x4 = get_freq_statistics(sample_test_cls, 'x4')
    freq_statistics_cls_x5 = get_freq_statistics(sample_test_cls, 'x5')
    freq_statistics_cls_x6 = get_freq_statistics(sample_test_cls, 'x6')
    logger.info("successfullly got all statistics data")

    # # The sentence below is to save the population data in csv
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
    print(freq_statistics_x1)
    print("")
    print(freq_statistics_x2)
    print("")
    print(freq_statistics_x3)
    print("")
    print(freq_statistics_x4)
    print("")
    print(freq_statistics_x5)
    print("")
    print(freq_statistics_x6)

    # Print SRS method sampling
    print(color.green+"rss sampling result"+color.white)
    print(sample_test_srs)
    print("")
    print(color.green+"rss sampling basic statistics"+color.white)
    print(basic_stats_sample_rss)
    print("")
    print(freq_statistics_rss_x1)
    print("")
    print(freq_statistics_rss_x2)
    print("")
    print(freq_statistics_rss_x3)
    print("")
    print(freq_statistics_rss_x4)
    print("")
    print(freq_statistics_rss_x5)
    print("")
    print(freq_statistics_rss_x6)
    print("")

    # Print systematic sampling method
    print(color.green+"sys sampling result"+color.white)
    print(basic_stats_sample_sys)
    print("")
    print(freq_statistics_sys_x1)
    print("")
    print(freq_statistics_sys_x2)
    print("")
    print(freq_statistics_sys_x3)
    print("")
    print(freq_statistics_sys_x4)
    print("")
    print(freq_statistics_sys_x5)
    print("")
    print(freq_statistics_sys_x6)
    print("")

    # Print stratified random sampling
    print(color.green+"stratified sampling result"+color.white)
    print(basic_stats_sample_str)
    print("")
    print(freq_statistics_str_x1)
    print("")
    print(freq_statistics_str_x2)
    print("")
    print(freq_statistics_str_x3)
    print("")
    print(freq_statistics_str_x4)
    print("")
    print(freq_statistics_str_x5)
    print("")
    print(freq_statistics_str_x6)

    # Print cluster random sampling
    print(color.green+"cluster random sampling result"+color.white)
    print(basic_stats_sample_cls)
    print("")
    print(freq_statistics_cls_x1)
    print("")
    print(freq_statistics_cls_x2)
    print("")
    print(freq_statistics_cls_x3)
    print("")
    print(freq_statistics_cls_x4)
    print("")
    print(freq_statistics_cls_x5)
    print("")
    print(freq_statistics_cls_x6)
    logger.info("successfully printed all data I want")


if __name__ == '__main__':
    main()
