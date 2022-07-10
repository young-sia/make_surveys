import logging
import numpy as np
import pandas as pd

from report_survey.statistics import normal_distribution, nominal_variance_with_my_probability,\
    nominal_variance_with_my_probability_with_condition, normal_distribution_with_condition


logger = logging.getLogger('logger')


# making an arbitrary survey with questions- 3 questions: 2 continuous variable+ 1 nominal variable
def random_survey_example1(n):
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


# Questions and notices are in my_survey.txt, survey_question folder
#  Q2 affects Q6 and Q8, Q6 affects Q8
# TODO: data does not belong in code. move this data to some csv files or something and read them in
def my_survey(n):
    # Getting probability of nominal variances
    logger.info('about to get random survey')
    prob1 = [0.5, 0.5]  # nominal variance
    prob2 = [0.578, 0.1, 0.087, 0.01, 0.225]  # nominal variable
    prob3 = [0.186, 0.259, 0.258, 0.297]    # nominal variable
    prob4 = [0.573, 0.155, 0.234, 0.038]    # nominal variable
    prob5 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    logger.info('got all the probabilities of nominal variances')
    # since Q6 gets effect from Q2, the probability of variables of Q6 is different(has 5 lists)
    prob6 = pd.DataFrame({'high school': [0.195, 0.166, 0.368, 0.271], 'college': [0.393, 0.135, 0.069, 0.403],
                           'university': [0.393, 0.135, 0.174, 0.298], 'graduate school': [0.393, 0.135, 0.174, 0.298],
                           'else': [0.03, 0.083, 0.389, 0.498]})
    # Q2 and Q6 affects Q8. So there are total 20 lists : 5types of answers from Q2, 4 types of answers from Q6
    prob8 = ({1: {1: [102.4, 8], 2: [51.9, 8], 3: [30.3, 8], 4: [30.3, 16]},
              2: {1: [112.9, 8], 2: [54.6, 8], 3: [30.3, 8], 4: [30.3, 16]},
              3: {1: [142.8, 8], 2: [70.8, 8], 3: [30.3, 8], 4: [30.3, 16]},
             4: {1: [215.4, 8], 2: [85.2, 8], 3: [30.3, 8], 4: [30.3, 16]},
              5: {1: [88.8, 8], 2: [46.6, 8], 3: [30.3, 8], 4: [30.3, 16]}})
    logger.info('got all the probabilities of nominal variances')
    logger.info(f'about to get random samples:{n}')

    # making lists of variables
    x1 = nominal_variance_with_my_probability(2, n, prob1)
    x2 = nominal_variance_with_my_probability(5, n, prob2)
    x3 = nominal_variance_with_my_probability(4, n, prob3)
    x4 = nominal_variance_with_my_probability(4, n, prob4)
    x5 = nominal_variance_with_my_probability(10, n, prob5)
    # Q6 gets from Q2. So it uses different definition
    # The function nominal_variance_with_my_probability_with_condition is samples that are
    # not ordered properly due way of samples I got. Also, x6_dic is in form of a dictionary
    # So I made new list to make the list in right order.
    # For example, if
    # x6_dic = {1:{'samples': 4,2,5}, 2:{'samples': 3,1,1}} and x2=[2,1,1,2,2,1],
    # x6 = [3,4,2,1,1,5]
    # TODO: why is is this a dictionary if your keys are numbers? why not a list?
    x6_dic = nominal_variance_with_my_probability_with_condition(4, x2, prob6)
    x6_original = [0]*5
    x6_sub = list()
    for row_num in range(n):
        # TODO: why are we counting from 1???
        for sample_set_index in range(1, 6):
            if x2[row_num] == sample_set_index:
                # TODO(TheBeege): fix this
                # breaks here. the values in x6_original are dynamic, and there's no constraint ensuring that
                # the values in x6_original don't exceed the length of the number of values in x6_dic[n]['samples']
                x6_sub += [x6_dic[sample_set_index]['samples'][x6_original[sample_set_index-1]]]
                x6_original[sample_set_index-1] += 1

    # x6_sub is 1*n list. However, other lists I need to merge are n*1 list. So I transposed it
    x6 = np.transpose(x6_sub)

    x7 = normal_distribution(30, 30, n)

    # TODO: why do x2 and x6 affect x8??? what are these x's???
    # TODO: don't use "x" unless you're working in geometric coordinate space
    # TODO: what is this order?
    # TODO: what is "condition" in this context?
    # TODO: your example doesn't actually explain anything. what?
    # TODO: when writing nested data structures, use newlines and indentation
    # x2 and x6 affects x8. Like x6, I needed to make it in right order. So I fixed the order to match up with
    # other answers properly. For example, if
    # x8_condition = {1: {1: {2,3,1}, 3: {4,4}}, 2:{3: {2,1}} }, x2 = [1,1,1,2,1,2,1], x6 = [1,1,3,3,3,3,1]
    # it should be x8= [2,3,4,2,4,1,1]
    x8_condition = pd.DataFrame({'x2': x2, 'x6': x6})
    x8_sub = normal_distribution_with_condition(x8_condition, prob8, n)
    x8 = list()
    for row_num in range(0, n):
        x6_2 = x8_condition.iloc[row_num, 0]
        x6_3 = x8_condition.iloc[row_num, 1]
        # TODO: this is the most absurd variable name i've ever seen, but it's accurate given my limited understanding
        x6_2_by_x6_3_values = [[0]*4]*5
        for x6_2_index in range(5):
            for x6_3_index in range(4):
                # TODO: if we counted by 0 (i.e. used a list instead of a dictionary), we could skip this i+1 nonsense
                # TODO: something tells me that if i understood iloc better, we could avoid this
                if x6_2 == x6_2_index + 1 and x6_3 == x6_3_index + 1:
                    x8 += [
                        x8_sub[x6_2_index+1][x6_3_index+1][
                            x6_2_by_x6_3_values[x6_2_index][x6_3_index]
                        ]
                    ]
                    x6_2_by_x6_3_values[x6_2_index][x6_3_index] += 1

    # x6_sub is 1*n list. However, other lists I need to merge are n*1 list. So I transposed it
    x8 = np.transpose(x8)
    logger.info('successfully got all the samples')

    data = pd.DataFrame({'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5,
                         'x6': x6, 'x7': x7, 'x8': x8})

    logger.info('successfully got the dataframe')
    return data
