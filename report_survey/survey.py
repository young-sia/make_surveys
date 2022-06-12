import logging
import numpy as np
import pandas as pd

from report_survey.statistics import normal_distribution


logger = logging.getLogger('logger')


# making an arbitrary survey with questions- 3 questions: 2 continuous variable+ 1 nominal variable
def make_random_survey_example(n):
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


