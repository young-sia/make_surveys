import logging

from report_survey.survey import my_survey
from report_survey.statistics import get_basic_statistics, get_freq_statistics
from report_survey.sampling import simple_random_sampling, sys_sampling, stratified_sampling, cluster_sampling
import else_in_need.color as color

logger = logging.getLogger('logger')


def main():
    test = my_survey(1000)
    basic_stats_test = get_basic_statistics(test, 8)
    freq_statistics_x1 = get_freq_statistics(test, 'x1')
    freq_statistics_x2 = get_freq_statistics(test, 'x2')
    freq_statistics_x3 = get_freq_statistics(test, 'x3')
    freq_statistics_x4 = get_freq_statistics(test, 'x4')
    freq_statistics_x5 = get_freq_statistics(test, 'x5')
    freq_statistics_x6 = get_freq_statistics(test, 'x6')
    sample_test_rss = simple_random_sampling(test, 300)
    sample_test_sys = sys_sampling(test, 300)
    sample_test_str = stratified_sampling(test, 'x5', 300)
    sample_test_cls = cluster_sampling(test, 'x5', 3)
    basic_stats_sample_rss = get_basic_statistics(sample_test_rss, 8)
    basic_stats_sample_sys = get_basic_statistics(sample_test_sys, 8)
    basic_stats_sample_str = get_basic_statistics(sample_test_str, 8)
    basic_stats_sample_cls = get_basic_statistics(sample_test_cls, 8)

    # population
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
    # SRS method sampling
    print(color.green+"rss sampling result"+color.white)
    print(sample_test_rss)
    print("")
    print(color.green+"rss sampling basic statistics"+color.white)
    print(basic_stats_sample_rss)
    # systematic sampling method
    print(color.green+"sys sampling result"+color.white)
    print(basic_stats_sample_sys)
    # stratified random sampling
    print(color.green+"stratified sampling result"+color.white)
    print(basic_stats_sample_str)
    # cluster random sampling
    print(color.green+"cluster random sampling result"+color.white)
    print(basic_stats_sample_cls)


if __name__ == '__main__':
    main()
