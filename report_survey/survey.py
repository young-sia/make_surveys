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


# Questions are from my_survey.txt
def my_survey(n):
    # Getting probability of nominal variances
    logger.info('about to get random survey')
    prob1 = [0.5, 0.5]
    prob2 = [0.578, 0.1, 0.087, 0.01, 0.225]
    prob3 = [0.186, 0.259, 0.258, 0.297]
    prob4 = [0.573, 0.155, 0.234, 0.038]
    prob5 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    logger.info('got all the probabilities of nominal variances')
    # since Q6 gets effect from Q2, the probability of variables of Q6 is different
    prob6 = pd.DataFrame({'고등학교': [0.195, 0.166, 0.368, 0.271], '전문대': [0.393, 0.135, 0.069, 0.403],
                           '4년제 대학교': [0.393, 0.135, 0.174, 0.298], '대학원': [0.393, 0.135, 0.174, 0.298],
                           '기타': [0.03, 0.083, 0.389, 0.498]})
    prob8 = ({1: {1: [102.4, 8], 2: [51.9, 8], 3: [30.3, 8], 4: [30.3, 16]},
              2: {1: [112.9, 8], 2: [54.6, 8], 3: [30.3, 8], 4: [30.3, 16]},
              3: {1: [142.8, 8], 2: [70.8, 8], 3: [30.3, 8], 4: [30.3, 16]},
             4: {1: [215.4, 8], 2: [85.2, 8], 3: [30.3, 8], 4: [30.3, 16]},
              5: {1: [88.8, 8], 2: [46.6, 8], 3: [30.3, 8], 4: [30.3, 16]}})
    logger.info('got all the probabilities of nominal variances')
    logger.info(f'about to get random samples:{n}')
    # making variables
    x1 = nominal_variance_with_my_probability(2, n, prob1)
    x2 = nominal_variance_with_my_probability(5, n, prob2)
    x3 = nominal_variance_with_my_probability(4, n, prob3)
    x4 = nominal_variance_with_my_probability(4, n, prob4)
    x5 = nominal_variance_with_my_probability(10, n, prob5)
    x6_dic = nominal_variance_with_my_probability_with_condition(4, x2, prob6)
    x6_sub = list()
    for k in range(0, n):
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        if x2[k] == 1:
            x6_sub += [x6_dic[1]['samples'][a]]
            a += 1
        elif x2[k] == 2:
            x6_sub += [x6_dic[2]['samples'][b]]
            b += 1
        elif x2[k] == 3:
            x6_sub += [x6_dic[3]['samples'][c]]
            c += 1
        elif x2[k] == 4:
            x6_sub += [x6_dic[4]['samples'][d]]
            d += 1
        else:
            x6_sub += [x6_dic[5]['samples'][e]]
            e += 1
    x6 = np.transpose(x6_sub)
    x7 = normal_distribution(30, 30, n)
    x8_condition = pd.DataFrame({'x2': x2, 'x6': x6})
    x8_sub = normal_distribution_with_condition(x8_condition, prob8, n)
    x8 = list()
    for a in range(0, n):
        b = x8_condition.iloc[a, 0]
        c = x8_condition.iloc[a, 1]
        i11 = 0
        i12 = 0
        i13 = 0
        i14 = 0
        i21 = 0
        i22 = 0
        i23 = 0
        i24 = 0
        i31 = 0
        i32 = 0
        i33 = 0
        i34 = 0
        i41 = 0
        i42 = 0
        i43 = 0
        i44 = 0
        i51 = 0
        i52 = 0
        i53 = 0
        i54 = 0
        if b == 1:
            if c == 1:
                x8 += [x8_sub[1][1][i11]]
                i11 += 1
            elif c == 2:
                x8 += [x8_sub[1][2][i12]]
                i12 += 1
            elif c == 3:
                x8 += [x8_sub[1][3][i13]]
                i13 += 1
            elif c == 4:
                x8 += [x8_sub[1][4][i14]]
                i14 += 1
        elif b == 2:
            if c == 1:
                x8 += [x8_sub[2][1][i21]]
                i21 += 1
            elif c == 2:
                x8 += [x8_sub[2][2][i22]]
                i22 += 1
            elif c == 3:
                x8 += [x8_sub[2][3][i23]]
                i23 += 1
            elif c == 4:
                x8 += [x8_sub[2][4][i24]]
                i24 += 1
        elif b == 3:
            if c == 1:
                x8 += [x8_sub[3][1][i31]]
                i31 += 1
            elif c == 2:
                x8 += [x8_sub[3][2][i32]]
                i32 += 1
            elif c == 3:
                x8 += [x8_sub[3][3][i33]]
                i33 += 1
            elif c == 4:
                x8 += [x8_sub[3][4][i34]]
                i34 += 1
        elif b == 4:
            if c == 1:
                x8 += [x8_sub[4][1][i41]]
                i41 += 1
            elif c == 2:
                x8 += [x8_sub[4][2][i42]]
                i42 += 1
            elif c == 3:
                x8 += [x8_sub[4][3][i43]]
                i43 += 1
            elif c == 4:
                x8 += [x8_sub[4][4][i44]]
                i44 += 1
        elif b == 5:
            if c == 1:
                x8 += [x8_sub[5][1][i51]]
                i51 += 1
            elif c == 2:
                x8 += [x8_sub[5][2][i52]]
                i52 += 1
            elif c == 3:
                x8 += [x8_sub[5][3][i53]]
                i53 += 1
            elif c == 4:
                x8 += [x8_sub[5][4][i54]]
                i54 += 1
    x8 = np.transpose(x8)
    logger.info('successfully got all the samples')
    data = pd.DataFrame({'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5,
                         'x6': x6, 'x7': x7, 'x8': x8})
    logger.info('successfully got the dataframe')
    return data
