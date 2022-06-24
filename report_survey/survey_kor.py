import logging
import numpy as np
import pandas as pd

from report_survey.statistics import normal_distribution, nominal_variance_with_my_probability,\
    nominal_variance_with_my_probability_with_condition


logger = logging.getLogger('logger')


# 임의의 n개의 모집단 데이터 생성
def random_survey_example1(n):
    logger.info('about to get random survey')

    # 모집단 데이터를 data라고 명명함
    data = pd.DataFrame({'x': np.arange(1, n+1)})
    logger.info('successfully got list data')
    x1 = normal_distribution(171, 3, n)
    x2 = normal_distribution(300000, 50000, n)
    logger.info('about to get random nominal variable')

    # 미지수가 명목 척도일 때 임의의 표본을 뽑기
    prob = [0.31, 0.27, 0.20, 0.1, 0.1, 0.01, 0.01]
    numbers = [1, 2, 3, 4, 5, 6, 7]
    x3 = np.random.choice(numbers, size=n, replace=True, p=prob)
    logger.info('successfully got random nominal variable')
    logger.info('about to append each list')

    # 각 미지수 별로 자료 합치기
    data['x1'] = x1
    data['x2'] = x2
    data['x3'] = x3
    logger.info('successfully got the data')
    return data


# 이 설문지는 my_survey_kor을 참고하면 된다.
def my_survey(n):
    logger.info('about to get random my_survey')
    # 미지수가 명목 척도일 때 임의의 표본을 뽑기(6개)
    prob1 = [0.5, 0.5]
    prob2 = [0.578, 0.1, 0.087, 0.01, 0.225]
    prob3 = [0.186, 0.259, 0.258, 0.297]
    prob4 = [0.573, 0.155, 0.234, 0.038]
    prob5 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    logger.info('got all the probabilities of nominal variances')
    # 6번 질문은 2번 질문의 영향을 받으므로 2번 질문의 답에 따라 확률이 다른 것을 반영했다.
    prob6 = pd.DataFrame({'고등학교': [0.195, 0.166, 0.368, 0.271], '전문대': [0.393, 0.135, 0.069, 0.403],
                           '4년제 대학교': [0.393, 0.135, 0.174, 0.298], '대학원': [0.393, 0.135, 0.174, 0.298],
                           '기타': [0.03, 0.083, 0.389, 0.498]})
    logger.info('got all the probabilities of nominal variances')
    logger.info(f'about to get random samples:{n}')

    # 각 질문에 따른 변수 생성
    x1 = nominal_variance_with_my_probability(2, n, prob1)
    x2 = nominal_variance_with_my_probability(5, n, prob2)
    x3 = nominal_variance_with_my_probability(4, n, prob3)
    x4 = nominal_variance_with_my_probability(4, n, prob4)
    x5 = nominal_variance_with_my_probability(10, n, prob5)

    # 6번 질문의 경우 2번의 영향을 받으므로 그 사항을 반영했다.
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
    # 이렇게 생성된 list는 n*1행렬이 아니므로 전치시켜준다.
    x6 = np.transpose(x6_sub)

    # 질문 7~10번
    x7 = normal_distribution(30, 15, n)
    x8 = normal_distribution(20, 6, n)
    x9 = normal_distribution(25, 10, n)
    x10 = normal_distribution(30, 5, n)
    logger.info('successfully got all the samples')

    # 모집단 데이터 data 생성
    data = pd.DataFrame({'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5,
                         'x6': x6, 'x7': x7, 'x8': x8, 'x9': x9, 'x10': x10})
    logger.info('successfully got the dataframe')
    return data
