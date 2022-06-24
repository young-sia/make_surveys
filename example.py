import logging

from report_survey.survey import random_survey_example1
from report_survey.statistics import get_basic_statistics, get_freq_statistics
from report_survey.sampling import simple_random_sampling

logger = logging.getLogger('logger')


def main():
    test = random_survey_example1(5000)
    basic_stats_test = get_basic_statistics(test, 10)
    freq_statistics = get_freq_statistics(test, 'x3')
    sample_test1 = simple_random_sampling(test, 50)
    sample_test2 = simple_random_sampling(test, 10)
    basic_stats_sample1 = get_basic_statistics(sample_test1, 10)
    basic_stats_sample2 = get_basic_statistics(sample_test2, 10)
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
